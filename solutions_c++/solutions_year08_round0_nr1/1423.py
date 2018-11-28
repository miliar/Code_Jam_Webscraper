#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

int main()
{
    char filename[50] = "A-large.in.txt";
	char outputFilename[50] = "A-large.out.txt";
	int a[1005][102], min[1005];
	char b[102][105], c[1005][105], d[10];

	int count, S, Q;
	int i, j, k;

	ofstream ostrm;
	ostrm.open(outputFilename);

	ifstream istrm(filename);	
	istrm.getline(d, 10);
	count = atoi(d);

	for (i=1; i<=count; i++)
	{
		istrm.getline(d, 10);
		S = atoi(d); 
		for (j=0; j<= S-1; j++)
			istrm.getline(b[j], 105); 
        
		istrm.getline(d, 10);
		Q = atoi(d); 
		if (Q==0)
		{
            cout << "Case #" << i << ": 0"  << endl;
			ostrm << "Case #" << i << ": 0"  << endl;
		    continue;
		}

		for (j=0; j<= Q-1; j++)
			istrm.getline(c[j], 105);

		for(j=0; j<=Q-1; j++)
		{
			min[j] = 100000;
			for(k=0; k<=S-1; k++)
			{
				if(strcmp(c[j], b[k]) == 0)
					a[j][k] = -1;
				else
				{
					if (j==0)
						a[j][k] = 0;
					else
					{
						if(a[j-1][k] == -1)
						    a[j][k] = min[j-1]+1;
						else
							a[j][k] = a[j-1][k];
					}					
				}

				if ((a[j][k] >= 0) && (a[j][k] < min[j]))
					min[j] = a[j][k];
			}
		}
		cout << "Case #" << i << ": " << min[Q-1] << endl;
		ostrm << "Case #" << i << ": " << min[Q-1] << endl;
	} 
	return 0;
}