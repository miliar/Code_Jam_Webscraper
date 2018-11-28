#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <fstream>

using namespace std;

int main()
{
	int t;
	int n,s,p,x,c;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
	fin>>t;
	for (int i = 1; i <= t; i++)
	{
	    c = 0;
	    fin>>n>>s>>p;
	    if (p == 0)
	    {
	        c = n;
	        for (int j = 1; j <= n; j++) fin>>x;
	    }
	    else if (p == 1)
	    {
	        for (int j = 1; j <= n; j++)
	        {
	            fin>>x;
	            if (x > 0) c++;
	        }
	    }
	    else
	    {
	        for (int j = 1; j <= n; j++)
	        {
	            fin>>x;
                if (x > 3*(p-1)) c++;
                else if ((x >= 3*(p-1)-1) && (s > 0))
                {
                    c++;
                    s--;
                }
	        }
	    }
	    fout<<"Case #"<<i<<": "<<c<<endl;
	}
	fout.close();
	return 0;
}
