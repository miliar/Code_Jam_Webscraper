#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
template <class T> void checkmin(T &t,T x){if (x < t) t = x;}
template <class T> void checkmax(T &t,T x){if (x > t) t = x;}

string ref = "ynficwlbkuomxsevzpdrjgthaq";
string s;

char get(char c){
//	cout << c;
	for (int i=0;i<26;i++){
		if (ref[i] == c)
			return i + 'a';
//		cout << ref[i] << " " << c << endl;
	}
}

int main(){
	cout << ref.size() << endl;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int Tc;
	cin >> Tc;
	getline(cin,s);
	for (int i=1;i<=Tc;i++){
		printf("Case #%d: ",i);
		getline(cin,s);
//		cout << s << endl;
		for (int i=0;i<s.size();i++)
			if (s[i] == ' '){
				printf(" ");
			} else {
				printf("%c",get(s[i]));
			}
		puts("");
	}
}

