#include <cstdio>
#include <cstring>

char pal[6000][20];
char ln[6000];
bool ex[20][40];

int main() {
	int l,d,n;
	
	scanf(" %d %d %d",&l,&d,&n);
	for (int i=0; i<d; i++) scanf(" %s",pal[i]);
	gets(ln);
	
	for (int i=0; i<n; i++) {
		gets(ln);
		
		memset(ex,0,sizeof(ex));
		
		bool ins=false;
		int tam=strlen(ln), q=0;
		for (int k=0; k<tam; k++) {
			if (ln[k]=='(') ins=true;
			else if (ln[k]==')') {
				ins=false;
				q++;
			}
			else {
				ex[q][ln[k]-'a']=true;
				if (!ins) q++;
			}
		}
		int res=0;
		for (int k=0; k<d; k++) {
			bool deu=true;
			for (int p=0; p<l; p++) 
				if (!ex[p][pal[k][p]-'a']) deu=false;
				
			if (deu) res++;
		}
		
		printf("Case #%d: %d\n",i+1,res);
	}
	
	return 0;
}
