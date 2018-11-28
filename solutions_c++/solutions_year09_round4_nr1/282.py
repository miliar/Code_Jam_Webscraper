#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

int a[100000],b[100000],c[100000],n;
char s[100];
queue<int> q,qq;

int perm2num(int n,int *p){
	int i,j,ret=0,k=1;
	for (i=n-2;i>=0;k*=n-(i--))
		for (j=i+1;j<n;j++)
			if (p[j]<p[i])
				ret+=k;
	return ret;
}

void num2perm(int n,int *p,int t){
	int i,j;
	for (i=n-1;i>=0;i--)
		p[i]=t%(n-i),t/=n-i;
	for (i=n-1;i;i--)
		for (j=i-1;j>=0;j--)
			if (p[j]<=p[i])
				p[i]++;
}

int can(int *a) {
int i;
	for (i=0;i<n;++i) {
		if (i<b[a[i]]) {
			return i;
		}
	}
	return -1;
}


int main() {
int z,zz,i,j,k,t;


	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		
		scanf("%d",&n);
		for (i=0;i<n;++i) {
			scanf("%s",s);
			for (j=n-1;j>=0;--j) {
				if (s[j]=='1') {
					break;
				}
			}
			b[i]=j;
			a[i]=i;
		}
		printf("Case #%d: ",z);
		for (k=0;;) {
			i=can(a);
			if (i<0) {
				break;
			}
			for (j=i+1;j<n;++j) {
				if (b[a[j]]<=i) {
					break;
				}
			}
			for (;;) {
				t=a[j];
				a[j]=a[j-1];
				a[--j]=t;
				++k;
				if (j==i) {
					break;
				}
			}
		}
		printf("%d\n",k);
				



	

	}

	
	return 0;
}