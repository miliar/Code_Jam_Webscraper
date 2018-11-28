#include <iostream>
#include <cstdio>
#include <memory>
#include <string.h>
using namespace std;

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char a[256];

void Learn()
{
    for (int i = 0; i < 256; ++i) {
    	a[i] = i;
    }
    for (int i = 0; i < s1.length(); ++i) {
    	a[s1[i]] = s2[i];
    }
    swap(a['q'], a['z']);
}

int main()
{
	Learn();

    int nn;
    scanf("%d\n", &nn);
    for (int ii = 1; ii <= nn; ++ii) {
    	char s[1024];
    	gets(s);
    	for (int i = 0, ilen = strlen(s); i < ilen; ++i) {
    		s[i] = a[s[i]];
    	}
    	printf("Case #%d: %s\n", ii, s);
    }

	return 0;
}
