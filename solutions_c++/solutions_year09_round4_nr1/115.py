#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int a[50];
int n, x;
char s[50];

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("a.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
 	while (tt<T) {
		scanf("%d\n",&n);
		int ans=0;
		for(int i=1;i<=n;++i) {
			a[i]=0;
			gets(s);
			for(int j=1;j<=n;++j) {
				if (s[j-1]=='1') a[i]=j;
			}
//			cout << a[i] << endl;
		}
		for(int i=1;i<=n;++i) {
			for(int j=i;j<=n;++j)
				if (a[j]<=i) {
					for(int k=j;k>i;--k) 
						a[k]=a[k-1];
					ans+=j-i;
//					cout << i << ' ' << j << endl;
					break;
			}
//			for(int j=1;j<=n;++j)
//				cout << a[j] << ' ';
//			cout << endl;
		}
		printf("Case #%d: %d\n",++tt, ans);
	}
	return 0;
}