#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <deque>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <sstream>

#define For(i,a,n) for(int i =a ; i < n ; ++i )
#define all(x) (x).begin(),(x).end()
#define n(x) (int)(x).size()
#define pb(x) push_back(x)

using namespace std;
typedef pair<int,int> pii;
const int maxn = 4;
int n;
string inp[maxn];
string out[maxn];
map<char,char> ch;

int main()
{
	inp[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	inp[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	inp[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	inp[3] = "y qee";

	
	
	out[0] = "our language is impossible to understand";
	out[1] = "there are twenty six factorial possibilities";
	out[2] = "so it is okay if you want to just give up";
	out[3] = "a zoo";

	For(i,0,maxn)
		For(j,0,n(inp[i]))
			ch[inp[i][j]]=out[i][j];
	ch['z'] = 'q';

	cin >> n;
	string str;
	getline(cin,str);
	For(i,0,n)
	{
		getline(cin,str);
//		cerr << str << endl;
		For(j,0,n(str))
			if(isalpha(str[j]))
				str[j] = ch[str[j]];
		cout << "Case #" << i+1 << ": " << str << "\n";
	}
		
	return 0;
}
