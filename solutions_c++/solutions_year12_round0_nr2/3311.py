// cj1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w",stdout); 
    int T;
		int n, c, s, p, ans, i, no;
        cin >> T;
		for(int tc=1;tc<=T;tc++) 
        { 
			cin >> n >> s >> p; 
			ans = 0;
			for(i =0; i < n;++i)
			{
				cin >> c;
				no = c/3 + (c%3 == 0 ? 0 : 1);
				
				if(no >= p)
					++ans;
				else if(s && no && (c%3 != 1) && (no+1>=p))
				{
					++ ans; --s;
				}
			}

			cout << "Case #"<<tc<<": "<< ans <<endl; 
        } 
	fclose(stdin);
	fclose(stdout);
	return 0;
}

