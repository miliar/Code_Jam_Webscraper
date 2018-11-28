#include <iostream>
using namespace std;


int l, d, n;

char pat[5000][16];
bool trans[15][26];
char msg[26*15+1];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d%d%d",&l,&d,&n);
	
	for(int i=0;i<d;i++)
		scanf("%s",pat[i]);
	
	for(int i=0;i<n;i++){
		memset(trans,0,sizeof trans);
		int cnt=0;
		int j,k;
		scanf("%s",msg);
		
		
		char *p=msg;
		for(j=0;j<l;j++){
			if(*p=='('){
				p++;
				while(*p!=')'){
					trans[j][*p-'a']=true;
					p++;
				}
			}
			else {
				trans[j][*p-'a']=true;
			}
			p++;
		}
		
		for(j=0;j<d;j++){
			for(k=0;k<l;k++)
				if(!trans[k][pat[j][k]-'a'])
					break;
			//printf("k=%d\n",k);
			if(k==l)cnt++;
		}
		
		printf("Case #%d: %d\n",i+1,cnt);
	}
	
	return 0;
}
