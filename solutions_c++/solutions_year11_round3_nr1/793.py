#include<iostream>
using namespace std;
int main(){
	int t;
	char map[52][52];
	bool impo;
	cin>>t;
	for(int x=1;x<=t;++x){
		int r,c;
		cin>>r>>c;
		impo = false;
		for(int i=0;i<r;++i){
			cin>>map[i];
		}
		for(int j=0;j<=c;++j)
			map[r][j] = 'x';
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				if(map[i][j]=='#'){
					if(map[i][j+1]=='#'&&map[i+1][j+1]=='#'&&map[i+1][j]=='#'){
						map[i][j]='/';
						map[i][j+1]='\\';
						map[i+1][j]='\\';
						map[i+1][j+1]='/';
					}
					else{
						impo = true;
						goto output;
					}
				}
			}
		
		}
		output:
		printf("Case #%d:\n",x);
		if(impo)
			printf("Impossible\n");
		else
			for(int i=0;i<r;++i)
				printf("%s\n",map[i]);
	}
}
