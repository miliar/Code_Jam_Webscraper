#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1100];
bool cmp(int a,int b){
	return a>b
;}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int casenum = 1;casenum<=t;casenum++){
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		for(int i = 0;i<n;i++)scanf("%d",&a[i]);
		sort(a,a+n);
		int j = n-1;
		int ans = 0;
		int c = 0;
		printf("Case #%d: ",casenum);
		for(int j = n-1;j>=0;j--){
			if(a[j]>=29){
				ans++;
				continue;
			}
			if(a[j]<=1){
				if(a[j]==1 && p<=1)ans++;
				if(a[j]==0 && p==0)ans++;
				continue;
			}
			if(c<s){
				if(a[j]%3){
					if(a[j]/3+1>=p)ans++;
					else {
						if(a[j]%3==2 && p<=a[j]/3+2){
							ans++;
							c++;
						}
					}
				}
				else {
					if(a[j]/3>=p)ans++;
					else {
						if(a[j]/3+1>=p)ans++,c++;
					}
				}
			}else {
				if(a[j]%3){
					if(a[j]/3+1>=p)ans++;
				}else {
					if(a[j]/3>=p)ans++;
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
