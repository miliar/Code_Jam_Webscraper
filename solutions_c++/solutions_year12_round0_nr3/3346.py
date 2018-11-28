// cj1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int count (int a)
{
	int sum =0;
	while(a>0)
	{
		a/=10;
		++sum;
	}
	return sum - 1;
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w",stdout); 
    int T;
		int a, b, ans, i, rot, mul,mul1;
        cin >> T;
		for(int tc=1;tc<=T;tc++) 
        { 
			cin >> a >> b; 
			rot = count(a);
			mul = mul1 = 1;
			for(i =0; i < rot/2; ++i)
				mul1*=10;
			mul = mul1*mul1;
			if(rot%2) 
			{ mul*=10; mul1*=10;}

			ans = 0;
			for(i =a; i < b;++i)
			{
				int no = i;
				int r = ((rot%2 == 1) && (no/mul1 == no%mul1) ? rot/2 : rot); 
				for(int j = 0; j < r ; ++j)
				{
					no = no/10 + (no%10)*mul;
					if((no > i) && (no <=b))
						++ans;
				}
			}

			cout << "Case #"<<tc<<": "<< ans <<endl; 
        } 
	fclose(stdin);
	fclose(stdout);
	return 0;
}

