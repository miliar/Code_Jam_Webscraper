#include<iostream>
#include<sstream>

using namespace std;

int a[1000];
int b[1000];
void solve(int test, string s){
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));

	string p = "welcome to code jam";
	for (int i = 0; i < s.size(); i++)
		if (s[i] == 'w')
			a[i] = 1;

	for (int k = 1; k < p.size(); k++){
		for (int i = 0; i < s.size(); i++)
			if (s[i] == p[k]){
				int sum = 0;
				for (int j = 0; j < i; j++)
					sum = (sum + a[j]) % 10000;
				b[i] = sum;
			}
		for (int i = 0; i < s.size(); i++)
			a[i] = b[i];
		memset(b, 0, sizeof(b));
	}

	int sum = 0;
	for (int i = 0; i < s.size(); i++)
	 	sum = (sum + a[i]) % 10000;
//	cout << sum << endl;
	stringstream ss;
	ss << sum;
	ss >> s;
	while (s.size() < 4)
		s = '0' + s;
	cout << "Case #" << test + 1 << ": " << s << endl;
}

int main(){
	int test;
	cin >> test;
	string s;
	getline(cin, s);
	for (int i = 0; i < test; i++){
		getline(cin, s);
		solve(i, s);
	}
	return 0;
}