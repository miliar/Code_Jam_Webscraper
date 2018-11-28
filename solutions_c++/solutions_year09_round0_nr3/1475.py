#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

#define NUM_TYPE	 int
struct Num{NUM_TYPE nVal;string sVal;Num(string str){sVal = str;istringstream stream(sVal);stream >> nVal;}Num(NUM_TYPE n){nVal = n;ostringstream stream(sVal);stream << fixed << n;sVal = stream.str();}};

string a;
string b = "welcome to code jam";

int table[1000][100];
int get(int i, int j){
	if(j >= b.size())return 1;
	if(i >= a.size())return 0;
	if(table[i][j] != -1)return table[i][j];

	int best = 0;
	for(int k = i ; k < a.size() ; k++)
		if(a[k] == b[j])
			best = (best+get(k+1, j+1))%10000;

	return table[i][j] = best;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int tt; scanf("%d ", &tt);
	for(int t = 0 ; t < tt ; t++){
		getline(cin, a);

		memset(table, -1, sizeof table);
		int r = get(0, 0);

		Num n(r);
		string s = n.sVal;
		while(s.size() < 4)
			s = "0"+s;
		cout << "Case #" << t+1 << ": " << s << endl;
	}

	return 0;
}
