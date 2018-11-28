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
	freopen("A-small-attempt1.in","r",stdin);
//	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
//	freopen("out2.txt","w",stdout);
	int numTests;
	cin >> numTests;
	for(int caseId=0;caseId<numTests;caseId++)
	{
     cout << "Case #"<<(caseId+1) << ": ";
     int noWires;
     vector<int> x;
     vector<int> y;
     vector<int> slope;
     cin >> noWires;
     for(int t=0;t<noWires;t++)
     {
         int temp1,temp2;
         cin >> temp1;
         x.push_back(temp1);
         cin >> temp2;
         y.push_back(temp2);
     }
     int count=0;

     for(int t=0;t<noWires;t++)
     {
        int valuex = x[t];
        int valuey = y[t];
        vector<int> indices;
        for(int q=t+1;q<noWires;q++)
        {
          if(valuex < x[q] )
          indices.push_back(q);
        }

        for(int w=0;w< indices.size();w++)
          if(valuey > y[indices[w]] )
          {
          count++;
          }
     }
     if(count==0)
     for(int t=0;t<noWires;t++)
     {
        int valuex = x[t];
        int valuey = y[t];
        vector<int> indices;
        for(int q=t+1;q<noWires;q++)
        {
          if(valuex > x[q] )
          indices.push_back(q);
        }

        for(int w=0;w< indices.size();w++)
          if(valuey < y[indices[w]] )
          {
          count++;
          }
     }
     cout << count << endl;
    }
	return 0;
}
