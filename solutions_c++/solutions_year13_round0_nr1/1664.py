#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;

int main(){
	int t;
	cin>>t;
	//cin.ignore();
	REP(x,t){
		//cout<<x<<" ";
		string board[4];
		REP(i,4){
			cin>>board[i];
			}
		cout<<"Case #"<<x+1<<": ";
		bool over = false;
		//Check rows
		REP(i,4){
			if((board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'O' &&board[i][3] == 'O') ||
			   (board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'O' &&board[i][3] == 'T') ||
			   (board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'T' &&board[i][3] == 'O') ||
			   (board[i][0] == 'O' && board[i][1] == 'T' && board[i][2] == 'O' &&board[i][3] == 'O') ||
			   (board[i][0] == 'T' && board[i][1] == 'O' && board[i][2] == 'O' &&board[i][3] == 'O')){
				cout<<"O won";
				over = true;
				break;
				}
			if((board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X' &&board[i][3] == 'X') ||
			   (board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X' &&board[i][3] == 'T') ||
			   (board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'T' &&board[i][3] == 'X') ||
			   (board[i][0] == 'X' && board[i][1] == 'T' && board[i][2] == 'X' &&board[i][3] == 'X') ||
			   (board[i][0] == 'T' && board[i][1] == 'X' && board[i][2] == 'X' &&board[i][3] == 'X')){
				cout<<"X won";
				over = true;
				break;
				}
			}
		//cout<<"After checking rows";
		if(!over){
			//check columns
			REP(i,4){
				if((board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'O' &&board[3][i] == 'O') ||
				   (board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'O' &&board[3][i] == 'T') ||
				   (board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'T' &&board[3][i] == 'O') ||
				   (board[0][i] == 'O' && board[1][i] == 'T' && board[2][i] == 'O' &&board[3][i] == 'O') ||
				   (board[0][i] == 'T' && board[1][i] == 'O' && board[2][i] == 'O' &&board[3][i] == 'O')){
					cout<<"O won";
					over = true;
					break;
					}
				if((board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'X' &&board[3][i] == 'X') ||
				   (board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'X' &&board[3][i] == 'T') ||
				   (board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'T' &&board[3][i] == 'X') ||
				   (board[0][i] == 'X' && board[1][i] == 'T' && board[2][i] == 'X' &&board[3][i] == 'X') ||
				   (board[0][i] == 'T' && board[1][i] == 'X' && board[2][i] == 'X' &&board[3][i] == 'X')){
					cout<<"X won";
					over = true;
					break;
					}
				}
			}
		//cout<<"After checking columns";
		if(!over){
			//check diagnoals
			if((board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O' &&board[3][3] == 'O') ||
			   (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O' &&board[3][3] == 'T') ||
			   (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'T' &&board[3][3] == 'O') ||
			   (board[0][0] == 'O' && board[1][1] == 'T' && board[2][2] == 'O' &&board[3][3] == 'O') ||
			   (board[0][0] == 'T' && board[1][1] == 'O' && board[2][2] == 'O' &&board[3][3] == 'O')){
				cout<<"O won";
				over = true;
				}
			if(!over && ((board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X' &&board[3][3] == 'X') ||
			   (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X' &&board[3][3] == 'T') ||
			   (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'T' &&board[3][3] == 'X') ||
			   (board[0][0] == 'X' && board[1][1] == 'T' && board[2][2] == 'X' &&board[3][3] == 'X') ||
			   (board[0][0] == 'T' && board[1][1] == 'X' && board[2][2] == 'X' &&board[3][3] == 'X'))){
				cout<<"X won";
				over = true;
				}
			if(!over && ((board[3][0] == 'O' && board[2][1] == 'O' && board[1][2] == 'O' &&board[0][3] == 'O') ||
			   (board[3][0] == 'O' && board[2][1] == 'O' && board[1][2] == 'O' &&board[0][3] == 'T') ||
			   (board[3][0] == 'O' && board[2][1] == 'O' && board[1][2] == 'T' &&board[0][3] == 'O') ||
			   (board[3][0] == 'O' && board[2][1] == 'T' && board[1][2] == 'O' &&board[0][3] == 'O') ||
			   (board[3][0] == 'T' && board[2][1] == 'O' && board[1][2] == 'O' &&board[0][3] == 'O'))){
				cout<<"O won";
				over = true;
				}
			if(!over && ((board[3][0] == 'X' && board[2][1] == 'X' && board[1][2] == 'X' &&board[0][3] == 'X') ||
			   (board[3][0] == 'X' && board[2][1] == 'X' && board[1][2] == 'X' &&board[0][3] == 'T') ||
			   (board[3][0] == 'X' && board[2][1] == 'X' && board[1][2] == 'T' &&board[0][3] == 'X') ||
			   (board[3][0] == 'X' && board[2][1] == 'T' && board[1][2] == 'X' &&board[0][3] == 'X') ||
			   (board[3][0] == 'T' && board[2][1] == 'X' && board[1][2] == 'X' &&board[0][3] == 'X'))){
				cout<<"X won";
				over = true;
				}
			}
		//cout<<"After checking diagnoals";
		if(!over){
			REP(i,4){
				REP(j,4){
					if(board[i][j] == '.'){
						cout<<"Game has not completed";
						over = true;
						break;
						}
					}
				if(over) break;
				}
			if(!over) cout<<"Draw";
			}
		//cout<<"After checking all";
		cout<<endl;
		}
	return 0;
	}
	