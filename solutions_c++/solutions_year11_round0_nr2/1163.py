#include<iostream>
#include<cstring>
//                       Last Change:  2011-05-07 09:40:17
using namespace std;
bool o[26][26];
int p[26][26];
int ans[1001];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int _,x;cin>>_;
	for(int cas=1;cas<=_;++cas)
	{
		cin>>x;
		memset(p,-1,sizeof(p));
		memset(o,0,sizeof(o));
		for(int i=1;i<=x;++i)
		{
			string tmp;
			cin>>tmp;
			p[tmp[0]-'A'][tmp[1]-'A']=tmp[2]-'A';
			p[tmp[1]-'A'][tmp[0]-'A']=tmp[2]-'A';
		}
		cin>>x;
		for(int i=1;i<=x;++i)
		{
			string tmp;
			cin>>tmp;
			o[tmp[0]-'A'][tmp[1]-'A']=true;
			o[tmp[1]-'A'][tmp[0]-'A']=true;
		}
		cin>>x;
		string tmp;cin>>tmp;
		x=0;
		for(int i=0;i<tmp.size();++i)
		{
			int v=tmp[i]-'A';
			if(x&&p[ans[x]][v]!=-1)
				ans[x]=p[ans[x]][v];
			else
			{
				bool kill=false;
				for(int i=1;i<=x;++i)
					if(o[ans[i]][v])
					{
						x=0;
						kill=true;
						break;
					}
				if(!kill)ans[++x]=v;
			}
		}
		printf("Case #%d: [",cas);
		for(int i=1;i<=x;++i)
		{
			putchar('A'+ans[i]);
			if(i!=x)printf(", ");
		}
		puts("]");
	}
	return 0;
}
