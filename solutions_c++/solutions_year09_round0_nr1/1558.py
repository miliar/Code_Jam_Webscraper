#include<cstdio>
#define L 10000
#define R 20
using namespace std;

int n,l,d,i,k,ans,t,I=0,j;
bool bt;
char word[L][R],s[L];

int main(){
	scanf("%d%d%d",&l,&d,&n);
	for (i=0;i<d;++i)scanf(" %s",word[i]);
	for (t=1;t<=n;++t){
	    printf("Case #%d: ",++I);
	    scanf(" %s",s);
	    ans=0;
	    for (i=0;i<d;++i){
			k=0;
			bt=1;
	        for (j=0;j<l;++j,++k)
	            if (s[k]=='('){
					bt=0;
					while (s[++k]!=')')
					    if (s[k]==word[i][j]) {
							bt=1;
						}
					if (!bt) break;
				}
				else if (word[i][j]!=s[k]) {bt=0;break;}
			if (bt) ++ans;
		}
		printf("%d\n",ans);
	}
	return 0;
}
