#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <string>
#include <cstring>
#include <ctime>
#include <cmath>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q;
	scanf("%d",&q);
	for(int test=1;test<=q;test++){
		int n,k,b,t;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		int i,j;
		int v[60],x[60],f[60];
		for(i=0;i<n;i++)scanf("%d",&x[i]);
		for(i=0;i<n;i++)scanf("%d",&v[i]);
		for(i=0;i<n;i++){
			if((b-x[i])<=v[i]*t)
				f[i]=1; //dude is fast enough
			else
				f[i]=0; //he's a gonner
		}
		int c[60]={0};
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++)
				c[i]+=1-f[j];
		}
		vector<int> vv;
		for(i=0;i<n;i++)if(f[i]==1)vv.push_back(c[i]);
		sort(vv.begin(),vv.end());
		if(vv.size()<k)
			printf("Case #%d: IMPOSSIBLE\n",test);
		else{
			int ans=0;
			for(i=0;i<k;i++)ans+=vv[i];
			printf("Case #%d: %d\n",test,ans);
		}
	}

	return 0;
}
