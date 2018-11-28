#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

class FastString {
public:
	const static size_t npos = -1;
	FastString() {
		m_len = 0;
	}
	FastString(const char * str, size_t len)
	: m_begin(str), m_len(len)
	{
	}
	FastString(const char * str)
	: m_begin(str), m_len(strlen(str))
	{
	}
	FastString(const string & str)
	: m_begin(str.data()), m_len(str.size())
	{
	}
	FastString(const FastString & str)
	: m_begin(str.data()), m_len(str.size())
	{
	}
	FastString & operator = (const FastString & str) {
		m_begin = str.m_begin;
		m_len = str.m_len;
		return *this;
	}
	vector<FastString> split(char delimiter) const {
		FastString str = *this;
		vector<FastString> result;
		while(true) {
			size_t pos = str.find(delimiter);
			if(pos==npos) {
				result.push_back(str);
				break;
			}
			result.push_back(str.substr(0, pos));
			str = str.substr(pos+1);
		}
		return result;
	}
	FastString substr(size_t pos, size_t n = npos) const {
		if(m_len < pos) {
			return FastString();
		}
		const char * begin = m_begin + pos;
		size_t len = m_len - pos;
		if(n < len) {
			len = n;
		}
		return FastString(begin, len);
	}
	size_t size() const {
		return m_len;
	}
	const char * data() const {
		return m_begin;
	}
	size_t find(char c) const {
		const char * begin = m_begin;
		size_t len = m_len;
		for(size_t i=0; i<len; ++i) {
			if(begin[i]==c) {
				return i;
			}
		}
		return npos;
	}
	int toInt() const {
		char buf[256];
		int len = min(255, (int)m_len);
		memcpy(buf, m_begin, len);
		buf[len] = '\0';
		return atoi(buf);
	}
	const char * begin() const {
		return m_begin;
	}
	const char * end() const {
		return m_begin + m_len;
	}
	char operator[](size_t idx) const {
		return m_begin[idx];
	}
private:
	const char * m_begin;
	size_t m_len;
};

bool func3(char c, const vector<FastString> & D) {
	for(int i=0, s=D.size(); i<s; ++i) {
		const FastString & d = D[i];
		for(int j=0, s2=d.size(); j<s2; ++j) {
			if(d[j]==c) {
				return true;
			}
		}
	}
	return false;
}

int func2(const FastString L, const FastString & d, vector<FastString> D) {
	int cnt = 0;
	for(int i=0, s=L.size(); i<s && 1 < D.size(); ++i) {
		char c = L[i];
		if(func3(c, D)) {
			bool flg = false;
			vector<FastString> D2;
			for(int j=0, s2=D.size(); j<s2; ++j) {
				const FastString & d2 = D[j];
				bool flg2 = false;
				for(int k=0, s3=d.size(); k<s3; ++k) {
					if(d[k]==c) {
						flg = true;
					}
					if(d2[k]!=d[k] && (d2[k]==c || d[k]==c)) {
						flg2 = true;
					}
				}
				if(!flg2) {
					D2.push_back(d2);
				}
			}
			D = D2;
			if(!flg) {
				++cnt;
			}
		}
	}
	return cnt;
}

string func(const string & L, const vector<string> & D) {
	int maxCost = 0;
	int maxI = 0;
	for(int i=0, s=D.size(); i<s; ++i) {
		vector<FastString> wordList;
		for(int j=0; j<s; ++j) {
			if(D[i].size()==D[j].size()) {
				wordList.push_back(D[j]);
			}
		}
		int cost = func2(L, D[i], wordList);
		if(i==0 || maxCost < cost) {
			maxCost = cost;
			maxI = i;
		}
	}
	return D[maxI];
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; ++t) {
		int N, M;
		scanf("%d%d", &N, &M);
		vector<string> D;
		for(int n=0; n<N; ++n) {
			char buf[256];
			scanf("%s", buf);
			D.push_back(buf);
		}
		printf("Case #%d:", t+1);
		for(int m=0; m<M; ++m) {
			char buf[256];
			scanf("%s", buf);
			printf(" %s", func(buf, D).c_str());
		}
		printf("\n");
	}
	return 0;
}
