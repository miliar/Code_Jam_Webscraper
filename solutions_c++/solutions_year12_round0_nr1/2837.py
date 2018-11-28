#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
using namespace std;

char google[28]="abcdefghijklmnopqrstuvwxyz ";
char engilsh[28]="yhesocvxduiglbkrztnwjpfmaq ";
char buf[105];
char ans[105];

int readline(char *s) {
	int L;
	for(L=0;(s[L]=getchar())!='\n'&&s[L]!=EOF;L++);
	s[L]=0;
	return L;
}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
	int Case,len;
	scanf("%d",&Case);
	int h=1;getchar();
	while(Case--) {
	
		readline(buf);
		len=strlen(buf);
		int k=0;
		for(int i=0;i<len;i++) {
		if(buf[i]>='a'&&buf[i]<='z') {
			for(int j=0;j<26;j++) {
				if(buf[i]==google[j]) {
					ans[k++]=engilsh[j];
				}
			}
			}
		else if(buf[i]==' ') {
		  ans[k++]=' ';
		  }
		}
		ans[k]=0;
		printf("Case #%d: %s\n",h++,ans);
	}
    return 0;
}


