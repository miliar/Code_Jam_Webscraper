#include <iostream>
#include <stdio.h>
#include <set>
#include <list>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
typedef long long LL;
#define rep(I,N) for(I = 0; I < N; I++)
string tab[101];
char txt[101][101];
int main()
{
	int l = 0;
	int j = 0;
	int i = 0;
	int Z,N,M;
	cin>>Z;
	rep(i,Z)
	{
		cin>>N>>M;
		rep(j,N)
		{
			cin>>tab[j];
		}
		rep(j,100) rep(l,100) txt[j][l] = '.';
		rep(j,N)
		{
			rep(l,M)
			{

				txt[j][l] = tab[j][l];
				
			}
		
		}
		
		bool bad = 0;
		rep(j,N)
		{
			rep(l,M)
			{
				if(txt[j][l] == '#' && (txt[j][l + 1] == '.' || txt[j + 1][l] == '.' || txt[j + 1][l + 1] == '.'))bad = 1;
				else if(txt[j][l] == '#')
				{
					txt[j][l] = '/';
					txt[j][l + 1] = '\\';
					txt[j + 1][l] = '\\';
					txt[j + 1][l + 1] = '/';
				}
				if(bad == 1) break;
			}
			if(bad == 1) break;
		}
		 cout<<"Case #"<<i + 1<<":"<<endl;
		if(bad) cout<<"Impossible"<<endl;
		else
		{
			rep(j,N)
			{
				rep(l,M)
				{
					cout<<txt[j][l];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}
