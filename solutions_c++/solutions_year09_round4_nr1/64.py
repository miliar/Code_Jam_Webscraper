
#include <iostream>
#include <cstring>
#include <deque>
#include <vector>
#include <cstdio>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;
#define f first
#define s second

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int n;scanf("%d",&n);
		int v[n];
		for(int i=0;i<n;i++){
			char buf[n+2];scanf("%s",buf);
			v[i]=0;
			for(int k=n-1;k>=0;k--){
				if(buf[k]=='0')v[i]++;
				else break;
			}
		}

		char used[n];memset(used,0,sizeof(used));
		int  ret[n];
		int ans=0;
		for(int i=0;i<n;i++){
			int need=n-i-1;

			for(int k=0;k<n;k++)if(used[k]==0 && need<=v[k]){
				used[k]=1;
				ret[i]=k;

				for(int t=0;t<i;t++)if(k<ret[t])ans++;

				break;
			}
		}

		static int npr=1;
		printf("Case #%d: %d\n",npr++,ans);
	}
}
