#include <iostream>
#include <cstdio>

using namespace std;
int n,m;
int map[1001][1001];
int a[1001][1001];

void work(){
     scanf("%d%d",&n,&m);
     getchar();
     memset(a,0,sizeof a);
     memset(map,0,sizeof map);
     
     for (int i=1;i<=n;i++){
         for (int j=1;j<=m;j++){
             char x=getchar();
             if (x=='#') a[i][j]=1;
             if (x=='.') a[i][j]=0;
         }
         getchar();
     }
     
     for (int i=1;i<n;i++){
         for (int j=1;j<m;j++){
             if (a[i][j]==1 && !map[i][j]){
                if (!map[i][j+1] && !map[i+1][j] && !map[i+1][j+1]){
                   map[i][j]=1;map[i][j+1]=2;map[i+1][j]=3;map[i+1][j+1]=4;
                }
             }
         }
     }
     
     int check=1;
     for (int i=1;i<=n;i++)
         for (int j=1;j<=m;j++)
             if (a[i][j]==1 && !map[i][j]) check=0;
     
     if (check){
        for (int i=1;i<=n;i++){
            for (int j=1;j<=m;j++){
                if (map[i][j]==0) printf(".");
                if (map[i][j]==1) printf("/");
                if (map[i][j]==2) printf("\\");
                if (map[i][j]==3) printf("\\");
                if (map[i][j]==4) printf("/");
            }
            printf("\n");
        }
     }
     else printf("Impossible\n");
                
}

int main(){
	//freopen("A.out","w",stdout);
	int t;
    cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ": "<<endl;
		work();
	}
	//system("pause");
	return 0;
}
/*
Simple Input:
 
*/
