#include <Windows.h>

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <vector>
#include <map>
#include <set>
#include <list>

int SearchDirectory(
		std::vector<std::string> &refvecFiles,
		const std::string        &refcstrRootDirectory,
		const std::string        &refcstrExtension,
		bool                     bSearchSubdirectories = true)
{
	std::string     strFilePath;             // Filepath
	std::string     strPattern;              // Pattern
	std::string     strExtension;            // Extension
	HANDLE          hFile;                   // Handle to file
	WIN32_FIND_DATA FileInformation;         // File information


	strPattern = refcstrRootDirectory + "\\*." + refcstrExtension;

	hFile = ::FindFirstFile(strPattern.c_str(), &FileInformation);
	if(hFile != INVALID_HANDLE_VALUE)
	{
		do
		{
			if(FileInformation.cFileName[0] != '.')
			{
				strFilePath.erase();
				strFilePath = refcstrRootDirectory + "\\" + FileInformation.cFileName;

				if(FileInformation.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
				{
					if(bSearchSubdirectories)
					{
						// Search subdirectory
						int iRC = SearchDirectory(refvecFiles,
							strFilePath,
							refcstrExtension,
							bSearchSubdirectories);
						if(iRC)
							return iRC;
					}
				}
				else
				{
					refvecFiles.push_back(strFilePath);
				}
			}
		} while(::FindNextFile(hFile, &FileInformation) == TRUE);

		// Close handle
		::FindClose(hFile);

		DWORD dwError = ::GetLastError();
		if(dwError != ERROR_NO_MORE_FILES)
			return dwError;
	}
}

/************************************************************************/
/*                             MAIN                                     */
/************************************************************************/
int main(int argc, const char* argv[])
{
	/*
	 * Selecting input file
	 */
	if(argc < 2)
	{
		std::cerr << "Directory must be provided." << std::endl;
		return -1;
	}

	std::string roundDirectory(argv[1]);

	std::vector<std::string> filesList;
	SearchDirectory(filesList, roundDirectory, "in");

	std::string infilePath;
	if(filesList.size()>1)
	{
		unsigned int fileNumber = 0;
		for(std::vector<std::string>::iterator fileIt = filesList.begin();
			fileIt != filesList.end();
			++fileIt, ++fileNumber)
		{
			std::cout << fileNumber << " : " << *fileIt << std::endl;
		}
		std::cin >> fileNumber;
		infilePath = filesList[fileNumber];
	}
	else if (filesList.size()==1)
	{
		infilePath = filesList[0];
	}
	else
	{
		std::cerr << "No \".in\" file in directory : " << roundDirectory << std::endl;
		return -1;
	}

	std::string filenameBody(
		infilePath.substr(
			infilePath.find_last_of('\\')+1,
			infilePath.size()-infilePath.find_last_of('\\')-4 // -1 -".in".length()
		)
	);

	std::string outfilePath(roundDirectory + '\\' + filenameBody + ".out");

	std::cout << std::endl << "SELECTED FILE : " << infilePath << std::endl;
#ifdef DEBUG
	std::cout << "(" << outfilePath << ")" << std::endl;
#endif

	/*
	 * Reading selected file
	 */
	std::ifstream infile;
	infile.open (infilePath, std::ios::in);

	std::ofstream outfile;
	outfile.open (outfilePath, std::ios::out);


	std::string line;
	getline(infile, line);

	std::istringstream iss(line);

	unsigned int gNbCases;
	iss >> gNbCases;

#ifdef DEBUG
	std::cout << "Nb test cases : " << gNbCases << std::endl;
#endif

	//
	// Initialization
	//
	typedef std::map<unsigned int, std::pair<unsigned int, unsigned int> > LimitMap;
	typedef std::pair<unsigned int, unsigned int> LimitPair;
	typedef std::pair<unsigned int, LimitPair > LimitMapEntry;

	LimitMap gLimitsMap;

	//Border cases
	gLimitsMap.insert( LimitMapEntry(0, LimitPair(0, 0)) );
	gLimitsMap.insert( LimitMapEntry(1, LimitPair(1, 1)) );

	for(unsigned int totalValue=2;
		totalValue <= 10;
		++totalValue)
	{
		unsigned int normalMinimum = totalValue + 2*(totalValue-1);
		unsigned int surprisingMinimum = totalValue + 2*(totalValue-2);

		gLimitsMap.insert( LimitMapEntry(totalValue, LimitPair(normalMinimum, surprisingMinimum)) );
	}

#ifdef DEBUG
	for(LimitMap::iterator limitIt=gLimitsMap.begin();
		limitIt != gLimitsMap.end();
		++limitIt)
	{
		std::cout << "Limits for best score of " << limitIt->first 
			<< " : (normal)" << limitIt->second.first << "  (surpr)" <<  limitIt->second.second << std::endl;
	}
#endif

	//
	//  Cases
	//
	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
		/*
		 * Case analysis
		 */
#ifdef DEBUG
		std::cout << "\tTest case #" << testId << std::endl;
#endif
		getline(infile, line);
		std::istringstream iss(line);

		unsigned int N_numGooglers, S_numSurprises, p_bestResultValue;
		iss >> N_numGooglers >> S_numSurprises >> p_bestResultValue;

		unsigned int normalLimit = gLimitsMap[p_bestResultValue].first;
		unsigned int surpriseLimit = gLimitsMap[p_bestResultValue].second;

		unsigned int normalValidating(0);
		unsigned int surprisingCandidate(0);

		// Each total
		for(unsigned int totalId=0;
			totalId < N_numGooglers;
			++totalId)
		{
			unsigned int ti_totalScore;
			iss >> ti_totalScore;

			#ifdef DEBUG
			// Validated
			//std::cout << "Total for googler #" << totalId << " : " << ti_totalScore << std::endl;
			#endif

			if(ti_totalScore >= normalLimit)
			{
				++normalValidating;
			}
			else if(ti_totalScore >= surpriseLimit)
			{
				++surprisingCandidate;
			}
		}

	
		unsigned int result = normalValidating + min(surprisingCandidate, S_numSurprises);

#ifdef DEBUG
		// 		std::cout  << "Case #" << testId+1 << ": [";
		// 		if(gResult.size())
		// 		{
		// 			std::cout << gResult.front();
		// 			gResult.pop_front();
		// 
		// 			for(InvocationList::iterator resultIt=gResult.begin();
		// 				resultIt != gResult.end();
		// 				++resultIt)
		// 			{
		// 				std::cout << ", " << *resultIt;
		// 			}
		// 		}
		// 		std::cout << "]" << std::endl;
#endif
		outfile  << "Case #" << testId+1 << ": " << result << std::endl;


		/************************************************************************/
		/* ENDED CASE                                                           */
		/************************************************************************/
	}
	infile.close();
	outfile.close();
}