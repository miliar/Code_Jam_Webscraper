/*
ID: amir.ho1
LANG: C++
TASK: test
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

int n;

long long max(long long x,long long y){return x>y?x:y;}
int a[100001];
int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);	
	int ti,tc,l,h,i,j;

	scanf("%d",&tc);
	for (ti=1;ti<=tc;ti++){
		scanf("%d %d %d",&n,&l,&h);
		for (i=0;i<n;i++){
			scanf("%d",&a[i]);
			//mx=max(mx,a[i]);
		}
		/*qsort(
		f=1;
		r=lcm(a[0],a[1]);*/
		int r=-1;
		for (i=l;i<=h;i++){
			for (j=0;j<n;j++)
				if (a[j]%i!=0 && i%a[j]!=0)
					break;
			if (j==n){
				r=i;
				break;
			}
		}
		printf("Case #%d: ",ti);
		if (r==-1)
			printf("NO\n");
		else
			printf("%d\n",r);
	}
	return 0;
}