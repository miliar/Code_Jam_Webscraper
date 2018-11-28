#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream in("easy.in");
ofstream out("easy.out");

int main()
{
	long test_count;
	long t;
	long n, ans=0;
	long a[10000];
	long b[10000],i,j;
	in>>test_count;
	for(t = 0;t < test_count;t++)
	{
		in>>n;
		ans = 0;
		for(i=0;i<n;i++)
			in>>a[i]>>b[i];

		for(i=0;i<n-1;i++)
			for(j=i+1;j<n;j++)
			{
				if(a[i]<a[j] && b[i]>b[j])
					ans++;
				if(a[j]<a[i] && b[i]<b[j])
					ans++;
			}
	    out<<"Case #"<<t+1<<": "<<ans<<endl;
	}

	//out<<"Case #"<<t+1<<": "<<re<<endl;
	return 0;
}
