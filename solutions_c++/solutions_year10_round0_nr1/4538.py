#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <ctype.h>


#define MIN(x,y) ((x)<(y))?(x):(y)
#define MAX(x,y) ((x)>(y))?(x):(y)

#define rep(i,b) for(int i = 0; i < (b); i++)
#define fo(i,a,b) for(int i = (a); i < (b); i++)
#define fos(i,a,b) for(int i = (a); i < (int)(b).size(); i++)

#include <sstream>
#include <conio.h>


using namespace std;


void main( int argc, char* argv[] )
{
	vector<bool> res;
	bool l[32];
	bool p[32];
	
	int T;
	FILE* in = fopen("input.txt", "r");
	if(in != NULL)
	{
		fscanf(in, "%d\n", &T);
		char buff[256];

		int N, K;
		fo(i, 0, T)
		{
			fscanf(in, "%d %d\n", &N, &K);
			memset(&l, 0, sizeof(l));
			memset(&p, 0, sizeof(p));
			p[0] = 1;

			fo(j, 0, K)
			{
				l[0] = 1 - l[0];
				fo(k, 1, N)
				{
					if (p[k] == 1)
					{
						l[k] = 1 - l[k];
					}

					if (p[k - 1] == 1 && l[k - 1] == 1)
					{
						p[k] = 1;						
					}
					else
					{
						p[k] = 0;
					}					
				}			
			}

			res.push_back(p[N-1] == 1 && l[N-1] == 1);
		}



		
		fclose(in);
	}

	FILE* o = fopen("output.txt", "w");
	if (o != NULL)
	{
		fos(i, 0, res)
		{
			fprintf(o, "Case #%d: %s\n", i + 1, res[i]? "ON":"OFF");
		}

		fclose(o);
	}

}
