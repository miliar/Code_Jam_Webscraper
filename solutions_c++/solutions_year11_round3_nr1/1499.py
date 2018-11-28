#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <stdio.h>
#include <limits.h>
#include <math.h>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

int main (){
	ifstream cin ("A-large.in");
	ofstream cout ("output.txt");
	int T;
	cin >> T;
	cout.precision (8);
	For(t,1,T+1){
		int R,C;
		cin >> R >> C;
		vector <string> a;
		string s;
		For(i,0,R){
			cin >> s;
			a.push_back(s);
		}
		bool isEr = false;
		For(i,0,R-1){
			For (j,0,C-1){
				if (a[i][j] == '#')
					if(a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#'){
						a[i][j] = '/';
						a[i+1][j] = 0x5c;
						a[i][j+1] = 0x5c;
						a[i+1][j+1] = '/';
					}
					else{
						isEr = true;
						break;
					}
			}
			if (isEr) break;
		}
		if (! isEr){
			For(i,0,R)
				For(j,0,C)
				if (a[i][j] == '#'){
					isEr = true;
					break;
				}
		}
		cout << "Case #" << t << ": " << endl;
		if (isEr){
			cout << "Impossible"<<endl;
		}
		else{
			For(i,0,R)
				cout << a[i] << endl;
		}
	}
	return 0;
}