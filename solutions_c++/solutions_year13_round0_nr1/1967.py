// =====================================================================================
//       Filename:  A.cpp
//    Description:  
//        Created:  04/13/2013 08:08:38 AM
//         Author:  BrOkEN@!
// =====================================================================================

#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define FOR(i,a,b) for(typeof((a)) i=(a); i <= (b) ; ++i)       
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)   
#define MAX 101


using namespace std;

typedef pair<int,int> PI;
typedef vector<PI> VI;

char grid[4][4];
bool fullGrid=true;
char state[4][25]={"X won","O won","Draw","Game has not completed"};

bool scan(int x,int y,char c){
	if(x!=-1 && y!=-1){
		grid[x][y]=c;
	}
	
	FOR(l,0,3){
		if(
			(grid[l][0]==c && grid[l][1]==c && grid[l][2]==c && grid[l][3]==c)  ||
			(grid[0][l]==c && grid[1][l]==c && grid[2][l]==c && grid[3][l]==c)
			){
			return true;
		}
	}
	
	if(
		(grid[0][0]==c && grid[1][1]==c && grid[2][2]==c && grid[3][3]==c)  ||
		(grid[0][3]==c && grid[1][2]==c && grid[2][1]==c && grid[3][0]==c)
	){
		return true;
	}

	return false;
	
}

int solve(){
	fullGrid=true;
	int m=-1,n=-1;
	FOR(x,0,3){
		FOR(y,0,3){
			if(fullGrid){
				fullGrid=!(grid[x][y]=='.');
			}
			if(grid[x][y]=='T'){
				m=x;n=y;
			}
		}
	}

	bool xWon = scan(m,n,'X');
	bool oWon = scan(m,n,'O');


	if(!xWon && !oWon){//No Body won
		if(fullGrid){
			return 2;
		}else{
			return 3;
		}
	}else{
		if(xWon){
			return 0;
		}else{
			return 1;
		}
	}

}


int main(){
	int T=0;
	scanf("%d",&T);
	FOR(t,1,T){
		FOR(l,0,3)
			scanf("%s\n",grid[l]);
		printf("Case #%d: %s\n",t,state[solve()]);
	}


	return 0;
}

