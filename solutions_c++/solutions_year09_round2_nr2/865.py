#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main ()
{
	int T;

	cin >> T;

	string s;
	for(int j=0;j<T;j++) {
		cin >> s;
	/*	vector<char> v;
		for(int i=0;i<s.size();i++) {
			v.push_back(s.at(i));
		}
		cout << s << " " ;*/
		bool flag = false;
		for(int i=0;i<s.size()-1;i++) {
			if(s.at(i+1) > s.at(i) ) flag = true;
		}
		if(flag) {
			next_permutation(s.begin(),s.end());
		}else {
			if(s.at(s.size()-1)=='0') {
			s.push_back('0');
				reverse(s.begin(),s.end());
				int i=0;
				for(i=0;i<s.size();i++) {
					if(s.at(i) !='0') break;
				}
				char c = s.at(i);
				s.at(i) = s.at(0);
				s.at(0) = c;
							
			}else {
			s.push_back('0');
				next_permutation(s.begin(),s.end());
				char ch = s.at(1);
				s.at(1) = s.at(0);
				s.at(0) = ch;
			}

		}
		
		cout << "Case #" << j+1 << ": " << s << endl;
	}
	return 0;
}
