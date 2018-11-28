#include <cstdio>
#include <iostream>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;
int tc = 1;
char isi[999][999];
int T,N,M;

int main() {
	freopen("C.txt","w",stdout);
	freopen("Cin.txt","r",stdin);
	
scanf("%d",&T);
while (T--){
	scanf("%d%d",&N,&M);
	for (int i=0;i<N;i++)
	scanf("%s",isi[i]);
	
	bool wow = 1;
	for (int i=0;i<N;i++)
	for (int j=0;j<M;j++) 
		{
			if (isi[i][j]=='#') {
				if (i+1 < N && j+1<M && isi[i+1][j]=='#' && isi[i+1][j+1]=='#' && isi[i][j+1]=='#') {
						isi[i][j]='/';
						isi[i][j+1]='\\';
						isi[i+1][j+1]='/';
						isi[i+1][j]='\\';
					}
				else wow=0;
				}
			}
	printf("Case #%d:\n",tc++);
	if (wow) {
		for (int i=0;i<N;i++) {
			for (int j=0;j<M;j++) printf("%c",isi[i][j]);
			printf("\n");
		
			}
		}
	else printf("Impossible\n");
	}
}
