#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define ok(a, b) ((a) >= 0 && (a) < N && (b) >= 0 && (b) < M && mat[a][b] == '.')

ifstream fin("c:\\B-small-attempt3.in");
ofstream fout("c:\\B-small-attempt3.out");



string run()
{
	set<char> hasComb;
	map <char, pair<char, char> > comb;
	map <char, char> revoke;
	string tmp;
	int C,D;
	fin >> C;
	
	for ( int c = 0; c < C; c++)
	{
		fin >> tmp;
	//	cout<<tmp<<' ';
		comb[tmp[0]] = make_pair(tmp[1], tmp[2]);
		comb[tmp[1]] = make_pair(tmp[0], tmp[2]);
		hasComb.insert(tmp[0]);
		hasComb.insert(tmp[1]);
	}
	//cout<<endl;
	
	fin >> D;
	for ( int d = 0; d < D; d++)
	{
		fin >> tmp;
	//	cout<<tmp<<' ';
		revoke[tmp[0]] = tmp[1];
		revoke[tmp[1]] = tmp[0];
	}
	//cout<<endl;
	
	string res=string("");
	map<char,int> cnt;
	
	int N;
	fin >> N;
	
	string invoke;
	fin >> invoke;
	//cout<<invoke<<endl;
	for ( int i = 0; i < invoke.length(); i ++)
	{
	//	cout<<res<<endl;
		char c = invoke[i];
		if (res.length() == 0 )
		{
			res += c;
			cnt[c]++;
			continue;
		}
		
		char last = res[res.length() - 1];
		if (hasComb.count(c) > 0 &&
			comb[c].first == last)
		{
			cnt[last] --;
			cnt[comb[c].second] ++;
			res[res.length() - 1] = comb[c].second;
			continue;
		}
		
		if ( cnt[revoke[c]] > 0)
		{
			res = string("");
			cnt.clear();
			continue;
		}
		
		res += c;
		cnt[c]++;
		
	}
	
	
	if ( res.length() == 0 ) return string("[]");
		string output = string("");
		output += res[0];
		for ( int i = 1; i < res.length(); i++)
			output += string(", ") + res[i];
		return string("[")+output + string("]");
		
		
	
}
int main() {
  
	int N;
	fin>> N;
	cout<<N<<endl;
	for( int n = 1; n <= N; n++)
	{
		string ret = run();
		//printf("Case #%d: %d\n", n, ret);
		fout<<"Case #"<<n<<": "<<ret<<endl;
   }
   return 0;
}