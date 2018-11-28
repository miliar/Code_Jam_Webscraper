#include <iostream>
using namespace std;


int main()
{
	int n, i, j, a[256];
	string s,t;
	
	getline(cin, s);
	getline(cin, t);
	for (i=0; i<256; i++) a[i]=0;
	for (j=0; j<s.length(); j++)
		a[int(s[j])]=int(t[j]);

	cin >> n;
	getline(cin, s);
	
	for (i=0; i<n; i++) {
		getline(cin, s);
		t=s;
		for (j=0; j<s.length(); j++)
			t[j]=a[s[j]];
		cout << "Case #" << i+1 << ": " << t << endl;;
	}	
	return 0;
}
