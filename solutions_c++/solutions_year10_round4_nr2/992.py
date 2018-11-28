#include <vector>
#include <list>
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

int i;
int t,map[2050],y,p;
int flag[2050];
int len,sum,len1;

int F(int a)
{
	int it,it1,_min;
	if(a*2<=len1)
		it=F(a*2);
	else
		it=map[a*2];
	if(a*2+1<=len1)
		it1=F(a*2+1);
	else
		it1=map[a*2+1];
	_min=it>it1?it1:it;
	flag[a]=_min-1;
	return flag[a];
}
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	
	cin>>t;
	for(int CaseID=1;CaseID<=t;CaseID++)
	{
		cout<<"Case #"<<CaseID<<": ";
		cin>>p;
		sum=0;
		
		len=(int)pow(2.0,p+1.0)-1;
		len1=len-(int)pow(2.0,p+0.0);
		
		for(i=len;i>0;i--)
			cin>>map[i];
		memset(flag,0,sizeof(flag));
		
		int ttttttt=F(1);
		for(i=len1;i>0;i--)
			if(flag[i]<0)
			sum+=map[i];
		
		cout<<sum<<endl;
	}
}
