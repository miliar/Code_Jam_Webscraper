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
	// Init
	//
	typedef std::map<char, char> CharTranslationMap;
	CharTranslationMap googlereseToEnglish;
	CharTranslationMap englishToGooglerese;

	std::string exampleGooglerese = "z y qee ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	std::string exampleEnglish =    "q a zoo our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	std::string completeAlphabet = "abcdefghijklmnopqrstuwvxyz";

	for(std::string::iterator stringIt=exampleGooglerese.begin(), enIt=exampleEnglish.begin();
		stringIt != exampleGooglerese.end();
		++stringIt, ++enIt)
	{
		googlereseToEnglish.insert(std::pair<char, char>(*stringIt, *enIt));
		englishToGooglerese.insert(std::pair<char, char>(*enIt, *stringIt));
	}

#ifdef DEBUG
	std::cout << "Map size : " << googlereseToEnglish.size() << std::endl;

	for(std::string::iterator alphabetIt = completeAlphabet.begin();
		alphabetIt != completeAlphabet.end();
		++alphabetIt)
	{
		if(googlereseToEnglish.find(*alphabetIt) == googlereseToEnglish.end())
		{
			std::cout << "Missing in Googlerese : " << *alphabetIt << std::endl;
		}

		if(englishToGooglerese.find(*alphabetIt) == englishToGooglerese.end())
		{
			std::cout << "Missing in English : " << *alphabetIt << std::endl;
		}
	}

	for(CharTranslationMap::iterator enToGoIt = englishToGooglerese.begin();
		enToGoIt != englishToGooglerese.end();
		++enToGoIt)
	{
		std::cout << "\t" << enToGoIt->first << " -> " << enToGoIt->second << std::endl;
	}
#endif

	//
	// Cases
	//
	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
		/*
		 * Case analysis
		 */
		getline(infile, line);
	
		std::string result("");
		
		for(std::string::iterator inputIt = line.begin();
			inputIt != line.end();
			++inputIt)
		{
			result += googlereseToEnglish[*inputIt];
		}

#ifdef DEBUG

#endif
		outfile  << "Case #" << testId+1 << ": " << result << std::endl;


		/************************************************************************/
		/* ENDED CASE                                                           */
		/************************************************************************/
	}
	infile.close();
	outfile.close();
}