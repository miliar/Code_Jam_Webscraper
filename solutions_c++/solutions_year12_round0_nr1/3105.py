#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;


#define SMALL
//#define LARGE

char s[]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq";
char o[]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz";
int finds(char ss)
{
	for(int i=0;i<127;i++)
	{
		if(s[i]==ss)
			return i;
	}
}

int main() {

#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	char ss[101];
	string str;

	int N;
	cin >> N;
	cin.getline(ss,101);
	for(int n=1;n<N+1;n++)
	{
		cin.getline(ss,101);
		printf("Case #%d: ", n);
		for(int i=0;ss[i]!='\0';i++)
		{
			cout<<o[finds(ss[i])];
		}
		cout<<endl;
	
	}
	
	return 0;
}
