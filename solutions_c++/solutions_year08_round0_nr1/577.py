#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
int DP[1024][1024];
map<string,int>kk;
string str;
int temp[1024];
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("ans1.out","w",stdout);
	int test;
	int Case = 0;
	scanf("%d",&test);
	while(test--){
		Case++;
		kk.clear();
		int n , len = 0;
		int i ,j ,k;
		scanf("%d",&n);
		getchar();
		for(i = 0 ; i < n ; i++){
			getline(cin , str);
			kk[str] = len++;
		}
		int m ;
		scanf("%d",&m);
		getchar();
		for(i = 0 ; i < m ; i++){
			getline(cin,str);
			temp[i] = kk[str];
		}
		for(i = 0 ; i < 1024 ; i++){
			for(j = 0 ; j < 1024 ; j++){
				DP[i][j] = 1000000;
			}
		}
		for(i = 0 ; i < m ; i++){
			if(i == 0){
				for(j = 0; j < n ; j++){
					if(temp[i] == j)
						continue;
					DP[i][j] = 0;
				}
			}
			else{
				for(j = 0 ; j < n ;j++){
					if(temp[i] == j){
						continue;
					}
					for(k = 0 ; k < n ; k++){
						if(k == j){
						
							DP[i][j] = min(DP[i-1][k] , DP[i][j]);
						}
						else{
						
							DP[i][j] = min(DP[i-1][k] + 1 , DP[i][j]);
						}
					}
				}
			}
		}	
	/*	for(i = 0 ; i < m ; i++){
			for(j = 0 ; j < n ; j++){
				printf("%d ",DP[i][j]);
			}
			printf("\n");
		}*/
		int Max = 100000000;
		for(i = 0 ; i < n ; i++){
			if(Max > DP[m-1][i] ){
				Max = DP[m-1][i];
			}
		}
		printf("Case #%d: %d\n" , Case , Max);
	}
	return 0;
}