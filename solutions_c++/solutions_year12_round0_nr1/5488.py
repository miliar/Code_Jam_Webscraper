#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;

#define RET return
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define SZ(n) ((int)n.size())

#define FORN(i,start,end) for(int i=start;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;--i)
#define SET(a,n) memset(a,n,sizeof(a))
#define foreach(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back

typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;

#define MAX 101

int main()
{
 	string input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
 	string output = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
 	map<char, char> mp;
 	int ln = SZ(input);
 	FOR(i, ln) {
  	    if (input[i] == ' ')
  	       continue;
		if (mp.count(input[i]) && (mp[input[i]] != output[i])) {
  		   cout<<"Dam you!! "<<i<<endl;
  		} else {
	   	   mp[input[i]] = output[i];
	    }
    }
    mp['q'] = 'z';
    mp['z'] = 'q';
    int test, line = 1;
    char input_line[MAX];
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    string input_l;
    fin>>test;
    fin.getline(input_line, MAX);
    while(line <= test ) {
	    fin.getline(input_line, MAX);
	    fout<<"Case #"<<line<<": ";
	    int index = 0;
		while (input_line[index]) {
  			 if (input_line[index] == ' ') {
			   fout<<" ";
             } else {
	   		   fout<<mp[input_line[index]];
	   		 }
	   		 index++;
		}
		fout<<endl;
		line++;
	}
 	system("pause");
 	return 0;
}
