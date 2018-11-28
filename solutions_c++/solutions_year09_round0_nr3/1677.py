#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

char text[600];
char pat[30] = "welcome to code jam";
int ans;

void dfs(int i,int j){
	if( j == 19 ){	ans++;	ans -= ans/10000*10000; return; }
	if( !text[i] )	return;
	if( text[i] != pat[j] )
		dfs(i+1,j);
	else{
		 dfs(i+1,j+1);
		 dfs(i+1,j);
		}
	return ;
}
	
int main()
{
	freopen("wel.out","w",stdout);
	int t,cas = 1;
	scanf("%d\n",&t);
	while( t-- ){
		ans = 0;
		gets(text);
		for(int i = 0; text[i]; i++)
			if( text[i] == 'w' )
				dfs(i+1,1);
		printf("Case #%d: ",cas++);
		if( ans <1000 )	printf("0");
		if( ans < 100 ) printf("0");
		if( ans < 10 ) printf("0");
		printf("%d\n",ans);
	}
	return 0;
}
