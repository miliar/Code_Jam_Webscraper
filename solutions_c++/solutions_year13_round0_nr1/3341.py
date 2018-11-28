#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

#define nMax 110

#define bug puts("Fuck");

int n = 4;
char a[5][5];
int sum=0;

bool win(char ch){
	for(int i=0;i<n;i++){
		int t=0,k=0;
		for(int j=0;j<n;j++) if(a[i][j]==ch)t++;else if(a[i][j]=='T')k++;
		if(t == 4 || (t==3 && k==1)) return true;
		t=0,k=0;
		for(int j=0;j<4;j++) if(a[j][i]==ch) t++;else if(a[j][i]=='T')k++;
		if(t==4 || (t==3 && k==1))return true;
	}
	int t=0,k=0;
	for(int i=0;i<4;i++)if(a[i][i]==ch) t++;else if(a[i][i]=='T') k++;
	if(t==4 || (t==3&&k==1))return true;
	t=0;k=0;
	for(int i=0;i<4;i++)if(a[i][3-i]==ch)t++;else if(a[i][3-i]=='T')k++;
	if(t==4 || (t==3&&k==1)) return true;
	return false;
}

bool over(){
	for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(a[i][j]=='.') return false;
	return true;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cas = 1;
    while(t--){
		for(int i=0;i<n;i++)scanf("%s",a[i]);
		printf("Case #%d: ",cas++);
		if(win('O'))printf("O won\n");
		else if(win('X')) printf("X won\n");
		else if(over()) printf("Draw\n");
		else printf("Game has not completed\n"); 
	}
	return 0;
}
