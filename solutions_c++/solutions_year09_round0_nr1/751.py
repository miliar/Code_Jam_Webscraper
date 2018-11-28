#include<iostream>
#include<algorithm>
using namespace std;

int L,d,n;
int sum[16];
char ch[5001][16],ch2[16][27];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d",&L,&d,&n);
	int i,num=0;
	for(i=0;i<d;i++)
		scanf("%s",ch[i]);

	for(i=0;i<n;i++) {
		memset(sum,0,sizeof(sum));
		char b[500];
		scanf("%s",b);
		int j=0,k=0,k2=0,l=strlen(b);
		for(j=0;j<l;) {
			if(b[j]=='(') {
				k2=0;
				int j2;
				for(j2=j+1;;) {
					if(b[j2]==')') {
						j=j2+1;
						sum[k]=k2;
						k++;
						break;
					}
					else {
						ch2[k][k2]=b[j2];
						j2++;
						k2++;
					}
				}
			}
			else {
				ch2[k][0]=b[j];
				j++;
				sum[k]=1;
				k++;
			}
		}
		int ans=0;
		for(j=0;j<d;j++) {
			int j2;
			bool yes=true;
			for(j2=0;j2<L;j2++) {	
				char c=ch[j][j2];
				int j3;
				bool ok=false;
				for(j3=0;j3<sum[j2];j3++)
					if(c==ch2[j2][j3]) {
						ok=true;
						break;
					}
				if(!ok) {
					yes=false;
					break;
				}
			}
			if(yes)
				ans++;
		}
		printf("Case #%d: %d\n",++num,ans);
	}
	return 0;
}




				




