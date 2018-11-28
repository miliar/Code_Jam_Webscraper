#include <string.h>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;


void Kevinew(){
#ifndef  ONLINE_JUDGE
	freopen("C:\\TDdownload\\A-large.in","r",stdin);
	freopen("C:\\TDdownload\\A-large.out","w",stdout);
	//freopen("C:\\TDdownload\\A-large.out","w",stdout);
#endif
}





int main(){
	int  i,icase;
	__int64 a[1000],b[1000],ans;
	int ncase,n;

	Kevinew();
	scanf("%d\n",&ncase);
	for(icase=0;icase<ncase;icase++) {
		ans = 0;
		scanf("%d\n",&n);
		for (i=0;i<n;i++)
		{
			scanf("%I64d\n",&a[i]);
		}
		for (i=0;i<n;i++)
		{
			scanf("%I64d\n",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		for (i=0;i<n;i++)
		{
			ans+=a[i]*b[n-i-1];
		}



	
		printf("Case #%d: %I64d\n",icase+1,ans);

	}

	return 0;

}


