#include <iostream>
#include <vector>
#include <algorithm>

#define VI vector<int>
#define M 101

using namespace std;

int tests;

int X,Y;
vector<vector<int> > data;
int CNT;

long long res;

void read_test(){
	int R;	
	cin >> R;
	data = vector<vector<int> >(M,vector<int>(M,0));
	CNT = 0;	
	for(int r=0; r < R; r++){
		int x1,y1,x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for(int x = x1; x <= x2; x++)
		for(int y = y1; y <= y2; y++){
			if(!data[x][y])
				CNT++;
			data[x][y] = 1;		
		}
	}
}

void solve_test(){
	res = 0;
	while(CNT){
		res++;
		for(int sum = 2*(M-1); sum >= 2; sum--)
		for(int x = 1; x <= M-1; x++){
			int y = sum-x;
			if (y < 1 || y > M-1)
				continue;
			if (data[x][y] == 1){
				if (data[x][y-1] == 0 && data[x-1][y] == 0){
					data[x][y] = 0;
					CNT--;				
				}			
			} else{
				if (data[x][y-1] == 1 && data[x-1][y] == 1){
					data[x][y] = 1;
					CNT++;				
				}			
			}		
		}	
	}
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	cout << res << endl;
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
