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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define LL long long
#define LD long double
#define pi 3.1415926535897932384626433
#define sqr(a) ((a)*(a))

using namespace std;


int T;
map<char,char> dic;
string str[30];

void makeDic(string sampleg,string samplen){	
	int length = sampleg.length();
	for (int i=0;i<length;i++)
	{
		if (dic.count(sampleg[i]) == 0)
			dic[sampleg[i]] = samplen[i];
	}	
}

string translate(string googlerese)
{
	string ans = "";
	
	int length = googlerese.length();
	for (int i=0; i<length; i++)
		ans += dic[googlerese[i]];
	
	return ans;
}

int main()
{

	makeDic("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	makeDic("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	makeDic("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	dic['q'] = 'z';
	dic['z'] = 'q';
	
	freopen("f:/googlejam/q/A-small-attempt0.in", "r", stdin);
	freopen("f:/googlejam/q/A-small-attempt0.out", "w", stdout);
	
	scanf("%d\n", &T);
	for (int i = 0; i < T; i ++)
		getline(cin,str[i]);
		
	for (int Case = 1; Case <= T; Case ++)
		cout << "Case #" << Case << ": " << translate(str[Case-1]) << endl;
	
	return 0;
}
