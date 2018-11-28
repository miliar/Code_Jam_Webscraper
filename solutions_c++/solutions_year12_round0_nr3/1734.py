#include <algorithm>
#include <sstream>
#include <iostream>
#include <map>
#include <cstring>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

#define rep(i,n) for(int i = 0;i<n;i++)
#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

using std::cerr;
using std::cout;
using std::endl;
using std::string;
using std::vector;
char mapping[30];


int A,B;

string rotate(string s,int n){
	reverse(s.begin(),s.begin() + n);
	reverse(s.begin() + n,s.end());
	reverse(s.begin(),s.end());
	return s;
}

int main() {
	//string a = "ABCDE";
	//cout << rotate(a,0);

	stringstream ss;
	string s;
	char c[20];
	int T;
	cin >> T;
	rep(cnt,T){
		cin >> A >> B;
		int ans = 0;
		set<pair<int,int> > pairs;
		for(int n = A;n<B;n++){
			ss.clear();
			ss.str("");
			ss << n;
			s = ss.str();
			for(int i = 1;i<s.length();i++){
				string sed;
				sed = rotate(s,i);
				ss.clear();
				ss.str("");
				ss << sed;
				int p;
				ss >> p;
				if(n < p && p <= B){
					if(!pairs.count(make_pair(n,p))){
						ans++;
						pairs.insert(make_pair(n,p));
					}
					else{
						//cout << "dup" << n << " " << p << endl;
					}
				}
			}
		}
		cout << "Case #" << cnt+1 << ": " << ans << endl;
	}
    return 0;
}

