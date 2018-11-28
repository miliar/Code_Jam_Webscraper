#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <numeric>

using namespace std;
int p,q;
bool pri[10000];
double dis(double x, double y, double z)
{
	return sqrt(x*x+y*y+z*z);
}

int coin(int rel)
{
	int ret=0;
	for(int i=rel;pri[i]!=false && i<p;i++)
	{
		ret++;
	}
	for(int i=rel-2;pri[i]!=false && i>=0;i--)
	{
		ret++;
	}
	return ret;
}

int main()
{
	char filename[500] = "K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Round1A\\Debug\\C";
	char outfile[500];
	char buff[2000];

	//scanf("%s", filename);
	strcpy(outfile, filename);
	strcat(outfile, ".out");
	FILE *ofp=fopen(outfile, "w+");

	int n;
	scanf("%d", &n);
	for(int i=0; i < n; i++)
	{
		vector<int> pos;
		scanf("%d %d", &p,&q);
		/*
		gets(buff);
		string line(buff);
		istringstream iss(line);*/
		for(int j=0;j<q;j++)
		{
			int tmp;
			scanf("%d", &tmp);
			
			//iss >> tmp;
			pos.push_back(tmp);
		}
		int ans=-1;
		do{
			for(int j=0;j<p;j++)
			{
				pri[j]=true;
			}
			int tmp=0;
			for(int j=0;j<q;j++)
			{
				pri[pos[j]-1] = false;
				tmp += coin(pos[j]);
			}
			if(ans == -1)
			{
				ans = tmp;
			}
			else if(ans > tmp)
			{
				ans = tmp;
			}
		}while(next_permutation(pos.begin(),pos.end()));

		fprintf(ofp, "Case #%d: %d\n", i+1, ans);
	}
	return 0;
}