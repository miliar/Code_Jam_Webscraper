#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
using namespace std;
int T, Case = 0;

string cycle(string n) {
    int sz = n.size();
    if(sz == 1) return n;
    return n[sz-1] + n.substr(0, sz-1);
}

int toInt(string s) {
    stringstream ss;
    ss << s;
    int n;
    ss >> n;
    return n;
}

string toStr(int n) {
    stringstream ss;
    ss << n;
    string s;
    ss >> s;
    return s;
}

int main() {

	cin >> T;
	while(T--) {
        ++Case;

        int A, B, Ans = 0;;
        cin >> A >> B; 

        for(int n = A; n <= B; ++n) {
            string nn = toStr(n);
            string n1 = nn;
            while((n1 = cycle(n1)) != nn) {
                int n1i = toInt(n1);
                if(A <= n1i && n1i <= B) ++ Ans;
            }
        }

        Ans >>= 1;

        cout << "Case #" << Case << ": " 
             << Ans << endl;
	}
	return 0;
}
