#include<cstring>
#include<cstdio>
#include<iostream>
#include<string>
#define INF 0xffffff
using namespace std;

int map[6][6];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;char s[10];bool ok=true,ok1=true;
	scanf("%d",&t);getchar();
	for(int cas=1;cas<=t;++cas){
		printf("Case #%d: ",cas);ok1=true;
		for(int i=1;i<=4;++i){
			scanf("%s",s);
			for(int j=0;j<4;++j){
				if(s[j]=='.') ok1=false,map[i][j+1]=0;
				else if(s[j]=='T') map[i][j+1]=3;
				else if(s[j]=='X') map[i][j+1]=1;
				else map[i][j+1]=2;
			}
		}
		int res=0,ans=0;
		for(int i=1;i<=4;++i){
			res=map[i][1];ok=true;
			for(int j=2;j<=4;++j)
				if(res==3) res=map[i][j];
				else if(map[i][j]!=res && map[i][j]!=3){
					ok=false;
					break;
				}
			if(map[i][1]!=0 && ok){ans=res;break;}
			res=map[1][i];ok=true;
			for(int j=2;j<=4;++j)
				if(res==3) res=map[j][i];
				else if(map[j][i]!=res && map[j][i]!=3){
					ok=false;
					break;
				}
			if(map[1][i]!=0 && ok){ans=res;break;}
		}
		res=map[1][1];ok=true;
		for(int i=2;i<=4;++i)
			if(res==3) res=map[i][i];
			else if(map[i][i]!=res && map[i][i]!=3){
				ok=false;
				break;
			}
		if(map[1][1]!=0 && ok) ans=res;
		res=map[1][4];ok=true;
		for(int i=2;i<=4;++i)
			if(res==3) res=map[i][5-i];
			else if(map[i][5-i]!=res && map[i][5-i]!=3){
				ok=false;
				break;
			}
		if(map[1][4]!=0 && ok) ans=res;
		if(ans==0 && ok1) printf("Draw\n");
		else if(ans==0 && !ok1) printf("Game has not completed\n");
		else if(ans==1) printf("X won\n");
		else printf("O won\n");
	}
	return 0;
}
