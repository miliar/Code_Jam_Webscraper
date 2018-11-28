
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Pattern
{
public:
	Pattern( int l, const std::string & p ):
	  L(l), mLetterList(l)
	{
		ParsePattern( p );
	}

	bool Matches( const std::string word ) const
	{
		for (int i=0; i<L; ++i)
		{
			if (mLetterList[i].find(word[i]) == std::string::npos)
				return false;
		}
		return true;
	}
private:

	void ParsePattern( const std::string& p )
	{
		int pos = 0;
		bool open = false;
		for (std::string::const_iterator sit = p.begin(); sit != p.end(); ++sit)
		{
			char lt = *sit;
			if (lt == '('){ open = true; }
			else if (lt == ')') { open = false; ++pos; }
			else { 
				mLetterList[pos].push_back(lt);
				if (!open) ++pos;
			}
		} 
	}
	std::vector< std::string > mLetterList;
	int L;
};

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	char dict[5000][16];
	int L, D, N;
	scanf("%d %d %d", &L, &D, &N);
	for (int i=0; i<D; ++i)
	{
		scanf("%s", &dict[i]);
	}
	for (int i=1; i<=N; ++i)
	{
		std::string parttern;
		cin >> parttern;
		Pattern pt(L, parttern);
		int cnt = 0;
		for (int j=0; j<D; ++j)
		{
			if (pt.Matches(dict[j])) ++cnt;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}
