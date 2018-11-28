
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)

class Magicka
{
	public:
		void ReadData()
		{
			char tab;
			rep(i,255)
			{
				rep(k,255)
				{
					m_combiners[i][k]=' ';
					m_Destroyers[i][k]=0;
				}
			}
			m_Inlist.clear();
			m_Outlist.clear();
			int t; 
			char a,b,c;
			scanf("%d", &t);
			scanf("%c", &tab);
			rep (m,t)
				{
					scanf("%c", &a);
					scanf("%c", &b);
					scanf("%c", &c);
					m_combiners[a][b]=c;
					m_combiners[b][a]=c;
			}
			
			scanf("%d", &t);
			scanf("%c", &tab);
			rep (m,t)
				{
					scanf("%c", &a);
					scanf("%c", &b);
					m_Destroyers[a][b]=1;
					m_Destroyers[b][a]=1;
			}
			scanf("%d", &t);
			scanf("%c", &tab);
			rep (m,t)
			{
				scanf("%c", &a);
				m_Inlist.push_back(a);
			}
			





		};
			void Solve()
				{
					ReadData();
					list<char>::iterator initer;
					initer=m_Inlist.begin();
					list<char>::iterator outiter;
					list<char>::reverse_iterator routiter;
					
					
					while (initer!=m_Inlist.end())
					{
						char last=0;
						if (!m_Outlist.empty())
							last=m_Outlist.back();
						if (m_combiners[last][*initer]!=' ')
						{
							m_Outlist.pop_back();

							m_Outlist.push_back(m_combiners[last][*initer]);
							
						}
						else 
						{
							bool foundDest=false;
							outiter=m_Outlist.begin();
							while (outiter!=m_Outlist.end())
							{
								if (m_Destroyers[*outiter][*initer]==1)
									foundDest=true;
								outiter++;
							}
							if (foundDest)
								m_Outlist.clear();
							else
								m_Outlist.push_back(*initer);

						}
						initer++;
					}
					
					printf("[");
					outiter=m_Outlist.begin();
					while (outiter!=m_Outlist.end())
					{
						printf("%c",*outiter);
						outiter++;			
						if (outiter!=m_Outlist.end())
							printf(", ");
					}
					printf("]");

			};
	
	char m_combiners[255][255];
	int m_Destroyers[255][255];
	list<char> m_Inlist;
	list<char> m_Outlist;


};

int main(int argc, char ** argv) {
   int t;
   Magicka majika;
   char c;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 //  storecredit1.GetData();
	   
	    majika.Solve();

       printf("\n");
   }
   return 0;
}