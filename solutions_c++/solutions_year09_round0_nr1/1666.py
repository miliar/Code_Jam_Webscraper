#include<iostream>
#define MAX 50001
using namespace std;
bool have[16][27];
char word[MAX][20];
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	int l,d,n;
	int i,j,k,count;
	bool brace;
	char w;
	scanf("%d%d%d",&l,&d,&n);
	while(getchar()!='\n');
	for(i=0;i<d;i++)gets(word[i]);
	for(i=0;i<n;i++){
		memset(have,0,sizeof(have));
		j=-1;brace=false;
		while(true){
			if(!brace&&j==l-1)break;
			scanf("%c",&w);
			if(w=='('){j++;brace=true;}
			else if(w==')')brace=false;
			else if(w>='a'&&w<='z'){
				if(!brace)j++;
				have[j][w-'a']=true;
			}
		}
		while(getchar()!='\n');
		for(j=0,count=0;j<d;j++){
			for(k=0;k<l;k++){
				if(!have[k][word[j][k]-'a'])break;
			}
			if(k==l)count++;
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}