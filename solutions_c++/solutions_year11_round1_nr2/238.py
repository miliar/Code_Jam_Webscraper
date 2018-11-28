#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

struct word
{

string s;
int index, depth, mask;
};

int mask(string s)
{
int ret = 0;
for(int i=0; i<s.size(); i++) 
	ret |= 1<<(s[i]-'a');
return ret;
}

string unmask(string s, int m)
{
string ret = "";
for(int i=0; i<s.size(); i++)
	ret += ((1<<(s[i]-'a')) & m ) ? s[i] : '-';
return ret;
}


int main()
{

fstream In("b-small.in", ios::in);
fstream Out("b-small.out", ios::out);

int tests;

In >> tests;


for(int h=0; h<tests; h++)
{
int N , M;

In >> N >> M;

vector<word > dict(N);

for(int i=0; i<N; i++) 
{
	In >> dict[i].s;
	dict[i].index = i;
	dict[i].depth = 0;
	dict[i].mask = mask(dict[i].s);
}

string ret = "";


for(int g = 0; g<M; g++)
{
string letters;
In >> letters;

vector<word> v = dict;

for(int i=0, m=0; i<26; i++)
{
map<string, int> table;
set<string> temp;
for(int j=0; j<N; j++)
{	string s = (unmask(v[j].s, m) );
	temp.insert(s);
	table[s] |= v[j].mask;
}
for(int j=0; j<N; j++)
	if(table[unmask(v[j].s, m)] & (1<<(letters[i]-'a') ) )
		v[j].depth += !(v[j].mask & (1<<(letters[i]-'a') ) );

m |= 1<<(letters[i]-'a');
}
int index = 0, best = v[0].depth;
for(int i=0; i<N; i++)
	if(best < v[i].depth)
	{
		index = i;
		best = v[i].depth;
	}

ret += (g==0 ? "" : " ");
ret += v[index].s;
}

Out << "Case #" << h+1 << ": " << ret << endl;

}

In.close();

Out.close();

return 0;

}
 
