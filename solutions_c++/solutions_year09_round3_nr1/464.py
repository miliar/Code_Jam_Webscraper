#include <iostream>
#include <set>
#include <map>

using namespace std;

set<char> exist;
map<char, int> digit;

int main(){
	int T;
	string s;
	int num[100];
   	
	cin >> T >> ws; 

	for (int cnt = 1; cnt <=T; ++cnt){
		exist.clear();
		digit.clear();

		getline(cin, s);
		int m = s.length();

		int n_ch= 0;
		for (int i=0; i<s.length(); ++i){
			if (exist.find(s[i])==exist.end()){
				n_ch++;
				exist.insert(s[i]);
			}
		}

		int base = n_ch;
		if (base==1)
			base =2;
		bool usedzero = 0;
		int next = 2;
		
		num[0] = 1;
		digit[s[0]] = 1;
		for (int i=1; i<m; ++i){
			if (digit.find(s[i])!=digit.end()){
				num[i] = digit[s[i]];
			} else {
				if (!usedzero){
					num[i] = 0;
					digit[s[i]] = 0;
					usedzero = true;
				} else {
					num[i] = next;
					digit[s[i]] = next;
					next++;
				}
			}
		}

/*		cerr<< "The number is" << endl;
		for (int i=0; i<m; ++i){
			cerr << num[i] << endl;
		}	 */

		long long sum = 0;
		long long prd = 1;
		for (int i=m-1; i>=0; i--){
			sum += prd * (long long) num[i];
			prd *= (long long) base;
		}


		cout << "Case #" << cnt << ": " << sum << endl;
	}

	cerr << "Program Terminated Property." << endl;

	return 0;
}
