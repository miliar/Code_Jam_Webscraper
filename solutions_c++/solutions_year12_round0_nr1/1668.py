#include <iostream>

using namespace std;


char ch[200];
char a[40000];
int len,l,T;
char m[200];
int main()
{
	freopen("a0.in","r",stdin);
	for (int j=0; j<3; j++) {
		gets(ch);
		for (int i=0; i<strlen(ch); i++) 
			if ('a'<=ch[i] && ch[i]<='z') a[len++]=ch[i];
	}
	freopen("a0.out","r",stdin);
	for (int j=0; j<3; j++) {
		gets(ch);
		for (int i=0; i<strlen(ch); i++) 
			if ('a'<=ch[i] && ch[i]<='z') {
				m[a[l++]]=ch[i];
			}
	}
	m['z']='q';
	m['q'] = 'z';
	
	freopen("A-small-attempt1.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d\n",&T);
	for (int ttt=1; ttt<=T; ttt++){
		printf("Case #%d: ",ttt);
		gets(ch);
		for (int i=0; i<strlen(ch); i++)
			if ('a'<=ch[i] && ch[i]<='z') printf("%c",m[ch[i]]);
			else printf("%c",ch[i]);
		printf("\n");
	}
}