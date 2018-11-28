#include <stdio.h>
#include <string.h>
#define maxn 110
int p,q,ans;
int n;
int pos[maxn];
int a[maxn],an,t1[maxn];
int b[maxn],bn,t2[maxn];
int tn;
int main(){
	int i,j,k;
	int casen=0;
	for (scanf("%d",&tn);tn>0;tn--){
		scanf("%d",&n);
		an=bn=0;
		for (k=0;k<n;k++){
			char s[10];
			scanf("%s %d",s,pos+k);
			if (s[0]=='O'){
				t1[an]=k;
				a[an++]=pos[k];
			}else{
				t2[bn]=k;
				b[bn++]=pos[k];
			}
		}
		j=k=0;
		p=q=1;
		ans=0;
		int dt=0;
		while (j<an || k<bn){
			ans++;
			int flag=0;
			if (j<an){
				if (p!=a[j]){
					if (p<a[j]) p++;else p--;
				}else{
					if (t1[j]==dt){
						j++;
						flag=1;
					}
				}
			}
			if (k<bn){
				if (q!=b[k]){
					if (q<b[k]) q++;else q--;
				}else{
					if (t2[k]==dt){
						k++;
						flag=1;
					}
				}
			}
			dt+=flag;
		}
		printf("Case #%d: %d\n",++casen,ans);
	}
	return 0;
}
