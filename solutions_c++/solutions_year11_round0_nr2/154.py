#include<iostream>
#include<vector>
#include<cstring>
#include<cstdio>
using namespace std;
char to[30][30],tem[1000],stack[1000];
bool oo[30][30];
int main(){
	
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int T,c,d,n,TC=0,i,j;
	scanf("%d",&T);
	while(T--){TC++;
		scanf("%d",&c);
		memset(to,0,sizeof(to));
		memset(oo,0,sizeof(oo));
		while(c--){
			scanf("%s",tem);
			to[tem[0]-'A'][tem[1]-'A']=tem[2];
			to[tem[1]-'A'][tem[0]-'A']=tem[2];
		//	printf("$$%c %c %c\n",tem[0],tem[1],tem[2]);
		}
		scanf("%d",&c);
		while(c--){
			scanf("%s",tem);
			oo[tem[0]-'A'][tem[1]-'A']=1;
			oo[tem[1]-'A'][tem[0]-'A']=1;
		}
		scanf("%d",&c);
		scanf("%s",tem);
		int top=0;
		for(i=0;i<c;i++){
			char temp = tem[i];
			while(top>0 && to[stack[top-1]-'A'][temp - 'A'] !=0){
				temp = to[stack[top-1]-'A'][temp - 'A'];
				top--;
				//printf("##%c %c %c\n",stack[top-1],temp,temp);
			}
			stack[top++]=temp;
			for(j=0;j<top-1;j++)if(oo[stack[top-1]-'A'][stack[j] - 'A']){
				top=0;
				break;
			}
		}
		printf("Case #%d: [",TC);
		if(top>0)printf("%c",stack[0]);
		for(i=1;i<top;i++)printf(", %c",stack[i]);
		printf("]\n");
	}
}
