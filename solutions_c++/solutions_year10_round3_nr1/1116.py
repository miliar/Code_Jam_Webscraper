
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long unsigned int n;

int main()
{

	printf("\nHello GCJ");

		freopen("A-large.in","r",stdin);
		freopen("Output.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	//scanf("%d",&testcase);
	cin>>testcase;

	for (int caseId=1;caseId<=testcase;caseId++)
	{
		vector<long unsigned int> l;
		vector<long unsigned int> r;
		cin>>n;
		long unsigned int a,b;
		for(int i=0; i<n;i++)
		{
			cin>>a;
			l.push_back(a);
			cin>>b;
			r.push_back(b);
			
		}
		long long result = 0;
		for(int i=0; i<n;i++)
		{
			for(int j = i+1; j <n;j++)
			{
				if((l[i]>l[j] && r[i]<r[j]) || (l[i]<l[j] && r[i]>r[j]))
				{
					result++;
				}
			}
		}

		cout<<"Case #"<<caseId<<": "<<result;
		cout<<"\n";

	}
	return 0;
}

