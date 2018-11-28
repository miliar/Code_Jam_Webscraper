#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

string S[5005];
vector <string> W;
int L,D,N;

int main()
{
	freopen("d://A-large.in","r",stdin);
	freopen("d://1.txt","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;i++)
		cin>>S[i];
	for(int i=1;i<=N;i++)
	{
		int res=0;
		string t,s="";
		cin>>t;
		//cout<<t<<endl;
		t+=')';
		bool b=false;
		W.clear();
		for(int j=0;j<t.size();j++)
		{
			if(t[j]=='(')
			{
				s="";
				b=true;
			}
			else if(t[j]==')')
			{
				b=false;
				if(s!="")
				{
					sort(s.begin(),s.end());
					W.push_back(s);
				}
				s="";
			}
			else
			{
				s+=t[j];
				if(!b) { W.push_back(s); s=""; }
			}
		}
		for(int j=0;j<D;j++)
		{
			string p=S[j];
			bool ok=true;
			for(int k=0;k<L;k++)
			{
				bool f=false;
				for(int l=0;l<W[k].size()&&!f;l++)
				{
					if(W[k][l]==S[j][k])
						f=true;
				}
				if(!f) { ok=false; break; }
			}
			if(ok) res++;
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}