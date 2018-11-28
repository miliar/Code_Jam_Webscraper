#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int cycle(string str, int k)
{
	if(str[k] == '0')
		return -1;

	int left=0, right=0, mult=1;

	for(int i=0; i < str.size(); ++i){
		if(i < k){
			left = (left * 10) + (str[i]-'0');
			mult *= 10;
		}
		else{
			right = (right * 10) + (str[i]-'0');
		}
	}

	return (right * mult) + left;
}


int main() {

	int T; cin >> T;

	set<int> SET;

	for(int t=0; t < T; ++t){
		int A; cin >> A;
		int B; cin >> B;
		int result = 0;

		for(int n=A; n < B; ++n){
			SET.clear();
			ostringstream os;
			os << n;
			string str = os.str();
			int m;
			for(int k=1; k < str.size(); ++k){
				if((m = cycle(str, k)) != -1 && n < m && m <= B){
					SET.insert(m);	//all m will be distinct 
				}
			}
			result += SET.size();
		}

		cout << "Case #" << t+1 << ": " << result << endl;
	}


	return 0;
}


