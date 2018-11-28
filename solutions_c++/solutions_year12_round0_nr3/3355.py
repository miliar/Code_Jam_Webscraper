#include <cstdlib>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <set>

using namespace std;

int shift(int x, int k)
{
	stringstream ss;
	string s;
	ss << x; ss >> s; ss.clear();
	int n = s.size();
	s = s.substr(n-k, k) + s.substr(0, n-k) ;
	ss << s; ss >> x;
	return x;
} 

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		set <string> st;
		int A, B, a, b, p = 0;
		cin >> A >> B;
		a = A;
		while(a/=10) p++; 
	
		for(int a = A; a <= B; a++)	{
			for(int j = 1; j <= p; j++)	{
				b = shift(a, j);
				if(b != a && b >= A && b <= B) {
					int aa, bb;
					if(a < b) aa = a, bb = b;
					else aa = b, bb = a;
					stringstream ss;
					string s;
					ss << aa << '-' << bb;
					ss >> s;
					st.insert(s);
				}
			}
		}
		cout << "Case #" << i+1 << ": " << st.size() << endl;
	}
    return EXIT_SUCCESS;
}
