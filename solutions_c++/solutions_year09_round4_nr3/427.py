#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <iostream>

using namespace std;

int n, K;
vector <long long> data[100];
int dynamic[1<<16];
bool cross[100][100], cCheck[1<<16];

bool isCross(int, int);
int getDynamic(int);

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		cin>>n>>K;
		for(int i=0;i<n;i++) data[i].resize(K);
		for(int i=0;i<n;i++) for(int j=0;j<K;j++) cin>>data[i][j];

		memset(cross, 0, sizeof(cross));
		for(int i=0;i<n;i++) 
		{
			for(int j=0;j<n;j++) if(isCross(i, j)) cross[i][j]=true;
		}

		memset(cCheck, 0, sizeof(cCheck));

		for(int i=0;i<(1<<n);i++)
		{
			vector <int> list;
			for(int j=0;j<n;j++) if(i & (1<<j)) list.push_back(j);
			bool flag=true;
			for(int j=0;j<list.size();j++) for(int k=j+1;k<list.size();k++) if(cross[list[j]][list[k]]) { flag=false; break; }
			if(!flag) cCheck[i]=true;
		}

		memset(dynamic, -1, sizeof(dynamic));
	
		cout<<"Case #"<<caseN<<": "<<getDynamic((1<<n)-1)<<endl;
	}

	return 0;
}

int getDynamic(int stat)
{
	int &ret=dynamic[stat];
	if(ret!=-1) return ret;

	if(stat==0) ret=0;
	else
	{
		ret=n;
		vector <int> list;
		for(int i=0;i<n;i++) if(stat & (1<<i)) list.push_back(i);
		int lim=list.size();

		for(int i=1;i<(1<<lim);i++)
		{
			int newStat=0;
			for(int j=0;j<lim;j++) if(i & (1<<j)) newStat^=(1<<list[j]);
			if(!cCheck[newStat])
			{
				newStat = (stat ^ newStat);
				ret=min(ret, getDynamic(newStat)+1);
			}
		}
	}

	return ret;
}

bool isCross(int a, int b)
{
	for(int i=0;i<K-1;i++)
	{
		if(data[a][i]==data[b][i] || data[a][i+1]==data[b][i+1]) return true;
		if((data[a][i]-data[b][i]) * (data[a][i+1]-data[b][i+1])<0) return true;
	}

	return false;
}

