#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int T,k=1,n,cnt,a[1005],b[1005];
	scanf ("%d",&T);
	while (k<=T){
		scanf ("%d",&n);
		for (int i=0;i<n;i++) scanf ("%d%d",&a[i],&b[i]);
		cnt=0;
		for (int i=0;i<n;i++){
			for (int j=i+1;j<n;j++){
				if ((a[i]>a[j]) && (b[i]<b[j])) cnt++;
				else if ((a[i]<a[j]) && (b[i]>b[j])) cnt++;
			}
		}
		printf ("Case #%d: %d\n",k,cnt);
		k++;
	}
	return 0;
}
