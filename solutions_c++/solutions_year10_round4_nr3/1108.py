#include<cstdio>
#include<map>
#include<vector>
#include<sstream>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)
#define FORZ(i,t) for(int i = 0;i < t;++i)
#define PB push_back

typedef long long LL;


#define MAX 102

int arr1[MAX][MAX],arr[MAX][MAX];

bool allzero() {
	FOR(i,0,MAX)
		FOR(j,0,MAX)
		if(arr[i][j])
			return false;
return true;
}

void next_state(){
		
	arr1[0][0] = 0;
	FOR(i,0,101)
		FOR(j,0,101){
			if(arr[i][j]){
				if(i == 0 && j > 0 && arr[i][j-1] == 0) 
					arr1[i][j] = 0;					
				else if(j == 0 && i > 0 && arr[i-1][j] == 0)
					arr1[i][j] = 0;
				else if(i > 0 && j > 0 && arr[i-1][j] == 0 && arr[i][j-1] == 0){
					arr1[i][j] = 0;
		//		printf("\n%d %d\n",i,j);
				}
				
			}
			else{
				if(i > 0 && j > 0)
					if(arr[i-1][j] == 1 && arr[i][j-1] == 1)
					arr1[i][j] = 1;
			}
		}
}

int main(){
	int test = GI;
	
	FOR(nt,1,test+1){
		int R = GI;
		memset(arr,0,sizeof arr);
		memset(arr1,0,sizeof arr);
		FOR(i,0,R) {
			int x1 = GI-1,y1 = GI-1,x2 = GI-1,y2 = GI-1;

			FOR(x,x1,x2+1)
				FOR(y,y1,y2+1)
				arr[y][x] = 1;
		}
		int k = 0;
		memcpy(arr1,arr,sizeof arr);
		while(!allzero()){
		/*	printf("\n============================================\n");
			FOR(i,0,10){
				printf("\n");
				FOR(j,0,10)
			printf("%d ",arr[i][j]);
			}
		*/
			next_state();
			memcpy(arr,arr1,sizeof arr);
			++k;
		}
		printf("Case #%d: %d\n",nt,k);
	}

	return 0;
}
