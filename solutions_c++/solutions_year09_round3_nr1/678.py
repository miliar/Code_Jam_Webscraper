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


int main()
{
	freopen("A-small-attempt4.in", "r", stdin);
	freopen("A-small-attempt4.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	char str[1000];

	gets(str);	
	int cases;

	for(cases = 0; cases < Cases; cases++)
	{
		gets(str);
		string sss = string(str);
		if(sss.length()==1)
		{
			printf("Case #%d: %d\n", cases+1, 1);
		}else
		{
			map<char, int> number;
		string s="";
		int k,m=2;
		number.insert(make_pair(str[0], 1));
		s += string(1,str[0]);
		for(int f=1; f<1000; f++)
		{
			if(str[f]!=str[0])
				break;
		}
		number.insert(make_pair(str[f], 0));
		s += string(1,str[f]);
// 		if(str[1]!=str[0])
// 			number.insert(make_pair(str[1], 0));

		for (k=0;str[k];k++)
		{
			if (s.find(str[k]) == -1)
			{
				number.insert(make_pair(str[k],m));
				m++;
				s += string(1,str[k]);
			}
		}
		int len = s.length();
		int res = 0;
		for(int i=0;i<k;i++)
		{
			res += number[str[i]] * pow(len, k-i-1); 
		}
		printf("Case #%d: %d\n", cases+1, res);
		}


	}
	return 0;
}