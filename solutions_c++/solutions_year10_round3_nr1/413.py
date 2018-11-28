//BISMILLAHIRRAHMANIRRAHIM


#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int a[1009],b[1009];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,I,i,j,k,n,m,q;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n;
		for(i=0;i<n;i++) cin>>a[i]>>b[i];
		q=0;
		for(i=0;i<n;i++) for(j=i+1;j<n;j++) {
			if(!((a[i]<a[j] && b[i]<b[j]) || (a[i]>a[j] && b[i]>b[j]))) q++;
		}
		printf("Case #%d: %d\n",I,q);
	}
	return 0;
}
