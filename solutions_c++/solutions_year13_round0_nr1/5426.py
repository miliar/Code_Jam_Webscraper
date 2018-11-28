#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main () {
	
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin >> T;
    string nono;
    char board[4][4];
    bool notEnd;
    bool XRow[4], ORow[4], XCol[4], OCol[4];
    for (int t=1; t<=T; t++) {
    	notEnd = false;
    	for (int i=0; i< 3; i++) {
    		XRow[i] = ORow[i] = XCol[i] = OCol[i] = true;
    	}
    	for (int j=0; j<4; j++){
    		for (int k=0; k<4; k++) {
    			cin >> board[j][k];
    			if (board[j][k] == '.') {
    				notEnd = true;
    				XRow[j] = ORow[j] = XCol[k] = OCol[k] = false;
    			}else if (board[j][k] == 'X') {
    				ORow[j] = OCol[k] = false;
    			}else if (board[j][k] == 'O') {
    				XRow[j] = XCol[k] = false;
    			}
    		}
    	}
    	bool okk = false;
    	// check col, then row, then diag
    	for (int i = 0; i<4; i++) {
    		if (XRow[i] || XCol[i]) {
    			printf("Case #%d: X won\n", t);
    			okk = true;
    			continue;
    		}
    	}
    	if (okk) continue;
    	for (int i = 0; i<4; i++) {
    		if (ORow[i] || OCol[i]) {
    			printf("Case #%d: O won\n", t);
    			okk = true;
    			continue;
    		}
    	}
    	if (okk) continue;
    	// diag
    	bool XD = true;
    	for (int i=0; i<4; i++){
    		if (board[i][i] == 'X' || board[i][i] == 'T'){}
    		else {
    			XD = false;
    			break;
    		}
    	}
    	if (XD) {
    		printf("Case #%d: X won\n", t);
    		continue;
    	} 
    	XD = true;
    	for (int i=0; i<4; i++){
    		if (board[i][3-i] == 'X' || board[i][3-i] == 'T'){}
    		else {
    			XD = false;
    			break;
    		}
    	}
    	if (XD) {
    		printf("Case #%d: X won\n", t);
    		continue;
    	}
    	XD = true;
    	for (int i=0; i<4; i++){
    		if (board[i][i] == 'O' || board[i][i] == 'T'){}
    		else {
    			XD = false;
    			break;
    		}
    	}
    	if (XD) {
    		printf("Case #%d: O won\n", t);
    		continue;
    	} 
    	XD = true;
    	for (int i=0; i<4; i++){
    		if (board[i][3-i] == 'O' || board[i][3-i] == 'T'){}
    		else {
    			XD = false;
    			break;
    		}
    	}
    	if (XD) {
    		printf("Case #%d: O won\n", t);
    		continue;
    	} 
    	// no one win
    	if (notEnd) {
    		printf("Case #%d: Game has not completed\n", t);
    	}
    	else {
    		printf("Case #%d: Draw\n", t);
    	}
    }
    
    return 0;
}