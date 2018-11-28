#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

void func(int casen);

int main()
{
	int cases;
	cin >> cases;

	for(int i=0;i<cases;i++)
	  func(i+1);	
}

void func(int casen)
{
	int n, i, j;
	long res = 0;
	long double t;

	cin >>n;

	vector<int> a(n, 0), b(n, 0);

	for(i=0;i<n;i++)
	{
		cin >> a[i] >> b[i];
	}

	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
		{
			
			if((b[i]-a[i]-b[j]+a[j])!=0)
			{
				t = a[j]-a[i];
				t = t/(b[i]-a[i]-b[j]+a[j]);
				if(t>0 && t<1)
					res++;
			}
				
		}


           cout << "Case #" << casen << ": " << res << endl;

}