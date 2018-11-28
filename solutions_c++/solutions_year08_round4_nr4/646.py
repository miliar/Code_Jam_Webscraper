#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tt=1; tt<=t; tt++){
		int ans = 2147483647;
		int k;
		char a[11111];
		char b[11111];
		memset(a,0,sizeof(a));
		scanf("%d\n%s\n",&k,a+1);
		vector<int> v;
		for(int i=1; i<=k; i++)
			v.push_back(i);
		do{
			vector<int> vv;
			int plus=0;
			int j=0;
			for(int i=1; i<=strlen(a+1); i++){
				vv.push_back(v[j]+plus);
				j++;
				if(i%k==0){
					plus+=k;
					j=0;
				}
			}
			memset(b,0,sizeof(b));
			for(int i=1; i<=strlen(a+1); i++){
				b[i] = a[vv[i-1]];
			}
			int cnt=0;
			for(int i=2; i<=strlen(a+1); i++){
				if(b[i]!=b[i-1])
					cnt++;
			}
			if(cnt<ans)
				ans=cnt;
		}while(next_permutation(v.begin(),v.end()));
		printf("Case #%d: %d\n",tt,ans+1);
	}
	return 0;
}