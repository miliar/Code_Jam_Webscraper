//
// a.cpp -- A
//
// Siwakorn Sriakaokul - ping128
// Written on Saturday, 13 April 2013.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>

using namespace std;

char in[5][5];
int cx[] = {-1, -1, -1, 0};
int cy[] = {-1, 0, 1, 1, 1};

void solve(){
	
	int n;
	cin >> n;
	for(int i = 1; i <= 4; i++ )
		scanf("%s", in[i] + 1);

	char player[] = {'X', 'O'};
	for(int p = 0; p < 2; p++ ){
		for(int i = 1; i <= 4; i++ ){
			for(int j = 1; j <= 4; j++ ){
				for(int d = 0; d <= 4; d++ ){
					int cnt = 0;
					for(int x = 0; ; x++ ){
						int ii = i + cx[d] * x;
						int jj = j + cy[d] * x;
						if(ii > 0 && jj > 0 && ii <= 4 && jj <= 4 && (in[ii][jj] == player[p] || in[ii][jj] == 'T')){
							cnt++;
						} else break;
					}
					if(cnt == 4){
						cout << player[p] << " won" << endl;
						return ;
					}

				}
			}
		}
	}

	for(int i = 1; i <= 4; i++ ){
		for(int j = 1; j <= 4; j++ ){
			if(in[i][j] == '.'){
				cout << "Game has not completed" << endl;
				return ;
			}
		}
	}
	cout << "Draw" << endl;
}


int main()
{
	int test;
	cin >> test;
	for(int tt = 0; tt < test; tt++ ){
		printf("Case #%d: ", tt + 1);
		solve();
	}
	return 0;
}
