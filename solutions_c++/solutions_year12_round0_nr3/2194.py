#include <Windows.h>

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <algorithm>
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

	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
		/*
		 * Case analysis
		 */
		getline(infile, line);

		std::istringstream issTest(line);
		std::string A,B;
		issTest >> A >> B;

		unsigned int Bint;
		std::istringstream ossB(B);
		ossB >> Bint;

		unsigned int Aint;
		std::istringstream ossA(A);
		ossA >> Aint;

		unsigned int result(0);

		unsigned int permutationCount = A.length()-1;

		for(unsigned int CurrentInt=Aint;
			CurrentInt < Bint;
			++CurrentInt)
		{
			std::map<unsigned int, unsigned int> unicity;

			std::ostringstream ossC;
			ossC << CurrentInt;
			std::string C = ossC.str();
	
			for(unsigned int currentPermutation = 1;
				currentPermutation <= permutationCount;
				++currentPermutation)
			{
				std::rotate(C.begin(), C.end()-1, C.end());

	#ifdef DEBUG
	//			std::cout << "Permutation # " <<currentPermutation << " : " << C;
	#endif

				unsigned int CurrentPermut;
				std::istringstream ossC(C);
				ossC >> CurrentPermut;

				if( (CurrentPermut > CurrentInt) && (CurrentPermut <= Bint))
				{
					if(unicity.find(CurrentPermut) == unicity.end())
					{
						unicity[CurrentPermut] = 0;
						++result;
					}
				}
			}

		}

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