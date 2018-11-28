#include<iostream>
using namespace std;
bool eq(char a1,char a2){
	if(a1=='T' || a2=='T') return 1;
	if(a1==a2)return 1;
	return 0;
}
int main(){
	char a[5][5];
	int t;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
scanf("%d",&t);
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		for(int i=0;i<4;++i)
			scanf("%s",a[i]);
		bool c=0;
		
			if(c)continue;
	if(	a[0][0]!='.'){	c=1;
		for(int i=1;i<4;++i)
			if(!eq(a[i][i],a[i-1][i-1]))
			{
				c=0;
			}
			if(c){
				if(a[0][0]=='O')printf("O won\n");
				else printf("X won\n");
			}}
			if(c) continue;
		if(a[0][3]!='.'){	c=1;
			for(int i=1;i<4;++i)
				if(!eq(a[i][3-i],a[i-1][3-(i-1)]))c=0;
			if(c){
				if(a[0][3]=='O')printf("O won\n");
				else printf("X won\n");
			}}
			if(c) continue;
			for(int i=0;i<4;++i)
			{c=0;
			if(a[i][0]!='.'){	c=1;
				for(int j=1;j<4;++j)
					if(!eq(a[i][j],a[i][j-1]))c=0;
				if(c){
				if(a[i][0]=='O')printf("O won\n");
				else printf("X won\n");break;
				}}if(c)break;}
			if(c) continue;
			for(int i=0;i<4;++i)
			{c=0;
			if(a[0][i]!='.'){	c=1;
				for(int j=1;j<4;++j)
					if(!eq(a[j][i],a[j][i-1]))c=0;
				if(c){
				if(a[0][i]=='O')printf("O won\n");
				else printf("X won\n");break;
				}}if(c)break;}
			if(c) continue;
			c=0;
			for(int i=0;i<4;++i){
			for(int j=0;j<4;++j)
			{
				if(a[i][j]=='.')
				{
					c=1;
					printf("Game has not completed\n");break;
				}
			}if(c)break;;
		}if(c)continue;
			printf("Draw\n");
	}
//	system("pause");
}