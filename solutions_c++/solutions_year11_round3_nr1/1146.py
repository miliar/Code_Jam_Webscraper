
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back
#define LL long long
#define LD long double

bool calc(string ip[], int r, int c)
{
	for(int j=0;j<r;j++)
	{
			int i =0;
		while(i<c)
		{
			if(ip[j][i]=='.')
			{
				i++;
				continue;
			}
			if(i+1<c && ip[j][i+1]=='#')
			{
				i+=2;
				continue;
			}
			return false;
		}
	}

	for(int j=0;j<c;j++)
	{
			int i =0;
		while(i<r)
		{
			if(ip[i][j]=='.')
			{
				i++;
				continue;
			}
			if(i+1<r && ip[i+1][j]=='#')
			{
				i+=2;
				continue;
			}
			return false;
		}
	}

	//char rep = '/';
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(ip[i][j]=='#')
			{
				ip[i][j] = '/';
				ip[i][j+1]='\\';
				ip[i+1][j] ='\\';
				ip[i+1][j+1]='/';
			}
		}
		//rep= rep=='\\'?'/':'\\';
	}

	return true;
}

int main()
{
	ifstream in("A-large.in");

	FILE* out = fopen("A-out-LARGE.out", "w");
	int t,r,c;
	in>>t;

	for(int i=1;i<=t;i++)
	{
		in>>r>>c;
		string ip[50];
		for(int j=0;j<r;j++)
			in>>ip[j];

		fprintf(out, "Case #%d:\n",i);
		if(!calc(ip,r, c))
		{
			fprintf(out, "Impossible\n");
		}
		else
		{
			for(int j=0;j<r;j++)
				fprintf(out, "%s\n", ip[j].c_str());
		}
	}
	return 0;
}