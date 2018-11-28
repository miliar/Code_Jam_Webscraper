#include <string>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	map<char,char> M;
	string C = "ejp mysljylc kd kxveddknmc re jsicpdrysi" 
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" 
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
		"yeq";

	string P = "our language is impossible to understand"
		"there are twenty six factorial possibilities" 
		"so it is okay if you want to just give up"
		"aoz";

	int L = C.length();
	for (int i = 0; i < L; i++) M[C[i]] = P[i];

#if 0
	set<char> st; st.clear();
	int P_L = P.length();
	for (int i = 0; i < P_L; i++) st.insert(P[i]);
	for (int i = 0; i < 26; i++) {
		if (st.find(char('a'+i)) == st.end()) cout << char('a'+i) << " "<< endl;
	}
#endif


#if 0
	for (int i = 0; i < 26; i++) {
			char ch = ((M.find(char('a'+i)) != M.end()) ? M[char('a'+i)] : char('a'+i));
			cout << char('a'+i) << ":"<< ch << " ";
	}
#endif

	M['z'] = 'q';
#if 1
	string T_S = "";
	getline(cin, T_S);
	int T = atoi(T_S.c_str());;
	for (int t = 0; t < T; t++) {
		string G = "", S = "";
		getline(cin, G);
		int GL = G.length();
		for (int i = 0; i < GL; i++) {
			char ch = ((M.find(G[i]) != M.end()) ? M[G[i]] : G[i]);
			S += ch;
		}
		cout << "Case #" << t+1 << ": " << S << endl;
	}
#endif

	return 0;
}
