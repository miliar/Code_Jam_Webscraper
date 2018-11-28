#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>
#include<queue>
#include <cstdlib>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define dforsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647
#define MAXL 9223372036854775807
#define salida(a,re) cout<<"Case #"<<a+1<<": "<<re<<endl
int d[1500];
bool usado[1500];
int main()
{	
	int pp;
	cin>>pp;
//	cout<<pp;
	forn(cc,pp)
	{
        long long re=0;       
		int n = 0;		
		cin>>n;
	//	cout<<n;
		forn(i,n)
		{
			d[i] = -1;
			usado[i] = false;
			string auxs;
			cin>>auxs;
			forn(j,n)
			{



				if (auxs[j] != '0')
				   d[i] = j;				
				
				
			}		
		//	cout<<" "<<d[i]<<" "<<endl;;
		}	
		forn(i,n)
		{
			int cont = 0;
			forn(j,n)
			{
				if (d[j] <= i && !usado[j])
				{
                    usado[j] = true;
					re+=cont;
					j = n;
				}
				else 
				{
                    if (!usado[j]) 
					   cont++;
                }
			}
		}
		
		
        salida(cc,re);      
	}
	return 0;
		
}
