#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
bool check(const string &d, const vector<string> &pattern);

int main(int argc, char ** argv)
{
	int L, D, N;
	ifstream f(argv[1]);
	vector<string> dict;
	vector<string> words;

	f >> L >> D >> N;
	dict.resize(D);
	for(int i=0; i<D; ++i){	f >> dict[i];}
	for(int i=0; i<N; ++i)
	{
		int res = 0;
		string word;
		vector<string> pattern(L);
		f >> word;
		int k=0;
		for(int j=0; j<L; ++j)
		{
			if(word[k]=='(')
			{
				++k;
				for(;word[k]!=')';++k)
				{
					pattern[j] = pattern[j] + word[k];
				}
			}else{
				pattern[j] = pattern[j] + word[k];
			}
			++k;
		}	
	

		for(int j=0; j<D; ++j)
		{
			if(check(dict[j],pattern)){++res;}
		}	
	
		cout << "Case #" << i+1 << ": " << res << endl;
	}


	return 0;
}

bool check(const string &d, const vector<string> &pattern)
{
	//cerr << d << endl;
	for(int i=0; i<d.size(); ++i)
	{
		//cerr << d[i] << " " << pattern[i] << " " << pattern[i].find(d[i]) << endl;
		if(pattern[i].find(d[i]) == string::npos){return false;}
	}
	return true;
}

