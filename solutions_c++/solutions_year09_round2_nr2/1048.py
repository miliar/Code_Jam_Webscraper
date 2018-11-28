#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main()
{
	
	int t;
	cin >> t;
	string s;
	string s1, s2;
	int j =1;
	while (j <= t) {
		cin >> s;
		s1 = s;
		sort(s1.begin(), s1.end());
		next_permutation(s.begin(), s.end());
		if (s == s1) {
			sort(s.begin(), s.end());
			s = '0'+s;
			for (int i = 0 ; i < s.size() ; ++i) {
				if (s[i] != '0') {
					swap(s[i], s[0]);
					break;
				}	
			}
		}
		cout <<"Case #"<< j <<": "<< s << endl;
		j++;
	}

	return 0;
}

