#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); freopen(outfile, "w", stdout);
}


char s[200][200];
int main()
{
    SetInputFile();

	long tc,tcounter,i,j,r,c;
	cin >> tc;
	tcounter = 0;

	while(tcounter++<tc)
	{
		
		cin >> r>>c;
		for(i=0;i<r;i++)
		{
			scanf("%s",s[i]);
		}


		bool m = true;
		for(i=0;i<r && m;i++)
		{
			
			for(j=0;j<c && m;j++)
			{
				bool n = false;
				
				if(s[i][j]=='#')
				{
					if(i+1 < r &&  j+1 && (s[i][j]=='#') && (s[i+1][j]=='#')
						&& (s[i][j+1]=='#') && (s[i+1][j+1]=='#'))
					{	s[i][j]= '//';
						s[i+1][j] = '\\';
						s[i][j+1]= '\\';
						s[i+1][j+1]= '//';
					}
					else n = true;
				}
				if(n) m = false;
			}
		}


		cout<<"Case #"<<tcounter<<":"<<endl;

		if(!m){ cout<<"Impossible"<<endl;
		}
		else
		{
			for(i=0;i<r && m;i++)
			{
					cout  << s[i]<<endl;
			}
		}




	}
	
    return 0;
}
