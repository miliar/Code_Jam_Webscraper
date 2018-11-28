#include<stdio.h>
#include<math.h>
#include<vector>
#include<string.h>
#include<iostream>
using namespace std;

int a[1010];

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	int cas = 1;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		int ans = 0;
		for(int i = 1; i <= n; i ++)
			scanf("%d",&a[i]);
		for(int i = 1; i <= n ; i ++){
			if(a[i] != i){
				ans ++;
			}
		}
		printf("Case #%d: %d.000000\n",cas++,ans );
	}
	return 0;
}