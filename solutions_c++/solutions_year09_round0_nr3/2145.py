#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   

string s, t="welcome to code jam";

int table[501][21];

int doit(int si, int ti)
{
	if(ti==t.size() ) return 1;
	else if(si==s.size() ) return 0;

	if(table[si][ti] > -1) return table[si][ti];

	table[si][ti] = doit(si+1, ti);

	if(s[si]==t[ti]) table[si][ti] = (table[si][ti] + doit(si+1, ti+1) )% 10000;

	return table[si][ti];
}

int main()
{

int L, D, N;

fstream In("C-large.in", ios::in);
fstream Out("C-large.out", ios::out);

int T;

In >> T;
getline(In, s);

for(int h=0; h<T; h++)
{
Out << "Case #" << h+1 << ": " ;

int N, M;

getline(In, s);

memset(table, -1, sizeof(table));

int ret = doit(0, 0);

if(ret < 1000) Out << "0";
if(ret < 100) Out << "0";
if(ret < 10) Out << "0";
Out << ret << endl;

}


In.close();

Out.close();

return 0;

}
