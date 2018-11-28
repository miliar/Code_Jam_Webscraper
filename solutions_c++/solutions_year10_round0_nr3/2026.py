#include <algorithm>
#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int t;
	int i,j,r,k,n;
	long long zysk;       //+
	long long suma_all;   //+
	int nast;             //+
	int ilosc_runda;      //+
	int kontynuowac;      //+
	int pocz_cyklu;       //+
	int dlugosc_cyklu;    //+
	long long zysk_cyklu; //+
	scanf("%d",&t);
	for(i=0;i<t;++i)
	{
		zysk=0;
		suma_all=0;
		scanf("%d%d%d",&r,&k,&n);
		vector<int> g(n);
		for(j=0;j<n;++j)
		{
			scanf("%d",&g[j]);
			suma_all+=g[j];
		}
		if(suma_all>k)
		{
			if(n<r)
			{
				//symuluje n razy
				nast=0;
				for(j=0;j<n;++j)
				{
					ilosc_runda=0;
					kontynuowac=1;
					while(kontynuowac)
					{
						if(ilosc_runda+g[nast]>k)
							kontynuowac=0;
						else
						{
							ilosc_runda+=g[nast];
							nast=(nast+1)%n;
						}
					}
					zysk+=ilosc_runda;
				}
				r=r-n; //UWAGA!!!
				//wyznaczanie cyklu
				pocz_cyklu=nast;
				dlugosc_cyklu=0;
				zysk_cyklu=0;
				do
				{
					++dlugosc_cyklu;
					ilosc_runda=0;
					kontynuowac=1;
					while(kontynuowac)
					{
						if(ilosc_runda+g[nast]>k)
							kontynuowac=0;
						else
						{
							ilosc_runda+=g[nast];
							nast=(nast+1)%n;
						}
					}
					zysk_cyklu+=ilosc_runda;
				}
				while(nast!=pocz_cyklu);
				//liczenie ile cykli sie zmiesci
				zysk+=zysk_cyklu*(int)(r/dlugosc_cyklu);
				r=r%dlugosc_cyklu;
				for(j=0;j<r;++j)
				{
					ilosc_runda=0;
					kontynuowac=1;
					while(kontynuowac)
					{
						if(ilosc_runda+g[nast]>k)
							kontynuowac=0;
						else
						{
							ilosc_runda+=g[nast];
							nast=(nast+1)%n;
						}
					}
					zysk+=ilosc_runda;
				}
				cout << "Case #" << (i+1) << ": " << zysk << "\n";
			}
			else
			{
				nast=0;
				for(j=0;j<r;++j)
				{
					ilosc_runda=0;
					kontynuowac=1;
					while(kontynuowac)
					{
						if(ilosc_runda+g[nast]>k)
							kontynuowac=0;
						else
						{
							ilosc_runda+=g[nast];
							nast=(nast+1)%n;
						}
					}
					zysk+=ilosc_runda;
				}
				cout << "Case #" << (i+1) << ": " << zysk << "\n";
			}
		}
		else
		{
			cout << "Case #" << (i+1) << ": " << suma_all*r << "\n";
		}
	}
}
