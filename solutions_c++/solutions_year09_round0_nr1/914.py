#include<iostream>
#include<cstring>
using namespace std;

char a[5100][20],s[20*30];
bool b[20][30];
int l,n,m;


int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&l,&n,&m);
	for (int i=0;i<n;i++)
		scanf("%s",a[i]);
	for (int i=0;i<m;i++) {
		scanf("%s",s);
		memset(b,0,sizeof(b));
		int k=0;
		for (int j=0;j<l;j++) {
			if (s[k] == '(') {
				k++;
				while (s[k] != ')') {
					b[j][s[k]-'a']=1;
					k++;
				}
				k++;
			} else {
				b[j][s[k]-'a']=1;
				k++;
			}
		}
		int ans=0;
		for (int j=0;j<n;j++) {
			bool bb=true;
			for ( k=0;k<l;k++)
				if (b[k][a[j][k]-'a']==false) {
					bb=false;
					break;
				}
			if (bb) {
				ans++;
			//	printf("%s\n",a[j]);
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}

			

	
