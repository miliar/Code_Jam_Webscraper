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
int ma[1500][25];
vector<int> d[150];
bool usa[150];
int pila[150][150];
int cf[150];
int n=0;;
int cont;
int re;
void r(int ii)
{
  //  cout<<ii<<endl; 
	if (ii == n || cont >= re)
	{
		if (cont < re)		
			re = cont;
        
   }
   else
   {
    int i = 0;
	while(i == 0 || cf[i-1] != 0)
	{
		bool entro = false;
		forn(j,cf[i])
		{
			if (!esta(pila[i][j],d[ii]))
			{
				entro = true;
				j = cf[i];
			}
		}
		if (!entro)
		{
			if (cf[i] == 0)
				cont++;
			pila[i][cf[i]++] = ii;
			r(ii+1);
            cf[i]--;
			if (cf[i] == 0)
				cont--;
			
		}
		i++;
	}
}
}

int main()
{	
	int pp;
	cin>>pp;
	//cout<<pp;
	forn(cc,pp)
	{
           int m ; 
		cin>>n>>m;
	//	cout<<n <<" "<< m;
		forn(i,n)
		{
			d[i].clear();
			cf[i] = 0;
			usa[i] = false;
			forn(j,m)
			{
				cin>>ma[i][j];
	//			cout<<ma[i][j]<< " ";
			}			
	//		cout<<endl;
		}
        forn(i,n)
		{
			forn(j,n){
				bool entro = false;
				forn(k,m)
				{
					if (ma[i][k] == ma[j][k])
						entro = true;
					if (k != 0)
					{
						if (ma[i][k-1] < ma[j][k-1] && ma[i][k] > ma[j][k])
						{
							entro = true;													
						}
						if (ma[i][k-1] > ma[j][k-1] && ma[i][k] < ma[j][k])
						{
							entro = true;													
						}
					}
				}
				if (!entro)
				{
					d[i].pb(j);
				}			
			}
		//	cout<<i<<endl;
		}
		int cont = 0;
		re=MAX;  
		r(0);
		
        salida(cc,re);      
	}
//	cout<<"ss";
	return 0;
		
}
