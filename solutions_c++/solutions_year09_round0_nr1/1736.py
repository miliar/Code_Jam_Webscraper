#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <fstream>

using namespace std;
typedef vector< set<char> > TestCase;
ifstream myin("A-large.in");
ofstream myout("1.out");

int main()
{
	int L, D, N;
	vector<string> words;
	myin >> L >> D >> N;
	for(int i=0; i<D; ++i)
	{
		string word;
		myin >> word;
		words.push_back(word);
	}

	for(int i=0; i<N; ++i)
	{
		string tmp;
		TestCase acase(L);
		bool inKH = false;
		myin >> tmp;
		for(int j=0, k=0; j<tmp.size(); ++j)
		{
			if(tmp[j] == '(')
			{
				inKH = true;
				continue;
			}

			if(tmp[j] == ')')
			{
				inKH = false;
				++k;
				continue;
			}

			acase[k].insert(tmp[j]);
			if(!inKH)
				++k;
		}

		int res=0;
		for(int j=0; j<D; ++j)
		{
			bool pass = true;
			for(int k=0; k<L; ++k)
			{
				if(acase[k].count(words[j][k]) == 0)
				{
					pass = false;
					break;
				}
			}
			if(pass)
				++res;
		}

		myout << "Case #" << i+1 << ": " << res << endl;
	}
	
	return 0;
}