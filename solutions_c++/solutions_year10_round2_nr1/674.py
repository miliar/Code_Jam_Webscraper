// r1b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <map>

class Dir
{
public:
	typedef std::map<std::string, Dir> TChildren;
	TChildren children;

	int AddPath(std::string strPath)
	{
		if (strPath.length() == 0) return 0;
		if (strPath[0] == '/') strPath = strPath.substr(1);
		
		int iLength = strPath.find('/');
		if (iLength == std::string::npos) iLength = strPath.length();
		
		std::string strFolder = strPath.substr(0, iLength);
		std::string strRemain = strPath.substr(iLength);

		TChildren::iterator iter = children.find(strFolder);
		if (iter == children.end())
		{
			return 1 + children[strFolder].AddPath(strRemain);
		}
		else
		{
			return iter->second.AddPath(strRemain);
		}
	}

	void Clear()
	{
		children.clear();
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
    FILE * fIn = fopen("A-large.in", "r");
    FILE * fOut = fopen("test.out", "w");

    int nTests = 0;
    fscanf(fIn, "%d", &nTests);
    printf("%d tests", nTests);

	Dir root;

    for (int iTest = 1; iTest <= nTests; iTest++)
    {
        root.Clear();
		
		int n, m; fscanf(fIn, "%d %d", &n, &m);
		printf("test: %d\n", iTest);

		char path[256];
		for (int i = 0; i < n; i++)
		{
			fscanf(fIn, "%s", path);
			root.AddPath(std::string(path));
		}

		int iRes = 0;
		for (int i = 0; i < m; i++)
		{
			fscanf(fIn, "%s", path);
			iRes += root.AddPath(std::string(path));
		}

        fprintf(fOut, "Case #%d: %d\n", iTest, iRes);
    }
	return EXIT_SUCCESS;
}
