#include <iostream>
#include <cstdio>
using namespace std;


char a[1000]="welcome to code jam";
char b[1000];
int c[1000][1000];

int main() {
	//freopen("c.input","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tn;
	
	scanf("%d ",&tn);
	
	for (int ti=1;ti<=tn;++ti) {
		gets(b);
		int len=strlen(b);
		//cout<<b<<endl;
		//cout<<len<<endl;
		memset(c,0,sizeof(c));
		for (int j=len;j>=0;--j) c[19][j]=1;
		for (int i=18;i>=0;--i)
			for (int j=len-1;j>=0;--j) {
				int count=0;
				for (int k=j;k<len;++k) if (b[k]==a[i]) {
					count+=c[i+1][k+1];
					count%=10000;
				}
				c[i][j]=count;
				//cout<<i<<' '<<j<<' '<<count<<endl;
			}
		//cout<<c[0][0]<<endl;
		printf("Case #%d: %04d\n",ti,c[0][0]);
		
		//break;
	}
			
	return 0;
}

		
			
		
	
	