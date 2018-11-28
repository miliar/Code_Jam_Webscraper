#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<time.h>
using namespace std;

typedef long long LL;
long long T;
LL N,W,L;
vector<pair<LL,LL> > pos;
vector<pair<LL,LL> > curpos;
vector<LL> R;
bool flag;
void dfs(int cur)
{
	if(flag) return;
	if(cur == N)
	{
		flag = true;
		pos = curpos;
		return ;
	}
	while(true)
	{
		LL x = rand();
		LL y = rand();
		x *= x;
		y *= y;
		x %= W;
		y %= L;
		int i;
		for(i=0;i<curpos.size();++i)
		{
			LL xx = curpos[i].first;
			LL yy = curpos[i].second;

			if((x-xx)*(x-xx)+(y-yy)*(y-yy)<(R[i]+R[cur])*(R[i]+R[cur])) break;
		}
		
		if(i == curpos.size())
		{
			curpos.push_back(make_pair(x,y));
			dfs(cur+1);
			curpos.pop_back();
		}
		if(flag) break;

	}
	if(flag) return;

}
int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	long long t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		
		cout<<"Case #"<<t<<":";
		
		cin>>N>>W>>L;
		flag=false;
		pos.clear();
		R.clear();
		int i;
		for(i=0;i<N;++i)
		{
			int r;
			cin>>r;
			R.push_back(r);
		}
		srand(time(0));
		
		dfs(0);
		for(i=0;i<pos.size();++i)
			cout<<" "<<pos[i].first<<" "<<pos[i].second;

		cout<<endl;
	}

	return 0;
}
