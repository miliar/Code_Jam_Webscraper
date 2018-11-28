// Ben Foxworthy
// 5-21-10

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <assert.h>

using namespace std;

struct Directory{
	char *name;
	Directory* subDirs[250];
	int numSubDirs;
};

static void FreeDirectory(Directory *a)
{
	for (int i=0; i < a->numSubDirs; i++){
		FreeDirectory(a->subDirs[i]);
		a->subDirs[i] = NULL;
	}
	free(a->name);
	free(a);
}

static int AddDirectory(Directory *root, const char *name)
{
	const char *startPos = name;
	const char *endPos;
	while (*startPos == '/'){
		++startPos;
	}
	endPos = startPos;
	while (*endPos != '/' && *endPos != '\0'){
		++endPos;
	}

	// We are done!
	if (*startPos == '\0'){
		return 0;
	}

	// Find subdir
	for (int i=0; i < root->numSubDirs; i++){
		if (strlen(root->subDirs[i]->name) == (endPos-startPos) && strncmp(root->subDirs[i]->name, startPos, (endPos-startPos))==0){
			return AddDirectory(root->subDirs[i], endPos);
		}
	}

	// Didn't exist
	assert(root->numSubDirs < 250);

	Directory *newDir = root->subDirs[root->numSubDirs++] = (Directory*)calloc(1, sizeof(Directory));
	newDir->name = (char*)malloc(endPos-startPos+1);
	strncpy(newDir->name, startPos, (endPos-startPos));
	newDir->name[(endPos-startPos)] = '\0';
	return 1 + AddDirectory(newDir, endPos);
}

int main(int argc, char *argv[])
{
	const char *inputFileName = NULL;
	char inputFileBuffer[256];
	if (argc == 2){
		inputFileName = argv[1];
	} else {
		cout << "Input file: ";
		cin >> inputFileBuffer;
		inputFileName = inputFileBuffer;
		cout << inputFileName << endl;
	}

	ifstream input(inputFileName);
	//ofstream output("output.txt");
	
	if (input.fail()){// || output.fail()){
		cout << "Error: Files couldn't be opened" << endl;
		system("PAUSE");
		return 1;
	}
	
	int numTestCases = 0;
	input >> numTestCases;
	
	for (int iCase = 0; iCase < numTestCases; iCase++){

		Directory *root = (Directory*)calloc(1, sizeof(Directory));
		unsigned int numExistingDirs = 0;
		unsigned int numNewDirs = 0;
		input >> numExistingDirs;
		input >> numNewDirs;

		for (unsigned int i = 0; i < numExistingDirs; i++){
			char buffer[1000];
			input >> buffer;
			AddDirectory(root, buffer);
		}

		int numAdded = 0;

		for (unsigned int i = 0; i < numNewDirs; i++){
			char buffer[1000];
			input >> buffer;
			numAdded += AddDirectory(root, buffer);
		}

		cout << "Case #" << iCase+1 << ": " << numAdded << endl;
		FreeDirectory(root);
	}
	
    return EXIT_SUCCESS;
}
