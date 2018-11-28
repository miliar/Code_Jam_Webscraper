#include <iostream>
#include <string>
#include <fstream>
#include <vector>

#define REP(i,n) for (int i=0; i<n; i++)

using namespace std;

enum WinFlag{
	Draw = 0,
	WinX = 1,
	WinO = 2,
	NotEnded = 3,
};

int main(){
	int testcase=0;	//Nth test
	int X;	//testcase
	ifstream inputfile("A-large.in");
	ofstream outputfile("output.txt");
	
	inputfile >> X;
	
	REP(k,X){
		testcase++;
		cout << "testcase:" << testcase << endl;
		WinFlag flag = NotEnded;
		vector<string> str(4);
		REP(i,4){
			inputfile >> str[i];
		}
		if(flag == NotEnded){	//yoko
			REP(i,4){
				string tmp = str[i];
				cout << "yoko" << tmp << endl;
				if(tmp == "XXXX" ||
					tmp == "XXXT" ||
					tmp == "XXTX" ||
					tmp == "XTXX" ||
					tmp == "TXXX"){
					flag = WinX;
					break;
				}else if(tmp == "OOOO" ||
					tmp == "OOOT" ||
					tmp == "OOTO" ||
					tmp == "OTOO" ||
					tmp == "TOOO"){
					flag = WinO;
					break;
				}
			}
		}
		if(flag == NotEnded){	//tate
			REP(i,4){
				string tmp;
				REP(j,4){
					tmp+=str[j][i];
				}
				cout << "tate" << tmp << endl;
				if(tmp == "XXXX" ||
					tmp == "XXXT" ||
					tmp == "XXTX" ||
					tmp == "XTXX" ||
					tmp == "TXXX"){
					flag = WinX;
					break;
				}else if(tmp == "OOOO" ||
					tmp == "OOOT" ||
					tmp == "OOTO" ||
					tmp == "OTOO" ||
					tmp == "TOOO"){
					flag = WinO;
					break;
				}
			}
		}
		if(flag == NotEnded){	//naname1
			string tmp;
			REP(j,4){
				tmp += str[j][j];
			}
			cout <<  "naname1" << tmp << endl;
			if(tmp == "XXXX" ||
				tmp == "XXXT" ||
				tmp == "XXTX" ||
				tmp == "XTXX" ||
				tmp == "TXXX"){
				flag = WinX;
			}else if(tmp == "OOOO" ||
				tmp == "OOOT" ||
				tmp == "OOTO" ||
				tmp == "OTOO" ||
				tmp == "TOOO"){
				flag = WinO;
			}
		}
		if(flag == NotEnded){	//naname2
			string tmp;
			REP(j,4){
				tmp += str[3-j][j];
			}
			cout <<  "naname2" << tmp << endl;
			if(tmp == "XXXX" ||
				tmp == "XXXT" ||
				tmp == "XXTX" ||
				tmp == "XTXX" ||
				tmp == "TXXX"){
				flag = WinX;
			}else if(tmp == "OOOO" ||
				tmp == "OOOT" ||
				tmp == "OOTO" ||
				tmp == "OTOO" ||
				tmp == "TOOO"){
				flag = WinO;
			}
		}
		if(flag == NotEnded){	//Draw
			if(str[0].find(".") == string::npos &&
				str[1].find(".") == string::npos &&
				str[2].find(".") == string::npos &&
				str[3].find(".") == string::npos
			){
				flag = Draw;
			}
		}
		string result;
		switch(flag){
		case Draw:
			result += "Draw";
			break;
		case WinX:
			result += "X won";
			break;
		case WinO:
			result += "O won";
			break;
		case NotEnded:
			result += "Game has not completed";
			break;
		}
			
		cout << "Case #" << testcase << ": " << result << endl;
		outputfile << "Case #" << testcase << ": " << result << endl;
	}
	
	return 0;
}