#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
int main(){

    int Test,cnt=1;cin>>Test;
    while(Test--)
    {
        int cval,temp,n;
	char r,e,d; 
	char m,t;
	string str;
	cin>>cval;
		if(cval>0)cin>>r>>e>>d;
        cin>>temp;
		if(temp>0) cin>>m>>t;
        cin>>n;
        cin>>str;
        vector<char> stack;
        stack.push_back(str[0]);
	int x=1;
        while(x<str.size())
        {
            stack.push_back(str[x]);
            if(cval)
            for(int j=stack.size()-1;j>=0;j--)
            {

                if(j>0&&stack[j]==r&&stack[j-1]==e)
                {
			stack.erase(stack.begin()+stack.size()-2);
			stack.erase(stack.begin()+stack.size()-1);
			stack.push_back(d);
			}

                if(j>0&&stack[j]==e&&stack[j-1]==r)
                {
			stack.erase(stack.begin()+stack.size()-2);
			stack.erase(stack.begin()+stack.size()-1);
			stack.push_back(d);
		}
            }



            if(temp)
            {
                if(stack[stack.size()-1]==m)
                {
                    for(int x=0;!stack.empty()&&x<stack.size()-1;x++)
                    {
                        if(stack[x]==t)
                        {
                            stack.clear();
                        }
                    }
                }
                if(stack[stack.size()-1]==t)
                {

                    for(int x=0;!stack.empty()&&x<stack.size()-1;x++)
                    {

                        if(stack[x]==m)
                        {

                            stack.clear();
                        }
                    }
                }
            }
	x++;
        }
        if(stack.empty())
        	
cout<<"Case #"<<cnt++<<": []\n";
        else
        {
		cout<<"Case #"<<cnt++<<": [";

       		for(int x=0;x<stack.size()-1;x++)
       			cout<<stack[x]<<", ";

	      	cout<<stack[stack.size()-1] <<"]\n";
        }
    }
	return 0;
}

