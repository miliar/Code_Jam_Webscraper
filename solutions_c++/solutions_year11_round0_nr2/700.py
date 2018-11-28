#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

class Combined {
public:
    void LoadCombined(size_t numCombined) {
        memset(m_comb, 0, sizeof(m_comb));
        for (size_t iComb = 0; iComb < numCombined; ++iComb) {
            string s;
            cin >> s;

            m_comb[s[0]][s[1]] = s[2];
            m_comb[s[1]][s[0]] = s[2];
        }
    };

    void LoadOpposed(size_t numCombined) {
        memset(m_comb, 0, sizeof(m_comb));
        for (size_t iComb = 0; iComb < numCombined; ++iComb) {
            string s;
            cin >> s;

            m_comb[s[0]][s[1]] = 1;
            m_comb[s[1]][s[0]] = 1;
        }
    };

	inline char GetCombined(char a, char b) const {
		return m_comb[a][b];
	}

	inline bool IsOpposed(char a, char b) const {
		return m_comb[a][b] != 0;
	}


private:
    char m_comb[256][256];
};


typedef vector<char> CharVector;

void Process(const Combined& comb, const Combined& opp, const string& invoked, CharVector& res) {
	res.clear();

	for (string::const_iterator pc = invoked.begin(); pc != invoked.end(); ++pc) {
		char c = *pc;
		res.push_back(c);
		while (res.size() >= 2) {
			char combined = comb.GetCombined(res[res.size() - 2], res.back());
			if (!combined)
				break;
			res.pop_back();
			res.pop_back();
			res.push_back(combined);
		}

		char last = res.back();
		for (size_t i = 0; i < res.size(); ++i) {
			if (opp.IsOpposed(res[i], last)) {
				res.clear();
				break;
			}
		}
	}
}

int main() {
    size_t numCases = 0;
    cin >> numCases;

    for (size_t iCase = 0; iCase < numCases; ++iCase) {
        size_t numCombined = 0;
        cin >> numCombined;
        Combined comb;
        comb.LoadCombined(numCombined);

		size_t numOpposed = 0;
        cin >> numOpposed;
		Combined opp;
		opp.LoadOpposed(numOpposed);

		size_t strLen = 0;
		cin >> strLen;

		string invoked;
		if (strLen > 0)
			cin >> invoked;
		
		CharVector res;
		Process(comb, opp, invoked, res);
		cout << "Case #" << (iCase + 1)  << ": [";
		for (size_t i = 0; i < res.size(); ++i) {
			if (i > 0)
				cout << ", ";
			cout << res[i];
		}
		cout << ']' << endl;
	}
}
