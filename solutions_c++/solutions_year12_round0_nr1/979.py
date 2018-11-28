#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";

string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";

int main()
{
	char to[256];
	
	for(int i=0; i<s1.size(); i++)
		to[s1[i]] = s2[i];
	
	int T;
	scanf("%d\n", &T);
	
	for(int caso=1; caso<=T; caso++)
	{
		char s[500];
		gets(s);
		for(int i=0; i<strlen(s); i++)
			s[i] = to[s[i]];
		
		printf("Case #%d: %s\n", caso, s);
	}
	
	return 0;
}
