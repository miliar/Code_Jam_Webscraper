#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int parse(int str[],int a1,int a2,int a3,int a4){
	int sum=str[a1]+str[a2]+str[a3]+str[a4];
	if (sum==3 || sum==4) 
	{
		printf("X won\n");
		return 1;
	}
	else if(sum==-3 || sum==-4)
	{
		printf("O won\n");
		return 1;
	}
	else if (sum>10) return 2;
	else return 3;
}
int main()
{
	freopen("c:\\1.in","r",stdin);
	freopen("c:\\out1.txt","w",stdout);
	
	int T;
	int map[10][4]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15,0,5,10,15,3,6,9,12};
	char c[20];
	int str[16];
	cin>>T;
	int i;
	for(i=1;i<=T;i++)
	{
			cout<<"Case #"<<i<<": ";
			scanf("%s",c);
			scanf("%s",c+4);
			scanf("%s",c+8);
			scanf("%s",c+12);
			int k;
			for (k=0;k<=15;k++){
					if (c[k]=='X') str[k]=1;
					else if (c[k]=='O') str[k]=-1;
					else if (c[k]=='T') str[k]=0;
					else str[k]=20;
			}
			int ans=1;
			for (k=0;k<=9;k++){
					int u=parse(str,map[k][0],map[k][1],map[k][2],map[k][3]);
					if (u==1) break;
					if (u==2) ans=2;
					if (k==9 ){
						if (ans==2){
							printf("Game has not completed\n");
						}
						else {
							printf("Draw\n");
						}
					}
			}	
	}
return 0;
}

