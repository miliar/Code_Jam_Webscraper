#include<iostream>
#include<algorithm>
#include<numeric>
#include<stdlib.h>
#include<stdio.h>
#include<queue>
#include<list>
#include<stack>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<math.h>
#include<limits>
#include<cmath>
#include<string>
#include<fstream>
#include<sstream>
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<complex>
#include<iterator>
using namespace std;

int main(){
	freopen("C:\\Documents and Settings\\zgmcn\\×ÀÃæ\\in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\zgmcn\\×ÀÃæ\\out.txt","w",stdout);
	int t, n, a[41];
	double x[41], y[41], d[41];
	scanf("%d",&t);
	//char s[41];
	for(int r=1; r<=t; r++){
		scanf("%d",&n);
	/*	for(int i=0,j; i<n; i++){
			scanf("%s",s);
			for(j=n-1; j>=0; j--) if( s[j]=='1') break;
			a[i] = j;
		}
		int num = 0;
		for(int i=0,j; i<n; i++){
			for(j=i; j<n; j++) if( a[j]<=i ) break;
			for(int k=j-1; k>=i; k--){ swap( a[k], a[k+1] ); num++; }
		}*/
		for(int i=0; i<n; i++) scanf("%lf%lf%lf",&x[i],&y[i],&d[i]);
		printf("Case #%d: ",r);
		if( n==1 ) printf("%.5f\n",d[0]);
		else if(n==2 ) printf("%.5f\n",max(d[0],d[1]));
		else{
			double s1 = d[2], d1 = sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]));
			s1 = max( s1, (d1+d[0]+d[1])/2 );

			double s2 = d[1], d2 = sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]));
			s2 = max( s2, (d2+d[0]+d[2])/2 );

			double s3 = d[0], d3 = sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]));
			s3 = max( s3, (d3+d[2]+d[1])/2 );
			s1 = min( s1, s2 ); s1 = min( s1, s3 );
			printf("%.5f\n",s1);
		}
		//printf("Case #%d: %d\n",r,num);
	}
	return 0;
}