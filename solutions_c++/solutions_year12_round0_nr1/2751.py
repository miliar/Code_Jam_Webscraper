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

char c_table[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b',
					'k','r','z','t','n','w','j','p','f','m','a','q'};

#define SMALL
//#define LARGE
int main()
{
#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif

	int case_n;
	char back;
	vector<char> senten;
	//printf("A");

	scanf("%d", &case_n);
	scanf("%c",&back);

	for (int i=0; i<case_n; i++)
	{
		senten.clear();
		char temp;

		while (scanf("%c",&temp))
		{
			if(temp=='\n')break;
			senten.push_back(temp);	
		}
		for(int j=0;j<senten.size();j++)
		{
			if(senten[j]==' ')
				continue;
			else
			{
				senten[j]=c_table[ int(senten[j] - 'a')];
			}
		}
	
		printf("Case #%d: ",i+1);
		for(int j=0;j<senten.size();j++)
		{
			printf("%c",senten[j]);
		}
		printf("\n");

	}
	return 0;
}
