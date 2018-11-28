#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <valarray>

using namespace std;

#define ALL(v) (v).begin(),(v).end()
typedef pair<int,int> pii;

char grid[5][5];

bool check(char s,int pi,int pj,int di,int dj){
	int i;
	int nt=0,ns=0;
	
	for(i=0;i<4;i++){
		if(grid[pi][pj] == s)
			ns++;
		if(grid[pi][pj] == 'T')
			nt++;
			
		pi += di;
		pj += dj;
	}
	if(ns == 4) return true;
	if(ns == 3 && nt == 1) return true;
	return false;
}

int main(){
	int nteste,teste;
	int i,j;
	
	
	
	scanf("%d",&nteste);
	for(teste = 1; teste <= nteste; teste++){
		
		bool comp = true;
		char ch;
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf(" %c",&ch);
				grid[i][j] = ch;
				
				if(ch == '.')
					comp = false;								
			}
		}
		char resp = '?';
		
		for(i=0;i<4;i++){
			if(check('O',i,0,0,1) || check('O',0,i,1,0) ){
				resp = 'O';
				break;
			}
			if(check('X',i,0,0,1) || check('X',0,i,1,0)){
				resp = 'X';
				break;
			}
		}
		if(check('O',0,0,1,1) || check('O',0,3,1,-1))
			resp = 'O';
		else if(check('X',0,0,1,1) || check('X',0,3,1,-1))
			resp = 'X';
			
		printf("Case #%d: ",teste);
		
		if(resp != '?')
			printf("%c won\n",resp);
		else if(comp)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
		
	}	
}
