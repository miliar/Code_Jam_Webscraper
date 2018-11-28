#include <iostream>
#include <fstream>

using namespace std;

int a[10006];

int main()
{
    ifstream iff;
    iff.open("c.in");
    ofstream of;
    of.open("c.out");
    int test;
    iff>>test;
    for(int t=0; t<test; t++)
    {
	int n,l,h;
	iff>>n>>l>>h;
	for(int i=0; i<n; i++)
	{
	    iff>>a[i];
	}
	
	int ans = 1;
	for(int i=l; i<=h; i++)
	{
	    ans = 0;
	    for(int j=0; j<n; j++)
	    {
		if( i>a[j] && i % a[j] != 0  ){ans = 1;break;}
		if( i<a[j] && a[j]% i != 0  ){ans = 1;break;}
	    }
	    if(ans == 0)
	    {
	      of<<"Case #"<<t+1<<": "<<i<<endl;
	      break;
	    }
	}
	if(ans == 1)of<<"Case #"<<t+1<<": NO"<<endl;
    }
    return 0;
}