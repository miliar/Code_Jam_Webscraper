#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int n,m;
int p[20000];

int hash(int i,int j){
	return (i-1)*m+(j-1);
}

int tofind(int a){
	if(p[a] == a) return a;
	return p[a] = tofind(p[a]);
}

void tounion(int a,int b){
	p[tofind(a)] = tofind(b);
}

int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};

int main(){
	int ncas;
	int land[104][104];
	char group[104][104];
	scanf("%d",&ncas);
	for(int cas=1;cas<=ncas;cas++){
		printf("Case #%d:\n",cas);
		
		scanf("%d %d",&n,&m);
		for(int i=0;i<104;i++){
			for(int j=0;j<104;j++){
				land[i][j] = 9999999;
				group[i][j] = 0;
			}
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				scanf("%d",&land[i][j]);
				p[hash(i,j)] = hash(i,j);
			}
		}
		
		bool flag = true;
		while(flag){
			flag = 0;
			for(int i=1;i<=n;i++){
				for(int j=1;j<=m;j++){
					int ii,jj;
					int mini = land[i][j];
					if(land[i-1][j] < mini){
						mini = land[i-1][j];
						ii = i-1;
						jj = j;
					}
					if(land[i][j-1] < mini){
						mini = land[i][j-1];
						ii = i;
						jj = j-1;
					}
					if(land[i][j+1] < mini){
						mini = land[i][j+1];
						ii = i;
						jj = j+1;
					}
					if(land[i+1][j] < mini){
						mini = land[i+1][j];
						ii = i+1;
						jj = j;
					}
					if(mini < land[i][j]){
						if(tofind(hash(ii,jj)) != tofind(hash(i,j))){
							tounion(hash(ii,jj),hash(i,j));
							flag = 1;
						}
					}
				}
			}	
		}

		char gp = 'a';
		map<int,char> mp;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=m;j++){
				if(mp.find(tofind(hash(i,j))) == mp.end()){
					mp[tofind(hash(i,j))] = gp++;
				}
				printf("%c",mp[tofind(hash(i,j))]);
				putchar(j==m?'\n':' ');
			}
		}
	}
	return 0;
}
