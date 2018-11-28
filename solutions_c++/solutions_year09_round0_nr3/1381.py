// メモ化再帰のDPで解けるけど，時間的に無理な件

#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std;

/*
string line = "wewwellllcomqqqqqqqqqqqqqqqqq e";
string word = "welcome";
string target = "welcom";
*/
string line;
string word = "welcome to code jam";

vector<vector<int> > memo;
map<char, vector<int> > hash;

int recursive(int w, int l);
#define HASH_NOT_EXIST(i)  (hash.find(word[i]) == hash.end())

int main()
{
	string file = "C-large";
	ifstream ifs((file + ".in").c_str());
	ofstream ofs((file + ".out").c_str());

	int N;
	getline(ifs, line);
	N = atoi(line.c_str());
	for(int n=0; n<N; n++)
	{
		getline(ifs, line);
		cout << n << endl; // " " << line << endl;
		hash.clear();

		for(size_t i=0; i<word.size(); i++)
		{
			if(HASH_NOT_EXIST(i))//hash.find(word[i]) == hash.end())
			{
				for(size_t j=0; j<line.size(); j++) if(word[i] == line[j])
				hash[word[i]].push_back(j);
			}
		}

	//	for(size_t i=0; i<target.size(); i++) for(size_t j=0; j<hash[target[i]].size(); j++)
	//		cout << target[i] << ": " << hash[target[i]][j] << endl;

		memo = vector<vector<int> >(word.size(), vector<int>(line.size()));
		for(size_t i=0; i<word.size(); i++) for(size_t j=0; j<line.size(); j++) memo[i][j] = -1;
		for(int i=0; i<line.size(); i++) memo[word.size()-1][i] = 1;

		int res = 0;
		// size_t型はunsignedだからマイナス注意
		if(HASH_NOT_EXIST(0)) { ofs << "Case #" << n+1 << ": " << setw(4) << setfill('0') << res%10000 << endl; continue; }
		for(int i=hash[word[0]].size()-1; i>=0; i--)
		{
			res += recursive(0, hash[word[0]][i]);
		}

		ofs << "Case #" << n+1 << ": " << setw(4) << setfill('0') << res%10000 << endl;
	}

	return 0;
}


int recursive(int w, int l)
{
	if(memo[w][l] != -1) return memo[w][l];
	if(HASH_NOT_EXIST(w+1)) { memo[w][l]; return 0; }
	vector<int>::iterator itr = hash[word[w+1]].end() - 1;
	int ll = *itr;
	int sum = 0;
	while(ll > l)
	{
		sum += recursive(w+1, ll) % 10000;
		// iteratorはbegin()より前は参照してだめよ．end()より後もだめよ．
		// ただコンテナの最後の要素の次がend()だからコンテナ一つ飛び出すのはいいよ．
		if(itr <= hash[word[w+1]].begin()) break;
		itr--;
		ll = *itr;
	}
	memo[w][l] = sum;
	return sum;
}


