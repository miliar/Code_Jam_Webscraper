#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>


	char s[1000];
	char a[6000][100];

int main(){
	freopen("in","rt",stdin);
	freopen("out","wt",stdout);
	int l, n, m;
	scanf("%d%d%d", &l, &n, &m);
	gets(s);
	for (int i=0; i<n; ++i)
		gets(a[i]);
	int k;
	bool p,q;
	int ans;
	for (int i=0; i<m; ++i){
		gets(s);		
		ans=0;
		for (int j=0; j<n; ++j){
			p=true;	
			k=0;
			for (int u=0; u<l; ++u){
				if (s[k]!='('){
					if (s[k]!=a[j][u]) p=false;
					break;				
				}
				else{
					q=false;
					while(s[k]!=')'){
						if (s[k]==a[j][u]) q=true;
						++k;					
					}
					if (!q) p=false;	
				}
				++k;
			}
			if (p) ++ans;
		}
		printf("Case #%d: %d\n", i+1, ans);	
	}
	return 0;
}