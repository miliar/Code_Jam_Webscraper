#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main () {
	string s;
	int i, j, l;
	int t, n, m;
	long long int k;
	vector <int> W;
	vector <int> E;
	vector <int> L;
	vector <int> C;
	vector <int> O;
	vector <int> M;
	vector <int> T;
	vector <int> D;
	vector <int> J;
	vector <int> A;
	vector <int> S;
	vector < vector <int> > letters;
	vector < vector <int> > size;
	vector <int>	aux;

	cin >> n;
	getchar();
	for(i=0; i<=19; i++)
		aux.push_back(0);
	for(t=1; t<=n; t++) {

		// read string
		s.clear();
		getline(cin, s);

		// init
		k = 0;
		letters.clear();
		size.clear();

		// store letters positions
		for(i=0; i<s.size(); i++) {
			if(s[i] == 'w') W.push_back(i);
			else if(s[i] == 'e') E.push_back(i);
			else if(s[i] == 'l') L.push_back(i);
			else if(s[i] == 'c') C.push_back(i);
			else if(s[i] == 'o') O.push_back(i);
			else if(s[i] == 'm') M.push_back(i);
			else if(s[i] == 't') T.push_back(i);
			else if(s[i] == 'd') D.push_back(i);
			else if(s[i] == 'j') J.push_back(i);
			else if(s[i] == 'a') A.push_back(i);
			else if(s[i] == ' ') S.push_back(i);
		}
		letters.push_back(W);
		letters.push_back(E);
		letters.push_back(L);
		letters.push_back(C);
		letters.push_back(O);
		letters.push_back(M);
		letters.push_back(E);
		letters.push_back(S);
		letters.push_back(T);
		letters.push_back(O);
		letters.push_back(S);
		letters.push_back(C);
		letters.push_back(O);
		letters.push_back(D);
		letters.push_back(E);
		letters.push_back(S);
		letters.push_back(J);
		letters.push_back(A);
		letters.push_back(M);

		m = 0;
		if(W.size() > m) m = W.size();
		if(E.size() > m) m = E.size();
		if(L.size() > m) m = L.size();
		if(C.size() > m) m = C.size();
		if(O.size() > m) m = O.size();
		if(M.size() > m) m = M.size();
		if(T.size() > m) m = T.size();
		if(D.size() > m) m = D.size();
		if(J.size() > m) m = J.size();
		if(A.size() > m) m = A.size();
		if(S.size() > m) m = S.size();

		// init
		W.clear();
		E.clear();
		L.clear();
		C.clear();
		O.clear();
		M.clear();
		T.clear();
		D.clear();
		J.clear();
		A.clear();
		S.clear();

		if(m!=0) {
			for(l=0; l<=m; l++)
				size.push_back(aux);
			for(l=0; l<=m; l++)
				size[l][1] = 1;

			for(i=2; i<=19; i++)
				for(l=0; l<letters[19-i].size(); l++)
					for(j=0; j<letters[19-i+1].size(); j++)
						if(letters[19-i][l] < letters[19-i+1][j]) {
							size[l][i] = (size[l][i]+size[j][i-1])%10000;
						}
			for(i=0; i<letters[0].size(); i++) {
				k = (k+size[i][19])%10000;
			}
		}

		// print output
		cout << "Case #" << t << ": ";
		cout.width(4);
		cout << setfill('0') << k << endl;
	}

	return 0;
}