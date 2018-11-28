#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>

using namespace std;

int main()
{
    int t,i,n,m,j,k,check,count;

	cin>>t;
	for(i=0;i<t;i++)
	{
	    count = 0;
	    cin>>n>>m;
	   /* stringstream in(str);
	    in>>n;
	    stringstream in1(str1);
	    in1>>m;*/
	    for(k=n;k<=m;k++)
	    {
	        string::iterator it;
	        std::string str1;
            std::stringstream out;
            out<<k;
            str1=out.str();
            int size=(int)str1.size();
	        for(j=0;j<size;j++)
            {
                string lastchar;
                lastchar.append(1,str1[(int)str1.size()-1]);
                it=str1.end()-1;
                str1.erase(it);
                str1.insert(0,lastchar);
                stringstream in1(str1);
                in1>>check;
                if(check>n && check<=m && check>k)
                    count++;
            }

        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
