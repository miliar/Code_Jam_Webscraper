/* MUKESH GUPTA */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
#define INF 1000000
typedef long long int LL;
#define FF(i,m,n)    for(int i=m;i<n;i++)
#define F(i,n)    FF(i,0,n)
typedef vector<int> vi;
typedef vector<vi> vvi;


vector<double> sOne;
int main()
{
	int T;
	cin>>T;
	int Kase=1;
	while(T--)
	{
		int N,Sum=0;
		cin>>N;
		vi S(N);
		FF(i,0,N)
		{
			cin>>S[i];
			Sum+=S[i];
		}
		vvi p(N,vi(Sum));
		map<pair<int,int>,vector<int>> mp;

		FF(i,0,Sum)
			p[0][i]=0;
		p[0][S[0]]=1;

		mp[make_pair(0,S[0])].push_back(S[0]);
		bool found=false;
		vector<int> set1;
		vector<int> set2;
		FF(i,1,N)
		{
			FF(j,0,Sum)
			{
				if(p[i-1][j]==1)
				{
					p[i][j]=1;
					
					vector<int> temp1 =mp[make_pair(i-1,j)];
					mp[make_pair(i,j)].insert(mp[make_pair(i,j)].begin(),temp1.begin(),temp1.end());
				}
				if(j-S[i]>=0)
				{
					if(p[i-1][j-S[i]]==1 && p[i-1][j]==1)
					{
					 set1=mp[make_pair(i-1,j)];
					 set2=mp[make_pair(i,j-S[i])];
					set2.push_back(S[i]);
					found=true;
					break;
					}
					if(p[i-1][j-S[i]]==1)
					{
						p[i][j]=1;
						vector<int> temp =mp[make_pair(i-1,j-S[i])];
						mp[make_pair(i,j)].insert(mp[make_pair(i,j)].begin(),temp.begin(),temp.end());
					mp[make_pair(i,j)].push_back(S[i]);
					}
					
				}
			}
			if(found==true)break;
		}
		vector<int>::iterator iter;
		cout<<"Case #"<<Kase++<<":\n";
		for(iter=set1.begin();iter!=set1.end();iter++)
			cout<<(*iter)<<" ";
		cout<<"\n";
		for(iter=set2.begin();iter!=set2.end();iter++)
			cout<<(*iter)<<" ";
		cout<<"\n";

	}
}