#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
int main()
{
freopen("out.txt","w",stdout);
freopen("in.txt","r",stdin);
int t;
long a[10001];
scanf("%d",&t);
long long n,l,h,tmp;

for(int z=1; z<=t; z++){
memset(a, 0, 10001);
scanf("%lld %lld %lld",&n,&l,&h);
	for(long long i=0; i<n; i++){
		scanf("%ld ",&a[i]);		
	}
bool f;
tmp=0;
for(long long i=l; i<=h; i++){
	f=false;
	for(long long j=0; j<n; j++)
		if(i%a[j]==0||a[j]%i==0) f=true; 
			else {
					f=false;
					break;
				}
	if (f) {
				tmp=i;
				break;
			}
	}	
if (!f) printf("Case #%d: NO\n",z);
	else
	printf("Case #%d: %lld \n",z,tmp);

}

return 0;}
