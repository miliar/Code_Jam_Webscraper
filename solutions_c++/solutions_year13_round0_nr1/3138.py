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
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(long i=a; i<b; i++)
#define fm(i,a,b) for(long i=a; i>b; i--)
#define xwon "X won"
#define owon "O won"
#define draw "Draw"
#define incomplete "Game has not completed"

using namespace std;

int t, n, r;  long D; int _case;
vector <long> d,l;
map <char, int> mp; 
string emp;
bool hasResult(int tot){
//	cout << "\t\tchecking with tot=" << tot << endl;
    switch (tot)
	{
		case 4:
		case 8:
			r = 1;
			return true;
			break;
		case 40:
		case 35:
			r = 2;
			return true;
			break;
		default:
			return false;
			break;
	}
}


int main()
{
	string row[4];
	string col[4];
	string diag[2];
	bool gameComplete = false;
	mp['O'] = 1;
	mp['X'] = 10;
	mp['.'] = 0;
	mp['T'] = 5; 
	int tot = 0;
	char c;
	int tr = -1;
    _case=1;		
    cin >> t;
    while(_case<=t)
    {
	tot = 0;
	r = -1;
	gameComplete = true;
	for(int i=0; i<4; i++)
		cin >> row[i];
	// check all rows first
	
	for(int i=0;i<4;i++){
		tot = 0;
		for(int j=0;j<4;j++){
			c = row[i][j] ;
			if(mp[c] == 0){ gameComplete = false;
                     //cout << "changning can be draw for " << c << endl;
            }
            tot = tot + mp[c];	
		}
		if(hasResult(tot)){
			break;
		}
	}
	if(r==-1){
	  for(int i=0; i<4; i++){
		      tot = 0;
                  for(int j=0;j<4;j++){ 
                          c = row[j][i] ;
                          tot = tot + mp[c];
                  }
                 if(hasResult(tot)){
                          break;
                  }
     }
    }
        
	if(r==-1){
		tot = mp[row[0][0]] + mp[row[1][1]]  
			+ mp[row[2][2]] + mp[row[3][3]];
		if(hasResult(tot)){
                           tr = 1;
                   }
	}

	if(r == -1){
		tot = mp[row[0][3]] + mp[row[1][2]]  
                        + mp[row[2][1]] + mp[row[3][0]];
		if(hasResult(tot)){
			tr = 1;
		}
	}
//	cout << "r finally is= " << r << endl;
	cout <<"Case #"<< _case <<": ";
	
        switch(r){   
		case 1:
			cout << owon << endl;
			break;
		case 2:
			cout << xwon << endl;
			break;
		case -1:
			if(gameComplete)
				cout << draw << endl;
			else
				cout << incomplete << endl;	
			break;
		default:
			if(gameComplete)
				cout << draw << endl;
			else
				cout << incomplete << endl;
			break;
	}
	//cin >> emp;
        _case++;
    }
	return 0;
}
