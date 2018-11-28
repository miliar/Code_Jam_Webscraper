// Author -Swarnaprakash.U
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cctype>
#include <cassert>
#include<cstring>


using namespace std;

const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define PB 			push_back
#define SZ(x)		((int)((x).size()))
#define TR(i,x) 	for(i=0;i<(x).size();++i)
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;
#define HELLO		if(debug) puts("hello");
#define LL 			long long
#define INF			0x3f3f3f3f
#define M			105



int main()
{
	int t,tc;
	scanf("%d",&tc);
	for(t=1;t<=tc;++t)
	{
		char a[100];
		scanf("%s",a);
		int len=strlen(a);
		if(next_permutation(a,a+len))
		{
			printf("Case #%d: %s\n",t,a);
		}
		else
		{
			string s(a);
			char c='9'+1;
			int i;
			TR(i,s)
				if(s[i]!='0')
					c=min(c,s[i]);
			assert(isdigit(c));
			TR(i,s)
				if(s[i]==c)
				{
					s[i]='9'+1;
					break;
				}
			sort(ALL(s));
			s.resize(SZ(s)-1);
			//DB(c);
			printf("Case #%d: %c0%s\n",t,c,s.c_str());	
		}
	}
	return 0;
}
