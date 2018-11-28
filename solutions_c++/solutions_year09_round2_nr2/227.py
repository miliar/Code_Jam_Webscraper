#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

#define MAXCHR 32

string stripZeroes(string t, int &howMany)
{
	string ret = "";
	howMany = 0;

	for ( int i = 0 ; i < t.size() ; i++ )
	{
		if ( t[i] != '0' ) ret += t[i];
		else howMany++;
	}

	return ret;
}

int main (void)
{
	int n;

	scanf("%d",&n);

	for ( int i = 0 ; i < n ; i++ )
	{
		char t[MAXCHR];
		string n;
		scanf(" %s",t);
		n = t;
//		n = stripZeroes(t);
//		printf("%s\n",n.c_str());
		if ( !next_permutation(n.begin(), n.end()) )
		{	
			int temp;
			n = stripZeroes(n,temp);
			for ( ; temp >= 0 ; temp-- )
			n.insert(1,"0");
//			next_permutation(n.begin(), n.end());
		}
		printf("Case #%d: %s\n",i+1,n.c_str());
	}

	return 0;
}
