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
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int numTests;
	cin >> numTests;
	for(int z=0;z<numTests;z++)
	{

	map<string,int> mexist;

	int N,M;
	cin >> N >> M;

	for(int t=0;t<N;t++)
	{
	    string temp,temp1;
	    cin >> temp;
	    temp1 = "/";
	    for(int len=1;len<temp.size();len++)
	    {
            if(temp[len]!='/')
            temp1 = temp1+ temp[len];
            else
            {
        //    cout << "mexist " <<temp1 <<"-"<< endl;
            mexist[temp1]=3;
            temp1=temp1+"/";
            }
        }
     //   cout << "mexist " <<temp <<"-"<< endl;
        mexist[temp]=3;
    }
     int count=0;
    for(int t=0;t<M;t++)
    {
        string temp , temp1;
        cin >> temp;
        temp1="/";
        vector<string> nv;
        for(int q=1;q<temp.length();q++)
        {
           if(temp[q]!='/')
           temp1 = temp1 +  temp[q];
           else
           {

           nv.push_back(temp1);
           temp1 = temp1 + "/"    ;
           }
        }
        nv.push_back(temp);

       for(int q=nv.size()-1;q>=0;q--)
       {

        int t=  mexist[nv[q]];
        if(t==0)
        {
        mexist[nv[q]]++;
        count++;
     //   cout << "nv "    << nv[q]<<"-"<< endl;
        }
        else
        break;
       }


    }

     cout << "Case #"<<(z+1) << ": " << count << endl;

    }

	return 0;
}
