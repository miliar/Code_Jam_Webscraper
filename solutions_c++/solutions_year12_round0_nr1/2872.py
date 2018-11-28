
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

int main(){
	map <char,char> googlerese;
	googlerese['a'] = 'y';
	googlerese['b'] = 'h';
	googlerese['c'] = 'e';
	googlerese['d'] = 's';
	googlerese['e'] = 'o';
	googlerese['f'] = 'c';
	googlerese['g'] = 'v';
	googlerese['h'] = 'x';
	googlerese['i'] = 'd';
	googlerese['j'] = 'u';
	googlerese['k'] = 'i';
	googlerese['l'] = 'g';
	googlerese['m'] = 'l';
	googlerese['n'] = 'b';
	googlerese['o'] = 'k';
	googlerese['p'] = 'r';
	googlerese['q'] = 'z';
	googlerese['r'] = 't';
	googlerese['s'] = 'n';
	googlerese['t'] = 'w';
	googlerese['u'] = 'j';
	googlerese['v'] = 'p';
	googlerese['w'] = 'f';
	googlerese['x'] = 'm';
	googlerese['y'] = 'a';
	googlerese['z'] = 'q';

	freopen("speakingTongues.in","r",stdin);
	freopen("speakingTongues.out","w",stdout);
	string s;
	int n,cases=1;scanf("%d",&n);
	getline(cin,s);
	while(n--){
		getline(cin,s);
		printf("Case #%d: ",cases++);
		for (int i = 0; i < s.length(); ++i)
		{
			char c=s[i];
			if(c!=' ')
				printf("%c",googlerese[c]);
			else
				printf(" ");
		}
		if(n)
			printf("\n");

	}


    return 0;
}