#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <ios>

using namespace std;

int main(int argc, char* argv[])
{
	int L, D, N;

	cin >> L >> D >> N;

	vector<vector<unsigned long> > words(D);

	for (unsigned i = 0; i < D; ++i) {
        string s;
		cin >> s;
        words[i].resize(L);

        for (unsigned j = 0; j < L; ++j)
            words[i][j] = (1 << (s[j] - 'a'));
    }
	
    for (unsigned i = 0; i < N; ++i) {
        string s;
        cin >> s;

        vector<unsigned long> pattern(L);
        int ind = 0;
        bool inner = false;
        for (unsigned j = 0; j < s.size(); ++j) {
            char c = s[j];
            if (c =='(') inner = true;
            if (c ==')') {
                inner = false;
                ++ind;
            }
            if (c >= 'a' && c <='z') {
                pattern[ind] |= (1 << (c - 'a'));
                if (!inner) ++ind;
            }
        }

        int result = 0;
        for (unsigned j = 0; j < D; ++j) {
            bool match = true;
            for (unsigned k = 0; k < L; ++k)
                if ((pattern[k] & words[j][k]) == 0) {
                    match = false;
                    break;
                }
            if (match) ++result;
        }

        cout << "Case #" << i << ": " << result << endl;
    }

	return 0;
}
