#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<list>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
using namespace std;

typedef vector<int> vi;
typedef vector< vi > vii;
typedef pair<int,int> pi;
typedef map<string,int> msi;
typedef map<int,string> mis;

#define MAX 105
int grid[MAX][MAX];
int temp[MAX][MAX];
queue<int>r;
queue<int>c;
int N;
int test_case;


int Soln(){
	bool flag;
	int count = 0;
	for(;;){
		flag = true;
		for(int i=1; i<=MAX; i++){
			for(int j=1; j<=MAX; j++){
				if( grid[i][j] == 1 ){
					flag = false;
					if(  grid[i-1][j] == 0 && grid[i][j-1] == 0 ) temp[i][j] = 0;
					
				}
				else {
					if(  grid[i-1][j] == 1 && grid[i][j-1] == 1 ){ temp[i][j] = 1;
						flag = false;
					}
				}

				
				
			}
		}
		
		
		for(int z=1; z<=MAX; z++){
			for(int x=1; x<=MAX; x++){
				grid[z][x] = temp[z][x];
			}

			
		}

		
		if ( flag ) return count;

		

		count++;

	}

}
int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w",stdout);
	int x1,x2,y1,y2,i,j,k;
	cin>>test_case;
	for( int caseId=1; caseId <= test_case; caseId ++ ){
		cin>>N;
		memset(grid,0,sizeof(grid)); 
		memset(temp,0,sizeof(temp));

		for(i=0; i<N; i++){
			cin>>x1>>y1>>x2>>y2;
			if( x1 > x2 ) swap(x1,x2);
			if( y1 > y2 ) swap(y1,y2);

			for( j=y1; j<=y2; j++){
				for(k=x1; k<=x2; k++){
					grid[j][k] = 1;
				

				}
			}
		}


		for(int z=1; z<=MAX; z++){
			for(int x=1; x<=MAX; x++){
				temp[z][x] = grid[z][x];
			}
		
		}	
		
		int ans = Soln();
		printf("Case #%d: %d\n",caseId,ans);


	}

	return 0;
}