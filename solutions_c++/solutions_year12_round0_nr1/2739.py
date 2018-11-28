#define _USE_MATH_DEFINES
#define INF 10000000
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>

using namespace std;

typedef long long ll;
typedef pair <int,int> P;
typedef pair <P,P> PP;
typedef pair <int,PP> PPP;

static const double eps = 1e-8;

int main(){
	string str;
	map<char,char> dic;
	dic['a'] = 'y';dic['b'] = 'h';dic['c'] = 'e';
	dic['d'] = 's';dic['e'] = 'o';dic['f'] = 'c';
	dic['g'] = 'v';dic['h'] = 'x';dic['i'] = 'd';
	dic['j'] = 'u';dic['k'] = 'i';dic['l'] = 'g';
	dic['m'] = 'l';dic['n'] = 'b';dic['o'] = 'k';
	dic['p'] = 'r';dic['q'] = 'z';dic['r'] = 't';
	dic['s'] = 'n';dic['t'] = 'w';dic['u'] = 'j';
	dic['v'] = 'p';dic['w'] = 'f';dic['x'] = 'm';
	dic['y'] = 'a';dic['z'] = 'q';

	while(getline(cin,str)){
		int n = atoi(str.c_str());
		for(int i=0;i<n;i++){
			getline(cin,str);
			printf("Case #%d: ",i+1);
			for(int j=0;j<str.size();j++){
				if(str[j] == ' '){
					printf("%c",' ');
					continue;
				}
				printf("%c",dic[str[j]]);
			}
			printf("\n");
		}
		break;
	}
}