#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define INF (1<<30)
#define EPS (1e-7)

vector<string> V,prev,Main;
char in[5005][1000],st[1000];

int main() 
{
	freopen("A-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int L,D,N,i,j,test,len,index,res;
	string stt;


	scanf("%d %d %d",&L,&D,&N);
	for ( i = 0; i < D; i ++)
	{
		scanf("%s",in[i]);
		Main.push_back(in[i]);
	}
	for ( test = 1; test <= N; test ++)
	{
		scanf("%s",st);
		V.clear();
		for ( i = 0; i < Main.size(); i ++)
			V.push_back(Main[i]);
		len = strlen( st );
		for ( i = 0,index = 0; i < len; i ++,index++)
		{
			if ( st[i] == '(' )
			{
				for ( ; i < len && st[i] != ')'; i ++)
				{
					for ( j = 0; j < V.size(); j ++)
					{
						if ( st[i] ==V[j][index]) 
							prev.push_back(V[j]);
					}
				}
			}
			else
			{
				for ( j = 0; j < V.size(); j ++)
				{
					if ( st[i] == V[j][index])
						prev.push_back(V[j]);
				}
			}
			V.clear();
			for ( j = 0; j < prev.size(); j ++)
			{
				stt = prev[j];
				V.push_back(stt);
			}
			prev.clear();
		}

		res = V.size();
		printf("Case #%d: %d\n",test,res);
	}

	return 0;
}
