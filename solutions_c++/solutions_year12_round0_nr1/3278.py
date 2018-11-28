#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char szmap[256];
int main()
{
//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("a-small.out","w",stdout);
	FILE *fp = NULL;
	
//	fp = freopen("a-test.in","r",stdin);
	fp = freopen("A-small-attempt1.in","r",stdin);
	fp = freopen("A.out","w",stdout);
	memset(szmap,0,sizeof szmap);
	/*
		ejp mysljylc kd kxveddknmc re jsicpdrysi
		our language is impossible to understand

		rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
		there are twenty six factorial possibilities

		de kr kd eoya kw aej tysr re ujdr lkgc jv
		so it is okay if you want to just give up znq bzj
		*/
	szmap['a'] = 'y';szmap['b'] = 'h';szmap['c'] = 'e';szmap['d'] = 's';szmap['e'] = 'o';szmap['f'] = 'c';szmap['g'] = 'v';
	szmap['h'] = 'x';szmap['i'] = 'd';szmap['j'] = 'u';szmap['k'] = 'i';szmap['l'] = 'g';szmap['m'] = 'l';szmap['n'] = 'b';
	szmap['o'] = 'k';szmap['p'] = 'r';szmap['q'] = 'z';szmap['r'] = 't';szmap['s'] = 'n';szmap['t'] = 'w';szmap[' '] = ' ';
	szmap['u'] = 'j';szmap['v'] = 'p';szmap['w'] = 'f';szmap['x'] = 'm';szmap['y'] = 'a';szmap['z'] = 'q';
	int testcase;
	cin>>testcase;
	char ch[1000];
	gets(ch);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		
		
		printf("Case #%d: ",caseId);

		gets(ch);
		for (int i=0;i<strlen(ch);i++)
		{
			ch[i] = szmap[ch[i]];
		}
		printf("%s\r\n",ch);
		
	}
	

	return 0;
}