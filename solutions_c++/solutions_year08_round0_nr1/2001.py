#include <stdio.h>
#include <string.h>
#include <iostream>
#include <iomanip>
#include <map>
#include <utility>

using namespace std;

int readcase(FILE* fp);

int main(int argc, char* argv[])
{
    int ncases;
    int i;

    if(argc < 2)
    {
	printf("no input\n");
        return 1;
    }

    // Read file
    char buff[11];
    FILE* fp = fopen(argv[1], "r");
    fgets(buff, 10, fp);
    sscanf(buff, "%d", &ncases);
    for(i=0; i<ncases; i++)
    {
	int result = readcase(fp);
	cout << "Case #"  << (i+1) << ": " << result << endl;
    }
    fclose(fp);

    return 0;
}

int readcase(FILE* fp)
{
    char buff[256];
    int i, j, k, nengine, nquery, t3;
    map<string, int> Engines;
    string t2;

    int querylist[1000];
    int swtable[1000][100];   // large input
    //int swtable[100][10];   // small input

    // Read file
    fgets(buff, 255, fp);
    sscanf(buff, "%d", &nengine);
    for(i=0; i<nengine; i++)
    {
        fgets(buff, 255, fp);
	buff[strlen(buff)-1] = '\0';
	t2 = buff;
	Engines[t2] = i;
    }
    fgets(buff, 255, fp);
    sscanf(buff, "%d", &nquery);
    for(i=0; i<nquery; i++)
    {
        fgets(buff, 255, fp);
	buff[strlen(buff)-1] = '\0';
	t2 = buff;
	t3 = Engines[t2];
	querylist[i] = t3;
	//cout << t3 << endl;
    }

    const int INFINITY = 1001;
    for(i=0; i<nquery; i++)
    {
	for(j=0; j<nengine; j++)
	{
	    if(querylist[i] == j)
		swtable[i][j] = INFINITY;
	    else if(i==0)
	    {
		swtable[i][j] = 0;
	    }
	    else
	    {
		int min = INFINITY, t4;
		for(k=0; k<nengine; k++)
		{
		    if(k == j)
			t4 = swtable[i-1][j];
		    else
			t4 = swtable[i-1][k] + 1;
		    if(t4 < min) min = t4;
		}
		swtable[i][j] = min;
	    }
	    //cout << setw(4) << swtable[i][j] << " ";
	}
	//cout << endl;
    }

    int result = INFINITY;
    for(i=0; i<nengine; i++)
    {
	if(swtable[nquery-1][i] < result)
	    result = swtable[nquery-1][i];
    }
    return result;
}



