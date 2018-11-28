#include<cstdio>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
using namespace std;
int main()
{
	freopen("a.in","r",stdin) ;
	freopen("aout.txt","w",stdout) ;
	int T=0;
	scanf("%d",&T);
	for(int cs=1;cs<=T;++cs)
	{
		int N=0;
		scanf("%d",&N);
		char nn[10];
		itoa(N,nn,10);
		string n(nn);
		bool ok=next_permutation(n.begin(),n.end());
		int res=0;
		if(!ok)
		{
			while(n[0]=='0')
				next_permutation(n.begin(),n.end());
			n.insert(1,"0");
		}
		res=atoi(n.c_str());
		printf("Case #%d: %d\n",cs,res) ;
	}	
	return 0;
}