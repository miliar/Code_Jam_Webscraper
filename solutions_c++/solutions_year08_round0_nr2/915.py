#include <stdio.h>
#include <string>
#include <set>
#include <iostream>
using namespace std;

int main()
{
	int n, cases, s, q, i;
	string str;
	set<string> bla;
	scanf("%d", &n);
	for(cases=1; cases<=n; ++cases)
	{
		scanf(" %d ", &s);
		
		for(i=0; i < s; ++i)
			getline(cin, str);
		
		scanf(" %d ", &q);
		
		int count = 0;
		bla.clear();
		//cout << "q" << q << endl;
		getline(cin, str);
		bla.insert(str);
		//cout << str << bla.size() << endl;
		
		for(i=1; i<q; ++i)
		{
			
			getline(cin, str);
			bla.insert(str);
			//cout << str << bla.size() << endl;
			if(bla.size() == s)
			{
				++count;
				bla.clear();
				bla.insert(str);
			}
		}
		
		printf("Case #%d: %d\n", cases, count);
	}
	return 0;
}
