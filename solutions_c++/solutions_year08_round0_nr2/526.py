#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <iostream>
#include <map>

#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	scanf("%d", &nTests);
	for(testId=1;testId<=nTests;testId++)
	{

		//XXX  -- Read input --  XXX
		int ta, na, nb, tmp;
		scanf("%d", &ta);
		scanf("%d", &na);
		scanf("%d", &nb);

		vector<int> schedA;
		vector<int> schedB;

		vector<int> readyA;
		vector<int> readyB;

		char str[1024];
		for(i=0;i< (na+nb);i++)
		{
        	scanf("%s", str);
			str[2]='\0';
			tmp = (atoi(str) * 60) + (atoi(str+3));
			//cout << tmp << endl;

			if(i<na)
				schedA.push_back(tmp);
			else
				schedB.push_back(tmp);

        	scanf("%s", str);
			str[2]='\0';
			tmp = (atoi(str) * 60) + (atoi(str+3));
			//cout << tmp << endl;

			if(i<na)
				readyB.push_back(tmp+ta);
			else
				readyA.push_back(tmp+ta);
		}

		sort(schedA.begin(), schedA.end());
		sort(schedB.begin(), schedB.end());

		sort(readyA.begin(), readyA.end());
		sort(readyB.begin(), readyB.end());

		#if 0
		vector<int>::iterator iter;
		for(iter=readyA.begin(); iter!=readyA.end(); iter++)
			cout << *iter<<" ";
		cout <<endl;
		for(iter=readyB.begin(); iter!=readyB.end(); iter++)
			cout << *iter<<" ";
		cout <<endl;
		#endif

		//XXX  -- Process input --  XXX

		vector<int>::iterator iter1, iter2;
		iter1=schedA.begin();
		iter2=readyA.begin();
		int numA=0;
		for( ; iter1!=schedA.end(); iter1++)
		{
			if ((iter2 != readyA.end() ) && (*iter2 <= *iter1))
			{
				iter2++;
				continue;
			}
			else
			{
				numA++;
			}
		}

		iter1=schedB.begin();
		iter2=readyB.begin();
		int numB=0;
		for( ; iter1!=schedB.end(); iter1++)
		{
			if ((iter2 != readyB.end() ) && (*iter2 <= *iter1))
			{
				iter2++;
				continue;
			}
			else
			{
				numB++;
			}
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d %d\n",testId, numA, numB);

	}

	return 0;
}
