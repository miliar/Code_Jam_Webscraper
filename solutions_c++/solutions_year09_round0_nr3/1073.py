#include<iostream>
#include<string>
using namespace std;
const string msg = "welcome to code jam";
const int L = 19;
int N;
string s;
int d[L+1];
int main()
{
	cin >> N;
	getline(cin, s);
	for(int k=1; k<=N; ++k)
	{
		getline(cin, s);
		d[0] = 1;
		for(int j=1; j<=L; ++j)
			d[j] = 0;
		for(int i=0; i<s.length(); ++i) {
		for(int j=L; j>0; --j)
		if(s[i]==msg[j-1])
		    d[j] = (d[j] + d[j-1]) % 10000;
		}
		cout << "Case #" << k << ": ";
		for(int t=1000; t>0; t/=10)
		    cout << d[L]/t%10;
		cout << endl;
	}
}
