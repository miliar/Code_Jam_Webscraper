#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7


#define siz 60
char str[siz][siz];
int R,C;

int ABS( int a ) { return a < 0 ? -a : a ;}
bool isValid(int a, int b){
	if(a>=0 && a<R && b >=0 && b <C) return true;
	return false;
}
bool fill(int r, int c){
	if(str[r][c]=='#'){
		str[r][c]='/';
	}
	else return false;
	c++;
	if(isValid(r,c) && str[r][c]=='#'){
		str[r][c]='\\';
	}
	else return false;
	r++;c--;
	if(isValid(r,c) && str[r][c]=='#'){
		str[r][c]='\\';
	}
	else return false;

	c++;
	if(isValid(r,c) && str[r][c]=='#'){
		str[r][c]='/';
	}
	else return false;

	return true;
}

bool call(){
	int i, j;
	bool res = true;
	for( i =0 ; i < R; i++){
		for( j =0 ; j < C; j++){
			if(str[i][j]=='#'){
				res = fill(i,j);
				if(!res) return false;
			}
		}
	}
	return true;
}
int main()
{
	freopen("lA.in","r",stdin);
	freopen("out.txt","w",stdout);
	int kase,ct = 1;
	int i, j;
	scanf("%d",&kase);
	while(kase--){
		scanf("%d %d",&R, &C);
		for(j = 0 ; j < R; j++){
			scanf("%s",str[j]);
		}
		printf("Case #%d:\n",ct++);
		bool res = call();
		if(!res) printf("Impossible\n");
		else
		for(i = 0 ; i<R; i++){
			printf("%s\n",str[i]);
		}
	}
	return 0;


}