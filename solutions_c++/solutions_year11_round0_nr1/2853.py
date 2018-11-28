/*
 * A.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: B2lawa
 */
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
#include <ext/numeric>
#include <memory.h>
#include <valarray>
using namespace std;
queue < pair<int,int> > O,B;
int main()
{
	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int t,N,n,y,b,o;
	char c;
	cin>>t;
	for(int x=1;x<=t;++x)
	{
		cin>>N;
		for(int i=0;i<N;++i)
		{
			cin>>c>>n;
			if(c=='O')O.push(make_pair(i,n));
			else B.push(make_pair(i,n));
		}
		y=0;
		b=1;
		o=1;
		//cout<<B.size()<<" "<<O.size()<<endl;
		bool f=true;
		while(!O.empty() || !B.empty())
		{
			//cout<<o<<" "<<b<<" "<<B.size()<<" "<<O.size()<<endl;
			//system("pause")
			if(!O.empty() && !B.empty())
			{
				f=true;
				if(O.front().first<B.front().first && O.front().second==o)
				{
					f=false;
					O.pop();
				}
				else if(O.front().second>o)o++;
				else if(O.front().second<o)o--;
				if(f && O.front().first>B.front().first && B.front().second==b)
				{
					B.pop();
				}
				else if(B.front().second>b)b++;
				else if(B.front().second<b)b--;
			}
			else if(!O.empty())
			{
				if(O.front().second==o)
				{
					O.pop();
				}
				else
				{
					if(O.front().second>o)o++;
					else if(O.front().second<o)o--;
				}
			}
			else
			{
				if(B.front().second==b)
				{
					B.pop();
				}
				else
				{
					if(B.front().second>b)b++;
					else if(B.front().second<b)b--;
				}
			}
			y++;
		}
		cout<<"Case #"<<x<<": "<<y<<endl;
	}
}
