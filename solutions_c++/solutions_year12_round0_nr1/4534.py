#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

#define For(I,A,B) for(int I = A; I < B; ++I)

int main(){
	ifstream cin("A-small-attempt4.in");
	ofstream cout ("out.txt");
	int T;
	char s[120];
	cin >> T;
	cin.getline(s,100);
	ifstream dic("dic.txt");
	map<char,char> vok;
	for(char i = 'a'; i <= 'z'; ++i)
		vok[i] = i;
	vok[' '] = ' ';
	char a,b;
	while (dic){
		dic >> a >> b;
		vok[a] = b;
	}
	int t = 1;
	while(T--){
		cin.getline(s,120);
		For(i,0,strlen(s)){
			s[i] = vok[s[i]];
		}
		cout << "Case #" << t++ << ": " << s << endl;
	}
	return 0;
}

