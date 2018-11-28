#include <iostream>
#include <cstdio>
#include <map>
#include <cassert>
using namespace std;
map<char, char> Map;
int main(){
	Map['a']='y';
	Map['b']='h';
	Map['c']='e';
	Map['d']='s';
	Map['e']='o';
	Map['f']='c';
	Map['g']='v';
	Map['h']='x';
	Map['i']='d';
	Map['j']='u';
	Map['k']='i';
	Map['l']='g';
	Map['m']='l';
	Map['n']='b';
	Map['o']='k';
	Map['p']='r';
	Map['q']='z';
	Map['r']='t';
	Map['s']='n';
	Map['t']='w';
	Map['u']='j';
	Map['v']='p';
	Map['w']='f';
	Map['x']='m';
	Map['y']='a';
	Map['z']='q';
	Map[' ']=' ';
	int T;
	scanf("%d\n", &T);
	for (int testcase = 0; testcase < T; ++ testcase){
		printf("Case #%d: ", testcase + 1);
		string s;
		getline(cin, s);
		for (int i = 0; i < (int)s.size(); ++ i){
			assert(Map.find(s[i]) != Map.end());
			s[i] = Map[s[i]];
		}
		printf("%s\n", s.c_str());
	}
	return 0;
}