#include<cstdio>
#include<iostream>
using namespace std;
string tile[1000];
void work(int x)
{
	int r,c;
	printf("Case #%d:\n",x);
	cin >> r >> c;
	for(int i = 0; i < r; i++)
		cin >> tile[i];
	for(int i =0; i < r-1; i++)
		for(int j = 0; j < c-1; j++){
			if(tile[i][j] == '#'){
				if(tile[i+1][j+1] == '#' && tile[i][j+1] == '#' && tile[i+1][j] == '#'){
					tile[i][j]='/';
					tile[i][j+1] = '\\';
					tile[i+1][j] = '\\';
					tile[i+1][j+1] = '/';
				}
				else{
					printf("Impossible\n");
					return;
				}
			}
		}
	for(int i = 0 ; i < r; i++)
		for(int j = 0; j < c; j++)if(tile[i][j]=='#'){
				printf("Impossible\n");
				return;
			}
	for(int i = 0; i < r; i++){
		for(int j = 0; j < c; j++)
			printf("%c",tile[i][j]);
		printf("\n");
	}
}
int main()
{
        int t;
        scanf("%d",&t);
        for(int i = 1; i <= t; i++)work(i);
}

