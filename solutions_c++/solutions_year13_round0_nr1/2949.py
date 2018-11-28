#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <iostream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <iomanip>

#define rep(i,m) for(unsigned long long i = 0;i < (unsigned long long)m ;i++)
#define rep2(i,n,m) for(unsigned long long i = (unsigned long long)n;i < (unsigned long long)m ;i++)
#define ui unsigned int
#define ull  unsigned long long
#define pb  push_back

using namespace std;

string tab[4];

int main() {
	int cases, count; 
	char ref;
	bool flag, X, O;
	cin >> cases;
	rep(casei, cases){
		count = 0;
		X = false;
		O = false;
		rep(i, 4)
			cin >> tab[i];
		rep(i, 4){
			flag = true;
			if(tab[i][0] == 'T')
				ref = tab[i][1];
			else
				ref = tab[i][0];
			rep(j, 4){
				if(tab[i][j] != ref && tab[i][j] != 'T'){
					flag = false;
					break;	
				}
			}
			if(flag && ref != '.'){
				if(ref == 'X'){
					X = true;
				}else{
					O = true;
				}
				break;	
			}
		}
		
		rep(i, 4){
			flag = true;
			if(tab[0][i] == 'T')
				ref = tab[1][i];
			else
				ref = tab[0][i];
			rep(j, 4){
				if(tab[j][i] != ref && tab[j][i] != 'T'){
					flag = false;
					break;
				}
			}
			if(flag && ref != '.'){
				if(ref == 'X'){
					X = true;
				}else{
					O = true;
				}
				break;	
			}
		}
		
		flag = true;
		if(tab[0][0] == 'T')
			ref = tab[1][1];
		else
			ref = tab[0][0];
		rep(j, 4){
			if(tab[j][j] != ref && tab[j][j] != 'T'){
				flag = false;
				break;
			}
		}
		if(flag && ref != '.'){
			if(ref == 'X'){
				X = true;
			}else{
				O = true;
			}
		}
		
		flag = true;
		if(tab[0][3] == 'T')
			ref = tab[1][2];
		else
			ref = tab[0][3];
		rep(j, 4){
			if(tab[j][3 - j] != ref && tab[j][3 - j] != 'T'){
				flag = false;
				break;
			}
		}
		if(flag && ref != '.'){
			if(ref == 'X'){
				X = true;
			}else{
				O = true;
			}
		}
		
		rep(i,4){
			rep(j,4){
				if(tab[i][j] == '.'){
					count++;
				}
			}
		}
		
		if(count == 0){
			if((X && O) || (!X && !O)){
				cout << "Case #"<< (int)casei + 1 <<": Draw"<< endl;
			} else {
				if(X){
					cout << "Case #"<< (int)casei + 1 <<": X won"<< endl;
				}else{
					cout << "Case #"<< (int)casei + 1 <<": O won"<< endl;
				}
			}
		} else {
			if(X && O){
				cout << "Case #"<< (int)casei + 1 <<": Draw"<< endl;
			} else {
				if(!X && !O){
					cout << "Case #"<< (int)casei + 1 <<": Game has not completed"<< endl;
				} else {
					if(X){
						cout << "Case #"<< (int)casei + 1 <<": X won"<< endl;
					}else{
						cout << "Case #"<< (int)casei + 1 <<": O won"<< endl;
					}
				}
			}
		}
    }
    return 0;
}