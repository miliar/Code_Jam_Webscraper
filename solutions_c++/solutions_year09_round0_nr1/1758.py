#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>

#include <boost/regex.hpp>

using namespace std;

int main()
{
	int i,j,k,m,n;
	int testId, l, d, nTests;
	cin >> l >> d >> nTests;
	string str[d];

	for(i=0; i<d; i++)
		cin >> str[i];

	for(testId=1;testId<=nTests;testId++)
	{
		//XXX  -- Read input --  XXX
		string expr;
		cin >> expr;

		//XXX  -- Process input --  XXX
		size_t found;

		found = expr.find_first_of("()");
		while(found != string::npos)
		{
			if (expr[found] == '(')
				expr[found]='[';
			else if (expr[found] == ')')
				expr[found]=']';
			else
				assert(0);

			found = expr.find_first_of("()", found+1);
		}

		//cout << "string: " << expr << endl;

		boost::regex re(expr);

		int match=0;
		for (i=0; i<d; i++)
		{
			//boost::cmatch what;
			if (boost::regex_match(str[i], re))
				match++;
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n",testId,match);



		/*
		 	for(i=0; i<nItems; i++)
			iter[i]=itemshop[i].begin();

		   double opt_cost=DBL_MAX;
		   double cur_cost;
		   for(int comb=1; 1; comb++)
		   {
		   for (i=0; i<nItems-1; i++)
		   {
		   if(iter[i] != itemshop[i].end())
		   break;
		   iter[i]=itemshop[i].begin();
		   iter[i+1]++;
		   }

		   iter[0]++;
		   }

		 */
	}

	return 0;
}
