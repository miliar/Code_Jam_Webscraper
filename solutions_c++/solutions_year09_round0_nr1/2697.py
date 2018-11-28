#include <stdio.h>
bool letter[26];
char word[5010][20];
int check[5100];
void clear(){
	int i;
	for(i=0;i<26;i++)
		letter[i]=false;
}
int main(){
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("alienSmall.out","wt",stdout);
	int l,c,d,n,i,m,j;
	char x;
	scanf("%d %d %d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s\n",word[i]);
	for(i=0;i<n;i++){
		for(j=0;j<l;j++){
			clear();
				scanf("%c",&x);
				//if(x=='\n' || x==EOF)break;
				if(x=='('){
					while(1){
						scanf("%c",&x);
						if(x==')')break;
						letter[x-'a']=true;
					}
				}else {
					letter[x-'a']=true;
				}
				for(m=0;m<d;m++){
					if(j==0){
						if(letter[word[m][j]-'a'])check[m]=i+1;
					}else if(!letter[word[m][j]-'a'])check[m]=0;
				}
		}
		for(m=0,c=0;m<d;m++)
			if(check[m]==i+1)c++;
		printf("Case #%d: %d\n",i+1,c);
		scanf("%c",&x);
	}
	return 0;
}

