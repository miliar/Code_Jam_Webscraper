#include<iostream>
#include<cstring>
using namespace std;

int n;
char st[100];
int c[256],d[100];
bool b[256];
long long ans;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    scanf("%d",&n);
	for ( int z=1;z<=n;z++) {
		scanf("%s",st);
		int l=strlen(st);
		memset(b,1,sizeof(b));
		int tot=0;
		for (int i=0;i<l;i++)
		    if (b[st[i]]) {
				b[st[i]]=false;
				tot++;
			}
		int k=0;
		if (tot == 1) tot++;
		for (int i=0;i<l;i++) {
		    if (b[st[i]]==false) {
				if (k == 0) c[st[i]]=1;
				else if (k == 1) c[st[i]]=0;
				else c[st[i]]=k;
				k++;
				b[st[i]]=true;
			}
			d[i]=c[st[i]];
		}
		ans=0;
		for (int i=0;i<l;i++)
			ans=ans*tot+d[i];
		printf("Case #%d: ",z);
		cout << ans << endl;
	}
}
			

				
