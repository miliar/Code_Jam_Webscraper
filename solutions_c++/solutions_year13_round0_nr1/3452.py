

#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int getData(char data[4][4]);
int processData(char data[4][4]);

int main() {
        freopen("inputA.in", "r", stdin);
	freopen("outputA", "w", stdout);
	int t; cin>>t;
	char data[4][4];
	string s[4] = {"X won", "O won", "Draw", "Game has not completed"};
	for(int i1 = 1; i1 <= t; ++i1) {
		getData(data);
		int ret = processData(data);
		cout<<"Case #"<<i1<<": "<<s[ret]<<endl;
	}

}

int getData(char data[4][4]) {
    char ch;
    for(int i1 = 0; i1 < 16; ++i1) {
	    do {
		    scanf("%c", &ch);
	    } while(ch == ' ' || ch == '\n');
	    data[i1 / 4][i1 % 4] = ch;
    }
	return 0;
}

int processData(char data[4][4]) {
	//scan row
	//scan column 
	//scan diagonal
	int ret = -1;	
	bool xwon, owon, nonfinish = false; //nonfinish = true; as long as there is .
	for(int i1 = 0; i1 < 4; ++i1) {
		xwon = owon = true;  
		for(int i2 = 0; i2 < 4; ++i2) {
			if(data[i1][i2] == 'X') {
				owon = false;
			} else if(data[i1][i2] == 'O') {
				xwon = false;
			} else if(data[i1][i2] == '.') {
				nonfinish = true; owon = xwon = false;
			}
		}
		if(xwon) return 0;
		else if(owon) return 1;
	}


	for(int i1 = 0; i1 < 4; ++i1) {
		xwon = owon = true;  
		for(int i2 = 0; i2 < 4; ++i2) {
			if(data[i2][i1] == 'X') {
				owon = false;
			} else if(data[i2][i1] == 'O') {
				xwon = false;
			} else if(data[i2][i1] == '.') {
				nonfinish = true; owon = xwon = false;
			}
		}
		if(xwon) return 0;
		else if(owon) return 1;
	}
	
	xwon = owon = true;
	for(int i1 = 0; i1 < 4; i1++){
			if(data[i1][i1] == 'X') {
				owon = false;
			} else if(data[i1][i1] == 'O') {
				xwon = false;
			} else if(data[i1][i1] == '.') {
				nonfinish = true; owon = xwon = false;
			}
		
	}
	if(xwon) return 0;
	else if(owon) return 1;


	xwon = owon = true;
	for(int i1 = 0; i1 < 4; i1++){
			if(data[i1][3 - i1] == 'X') {
				owon = false;
			} else if(data[i1][3 - i1] == 'O') {
				xwon = false;
			} else if(data[i1][3 - i1] == '.') {
				nonfinish = true; owon = xwon = false;
			}
		
	}
	if(xwon) return 0;
	else if(owon) return 1;

	if(nonfinish) return 3;
	else return 2;
}


