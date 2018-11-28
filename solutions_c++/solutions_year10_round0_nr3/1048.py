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
#include <fstream>
#include <cassert>

using namespace std;

bool flag=false;
int vec(vector<vector<int> > v,vector<int> v1)
{
	flag=false;
	sort(v1.begin(),v1.end());
	vector<vector<int> >::iterator it;
	for (it=v.begin();it!=v.end();it++)
	{
		//cout<<(*it).size()<<endl;
		if(v1.size() != (*it).size())
			continue;
		sort( (*it).begin(),(*it).end() );
		int i;
		for (i=0;i<v1.size();i++)
		{
			if(v1[i] != (*it)[i])
				break;
		}
		if(i == v1.size())
			break;
	}
	if(it != v.end())
		flag=true;
	return it-v.begin();
}

vector< vector<int> > v;
vector<int> v1;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	unsigned long long R,K,N;
	unsigned int g[1000];

	cin>>T;
	int round=1;
	unsigned long long  res;
	while(round<=T)
	{
		cin>>R>>K>>N;
		v.erase(v.begin(),v.end());
		for (int i=0;i<N;i++)
			cin>>g[i];

		int cur=0;
		while (true)
		{
			v1.erase(v1.begin(),v1.end());
			unsigned long long sum=0;
			int kkk=0;
			while (sum+g[cur]<=K && kkk<N)
			{
				kkk++;
				v1.push_back(cur);
				sum+=g[cur];
				cur=(cur+1)%N;
			}
			vec(v,v1);
			if (flag)
			{
				int yidong=vec(v,v1);
				//int cir=v.size()-yidong;

				unsigned long long d[1000]={0};
				unsigned long long d_2[1000]={0};
				int v_k;
				for (v_k=0;v_k<yidong;v_k++)
				{
					for (int v_k2=0;v_k2<v[v_k].size();v_k2++)
					{
						d[v_k]+=g[ v[v_k][v_k2] ]; //´íÎó
					}
				}

				unsigned long long accu=0;
				for (v_k=yidong;v_k<v.size();v_k++)
				{
					for (int v_k2=0;v_k2<v[v_k].size();v_k2++)
					{
						d_2[v_k-yidong]+=g[ v[v_k][v_k2] ];
					}
					accu+=d_2[v_k-yidong];
				}

				res=0;
				for (int i=0;i<R && i<yidong;i++)
				{
					res+=d[i];
				}
				if (yidong<R)
				{
					R-=yidong;
					res += (R/(v.size()-yidong))*accu;
					R=R%(v.size()-yidong);
					for (unsigned long long i=0;i<R;i++)
					{
						res+=d_2[i];
					}
				}
				break;
			}
			else
				v.push_back(v1);
		}
		cout<<"Case #"<<round<<": "<<res<<endl;
		round++;
	}
	return 0;
}