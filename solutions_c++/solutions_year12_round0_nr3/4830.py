/*
 * A.CPP
 *
 *  Created on: Apr 14, 2012
 *      Author: mohammad
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;
string ItoS(int num )
{
       if(num == 0) return "0";
       string str;
       while(num!=0)
       {
        int nlet = num%10;
        str += (nlet+'0');
        num/= 10;
       }
       reverse(str.begin(),str.end());
       return str;
}
int StoI(string s)
{
    int v, i, result = 0;
    for(i = 0 ; i < s.size() ; i++)
    {
           v = s[i] - '0';
          result = result*10+v;
    }
    return result;
}
int main()
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("a.out","wt",stdout);
	int tt;
	cin>>tt;
	int a,b;

	for(int t = 0 ; t < tt ; t++)
	{
		set<pair<int,int> > res;
		cin>>a>>b;
		for(int i = a ; i <= b ; i++)
		{
			string s = ItoS(i);
			for(int j = 1 ; j < s.size() ; j++)
			{
				string prt1,prt2,str;
				prt1 = s.substr(0,j);
				prt2 = s.substr(j);
				str = prt2 + prt1;
				int n2 = StoI(str);
				if(n2 > i && n2 <= b )
					res.insert(make_pair(i,n2));
			}
		}
		cout<<"Case #" << t+1 <<": "<< res.size() << endl;
	}


	return 0;
}


