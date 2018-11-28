#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
//#include<iostream>

int t,o,ans,n,pom,minn,b;

int main()
{
    cin >> t;
    o=0;
    while (o<t)
	{
	    o++;
	    cout << "Case #" << o << ": ";
	    cin >> n;
	    pom=0;
	    ans=0;
	    minn=1000000000;
	    for (int i=0; i<n; i++)
		{
		    cin >> b;
		    pom=pom^b;
		    ans=ans+b;
		    if (minn>b) minn=b;
		}
	    if (pom!=0) {cout << "NO" << endl; continue;}
	    cout << ans-minn << endl;
	}
}
