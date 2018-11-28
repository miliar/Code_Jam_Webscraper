#include<stdio.h>
using namespace std;
int t,r,c;
char map[52][52];
bool proses(int a, int b){
	if(r-a < 2 || c-b < 2) return false;
	if(map[a][b] == '#' && map[a][b+1] == '#' && map[a+1][b] == '#' &&
		map[a+1][b+1] == '#')
		{
			map[a][b] = '/';
			map[a+1][b+1] = '/';
			map[a][b+1] = '\\';
			map[a+1][b] = '\\';
			return true;
		}
	return false;
}
int main(){
	scanf("%d",&t);
	for(int I=1; I<=t; ++I){
		scanf("%d%d\n",&r,&c);
		for(int i=0; i<r; ++i)scanf("%s", map[i]);
		
		for(int i=0;i<r; ++i)
			for(int j=0;j<c;++j)
				if(map[i][j] == '#')
				
					if(!proses(i,j)) goto skip;
					
		skip:
		
		bool berhasil = true;
		for(int i=0;i<r;++i)
			for(int j=0;j<c;++j)
				if(map[i][j] == '#'){
					berhasil = false;
					goto skip2;
				}
				
		skip2:
		
		printf("Case #%d:\n",I);
		if(berhasil){
			for(int i=0;i<r;++i)
				printf("%s\n",map[i]);
					
		}
		else
			printf("Impossible\n");
		
	}
	return 0;
}
