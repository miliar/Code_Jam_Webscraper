#include <vector>
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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <queue>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("a.in");
ofstream fout("a.out");

int T;

char m[26];

void getInfo(char* a, char *b, int len)
{
	for(int i=0;i<len;i++)
	{
		if(a[i]!=' ')
		{
			m[a[i]-'a'] = b[i];
		}

	}
}
void train()
{
	char A[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char B[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char C[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";



	char A1[] = "our language is impossible to understand";
	char B1[] = "there are twenty six factorial possibilities";
	char C1[] = "so it is okay if you want to just give up";
	
	getInfo(A,A1,strlen(A));
	getInfo(B,B1,strlen(B));
	getInfo(C,C1,strlen(C));

	for(int i=0;i<26;i++)
		cout<<(char)(i+'a')<<":"<<m[i]<<endl;

	m['q'-'a'] = 'z';
	m['z'-'a'] = 'q';
	
}
int main()
{
	
	fin>>T;

	memset(m, 0, sizeof(m));
	train();
	

	char line[123];

	char res[123];
	fin.getline(line,123);

	for(int c=1;c<=T;c++)
	{
		fin.getline(line,123);

		memset(res,0,sizeof(res));
		
		for(int i=0;line[i] != '\0';i++)
		{
			char tmp = line[i];
			if(tmp == ' ')
			{
				res[i] = ' ';
			}
			else if(m[tmp-'a']=='\0')
				res[i] = '*';
			else
				res[i] = m[tmp-'a'];

		}

		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
