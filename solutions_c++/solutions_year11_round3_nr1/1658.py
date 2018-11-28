#include <fstream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <list>
#include <vector>
#include <map>
#include <math.h>
#define ms(a,b) memset(a,b,sizeof(a))
#define fori(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
char p[50][50];
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-small-attempt1.out");
	int T,r,c;
	in>>T;
	fori(i,1,T)
	{
		in>>r>>c;
		fori(g,0,r-1)
			in>>p[g];
		bool t=true;
		int j=0;
		while(j<r && t)
		{
			int h=0;
			while(h<c && t)
			{
				if(p[j][h]=='#')
				{
					if(j+1<r && h+1<c )
					{
						if(p[j][h+1]=='#' && p[j+1][h+1]=='#' && p[j+1][h]=='#')
						{
							p[j][h]='/';
							p[j][h+1]='\\';
							p[j+1][h]='\\';
							p[j+1][h+1]='/';
						}
						else
							t=false;
						
					}
					else
						t=false;
					
				}
				h++;
			}
			j++;
		}
		out<<"Case #"<<i<<": "<<endl;
		if(!t)
			out<<"Impossible"<<endl;
		else
		{
			fori(g,0,r-1)
			{
				fori(h,0,c-1)
					out<<p[g][h];
				out<<endl;
			}
		}
		
	}
	return 0;
}