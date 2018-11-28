#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int solve(string word,string sub)
{
	if (sub.empty())
		return 1;
	else if (word.empty())
		return 0;

	int cnt = 0;
	for (int i = 0;i < (int)word.size()-(int)sub.size()+1;i++)
	{
		if (word[i] == sub[0])
			cnt += solve(word.substr(i+1),sub.substr(1));
	}
	return cnt;
}

int main()
{
	ifstream fin("C-small-attempt3.in");
	ofstream fout("cout.txt");

	int n;
	fin >> n;
	string trash;
	getline(fin,trash);
	for (int i = 0;i < n;i++)
	{
		string str;
		getline(fin,str);
		int res = solve(str,"welcome to code jam");
		if (res >= 10000)
			res %= 10000;
		fout << "Case #" << i+1 <<": " << setw(4) << setfill('0') << res << endl;
	}
}