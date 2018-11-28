#include <iostream>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
using namespace std;

#define PW2(n) (n)*(n)
#define RPT(var, n) for(int var = 0; var < (n); var++)
#define RVT(var, n) for(int var = (n - 1); var >= 0; var--)
#define PRN(var) cout << #var << "=" << (var) << endl
#define vint vector<int>

string bd[4];

bool w(char plyr){
	
	RPT(x, 4){
		RPT(y, 4){
			if(bd[x][y] != plyr && bd[x][y] != 'T'){
				break;
			}	
			if(y == 3){
				return true;
			}			
		}
	}

	RPT(y, 4){
		RPT(x, 4){
			if(bd[x][y] != plyr && bd[x][y] != 'T'){
				break;
			}	
			if(x == 3){
				return true;
			}			
		}
	}

	RPT(i, 4){
		if(bd[i][i] != plyr && bd[i][i] != 'T'){
			break;
		}
		if(i == 3){
			return true;
		}			
	}	
	
	RPT(i, 4){
		if(bd[i][3-i] != plyr && bd[i][3-i] != 'T'){
			break;
		}		
		if(i == 3){
			return true;
		}		
	}	
	
	return false;
}

int main(){
	int n;
	cin >> n;
	
	RPT(i,n){
		RPT(y, 4){
			cin >> bd[y];
		}
		
		if(w('X')){
			cout << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(w('O')){
			cout << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		
		bool e = true;
		RPT(x, 4){
			RPT(y, 4){
				if(bd[x][y] == '.'){
					e = false;
				}				
			}
		}
		
		if(e){
			cout << "Case #" << i+1 << ": Draw" << endl;
		}else{
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
		}
	}

} 
