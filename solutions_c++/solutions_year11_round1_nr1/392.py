
#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int gcd(int a, int b)
{
    if(b == 0)
        return a;
    return gcd(b, a % b);
}

int main()
{
	freopen("out.txt", "w", stdout);
	
	int repeat,i,pd,pg;
	long long n;
	int cases=1;
	cin>>repeat;
	while(repeat--)
	{
		printf("Case #%d: ",cases++);
		cin>>n>>pd>>pg;
		if(pg==100&&pd!=100)
		{
			cout<<"Broken"<<endl;
			continue;

		}
		if(pg==0&&pd!=0)
		{
			cout<<"Broken"<<endl;
			continue;

		}
		bool ff=false;
		int x=gcd(100,pd);

		
		
		x=100/x;
		if(x<=n)
			ff=true;
		
		if(ff)
			cout<<"Possible"<<endl;
		else cout<<"Broken"<<endl;
	}


	return 0;
	
	
}
// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
