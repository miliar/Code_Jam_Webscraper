#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

const char c[20]="welcome to code jam";

char a[1000];
int d[1000][20];

int main() {
	int n;
	cin>>n;
	gets(a);
	for(int ii=0;ii<n;ii++) {
		gets(a);
		int m=strlen(a);
		//for(int i=0;i<m;i++) if (a[i]>='A' && a[i]<='Z') a[i]=a[i]-'A'+'a';
		memset(d,0,sizeof d);
		for(int i=0;i<m;i++) if (a[i]==c[0]) d[i][0]=1;
		int ans;
		for(int k=1;k<19;k++) {
			ans=0;
			for(int i=k;i<m;i++) if (a[i]==c[k]) {
				for(int j=0;j<i;j++) d[i][k]+=d[j][k-1];
				d[i][k]%=10000;
				ans+=d[i][k];
			}
			ans%=10000;
		}
		cout<<"Case #"<<ii+1<<": "<<ans/1000<<ans/100%10<<ans/10%10<<ans%10<<endl;
	}
	return 0;
}
