#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int b[100000],a[100000];
int n;
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int th=1;th<=cas;th++){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		scanf("%d",a+i);
		for(int i=0;i<n;i++)
		b[i]=a[i];
		sort(a,a+n);
		int x=0;
		for(int i=0;i<n;i++)
		if(a[i]!=b[i])x++;
		printf("Case #%d: %d.000000\n",th,x);
	}
	return 0;
}
