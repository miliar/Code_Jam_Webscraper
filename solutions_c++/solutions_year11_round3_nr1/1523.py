#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char map[100][101];
int n,m;
bool fill(int x,int y){
	if(!(y+1<m) || !(x+1<n))
		return false;
	if(map[x][y]!='#' || map[x+1][y]!='#' ||
		map[x][y+1]!='#' || map[x+1][y+1]!='#')
		return false;
	map[x][y]='/';
	map[x+1][y]='\\';
	map[x][y+1]='\\';
	map[x+1][y+1]='/';
	return true;
}
bool check(){
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
			if(map[i][j]=='#'){
				if(!fill(i,j))
					return false;
			}
	return true;
}
int main(){
	int tcase;
	cin>>tcase;
	for(int itcase=1; itcase<=tcase; ++itcase){
		cin>>n>>m;
		for(int i=0;i<n;++i)
			cin>>map[i];
		bool ans=true;
		ans=check();
		printf("Case #%d:\n", itcase);
		if(!ans){
			printf("Impossible\n");
		}else{
			for(int i=0;i<n;++i)
				cout<<map[i]<<endl;
		}
	}
	return 0;
}
