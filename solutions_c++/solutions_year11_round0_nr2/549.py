#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char in[200];
		
int ans[200];
int top;

int f[30][30];
int g[30][30];
int main () {
	freopen ("B-large.in","r",stdin);
	freopen ("B-large.out","w",stdout);
	int test,ca;
	cin>>test;
	for (ca = 1;ca<=test;ca++) {
	
		memset (f,-1,sizeof (f));
		memset (g,-1,sizeof (g));
		top = -1;
		int c;
		char str[5];
		cin>>c;
		for (int i=0;i<c;i++) {
			cin>>str;
			f[str[0]-'A'][str[1]-'A'] = str[2]-'A';
			f[str[1]-'A'][str[0]-'A'] = str[2]-'A';			
		}
		cin>>c;
		for (int i=0;i<c;i++) {
			cin>>str;
			g[str[0]-'A'][str[1]-'A'] = -2;
			g[str[1]-'A'][str[0]-'A'] = -2;
		}
		cin>>c;
		cin>>in;
		int len = strlen (in);
		for (int i=0;i<len;i++) {
			ans[++top] = in[i]-'A';
			while (top>0) {
				if (f[ans[top]][ans[top-1]] >= 0) {
					ans[top-1] = f[ans[top]][ans[top-1]];
					top--;
				} else {
					for (int j=0;j<top;j++) {
						if (g[ans[j]][ans[top]] == -2) {
							top = -1;
							break;
						}
					}
					break;
				}
			}
		}
		printf ("Case #%d: [",ca);
		for (int i=0;i<=top;i++) {
			if (i == 0) {
				printf ("%c",ans[i]+'A');
			} else {
				printf (" %c",ans[i]+'A');
			}
			if (top>0 && i!=top) {
				printf (",");
			}
		}
		printf ("]\n");
	}
	return 0;
}
		
