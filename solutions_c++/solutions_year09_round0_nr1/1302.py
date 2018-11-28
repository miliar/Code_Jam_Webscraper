#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	size_t L, D, N;
	cin>>L>>D>>N;
	vector<string> dictionary;
	for(size_t i = 0; i<D; ++i) {
		string s;
		cin>>s;
		dictionary.push_back(s);
	}
	sort(dictionary.begin(), dictionary.end());

	for(size_t nnn = 0; nnn<N; ++nnn) {
		string pattern;
		cin>>pattern;

		// parse pattern
		string::iterator pos = pattern.begin();
		vector<vector<char> > data;
		data.resize(L);
		for(size_t lll = 0; lll<L; ++lll) {
			if(*pos == '(') {
				while(*(++pos) != ')') {
					data[lll].push_back(*pos);
				}
				sort(data[lll].begin(), data[lll].end());
			}
			else
				data[lll].push_back(*pos);
			++pos;
		}

		// Now we are ready to process dictionary
		int count = 0;
		for(size_t ddd = 0; ddd<D; ++ddd) {
			string word = dictionary[ddd];
			bool ok = true;
			for(size_t l = 0; l<L; ++l) {
				bool f = false;
				for(size_t i = 0; i<data[l].size(); ++i)
					if(data[l][i] == word[l]) {
						f = true;
						break;
					}
				if(!f) {
					ok = false;
					break;
				}
			}
			if(ok)
				++count;
		}
		cout<<"Case #"<<nnn+1<<": "<<count<<endl;
	}
}
