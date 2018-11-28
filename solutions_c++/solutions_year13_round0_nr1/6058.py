#include <iostream>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

#define FOR(x,s,n) for(typeof(s) x=s;x<n;x++)
#define REP(x,n) for(typeof(n) x=0;x<n;x++)

int main()
{
	int N;
	cin >> N;
	REP(testcase,N) {
		char x[16];
		int tpos=-1;
		bool draw=true;
		REP(i,16){
			char v;
			cin >> v;
			v = toupper(v);
			if(v=='T') {
				tpos = i;
			} else if(v=='.') {
				draw = false;
			}
			x[i] = v;
		}


		bool won_o=false;
        bool won_x=false;
				
		char ch='O';
		//check if O won
		if(tpos>0)
			x[tpos]=ch;

		REP(c,4) {
			bool e=true;
			REP(r,4) {
				e&=x[(c*4)+r]==ch;
			}
			if(e) {
				won_o=true;
				goto next;
			}

		}
		REP(c,4) {
			bool e=true;
			REP(r,4) {
				e&=x[c+(r*4)]==ch;
			}
			if(e) {
				won_o=true;
				goto next;
			}

		}
		if(x[0]==ch &&
				x[5]==ch && 
				x[10] == ch &&
				x[15] == ch) {
			won_o=true;
			goto next;
		}
		if(x[3]==ch &&
				x[6]==ch && 
				x[9] == ch &&
				x[12] == ch) {
			won_o=true;
			goto next;
		}
		

		ch='X';
		//check if X won
		if(tpos>0)
			x[tpos]=ch;

		REP(c,4) {
			bool e=true;
			REP(r,4) {
				e&=x[(c*4)+r]==ch;
			}
			if(e) {
				won_x=true;
				goto next;
			}

		}
		REP(c,4) {
			bool e=true;
			REP(r,4) {
				e&=x[c+(r*4)]==ch;
			}
			if(e) {
				won_x=true;
				goto next;
			}

		}
		if(x[0]==ch &&
				x[5]==ch && 
				x[10] == ch &&
				x[15] == ch) {
			won_x=true;
			goto next;
		}
		if(x[3]==ch &&
				x[6]==ch && 
				x[9] == ch &&
				x[12] == ch) {
			won_x=true;
			goto next;
		}
		


next:
		if(won_o) {
		cout << "Case #" << testcase+1 << ": O won" << endl;
		} else if(won_x) {
		cout << "Case #" << testcase+1 << ": X won" << endl;
		} else {
			if(draw) {
				cout << "Case #" << testcase+1 << ": Draw" << endl;
			} else {
				cout << "Case #" << testcase+1 << ": Game has not completed" << endl;
			}
		}

	}
	return 0;
}
