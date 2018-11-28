#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

char word[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int T;
string s1,s2;
int l1,l2;

int main()
{
	scanf("%d\n",&T);
	for (int temp=1;temp<=T;++temp)
	{
		getline(cin,s1);
		l1=s1.size();
		s2.resize(l1);
		for (int i(0);i<l1;++i)
		{
            if (s1[i]==' ') s2[i]=s1[i];
			else s2[i]=word[s1[i]-97];
        }
		cout << "Case #" << temp << ": " << s2 << endl;
	}
	return 0;
}
