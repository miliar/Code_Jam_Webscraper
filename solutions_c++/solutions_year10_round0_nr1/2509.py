#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;

bool calc(int n, int k)
{
		if(k == 0)
				return false;
		k++;
		uint32_t base = 1 << n;
		uint32_t fac = base;
		while(fac <= k)
				fac *= base;
		fac /= base;
		if(k % fac == 0)
				return true;
		else
				return false;
}


int main(int argc, char**argv)
{
		ifstream in(argv[1]);
		ofstream out(argv[2]);
		if(!in)
		{
				cerr<<"can not open input file\n"<<endl;
				return 1;
		}
		int t,n,k;
		in>>t;
		int i = 1;
		char result[100];
		while(t-- > 0)
		{
				in>>n>>k;
				bool bOn = calc(n, k);
				if(bOn)
				{
						sprintf(result, "Case #%d: ON\n", i);
				}
				else
				{
						sprintf(result, "Case #%d: OFF\n", i);
				}
				out.write(result, strlen(result));
				i++;
		}
		return 0;
}
