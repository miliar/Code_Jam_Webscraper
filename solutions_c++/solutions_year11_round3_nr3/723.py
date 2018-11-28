#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template<class T> inline T gcd(T a,T b)//NOTES:gcd(
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}

////file selection
void SetInputFile()
{ char filename[32], infile[32], outfile[32]; scanf("%s", filename);
  strcpy(infile, filename); strcpy(outfile, filename); strcat(infile, ".in"); strcat(outfile, ".out");
  freopen(infile, "r", stdin); 
  freopen(outfile, "w", stdout);
}


char s[200][200];
int main()
{
    SetInputFile();

	long tc,tcounter,i,j,n,l,h,m,x;
	vector<long> d;
	cin >> tc;
	tcounter = 0;

	while(tcounter++<tc)
	{
		
		cin >> n>>l>>h;		

		d.clear();
		m = 0;
		
		for(i=0;i<n;i++)
		{
			cin >>m;
			d.push_back(m);
		}

		long t = -1;

		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(!(d[j]%i==0||i%d[j]==0))break;
			}
			if(j==n)
			{
				t = i;
				break;
			}
		}

		if(t<l||t>h)
			cout << "Case #"<<tcounter<<": NO"<<endl;
		else
			cout << "Case #"<<tcounter<<": "<<t<<endl;




	}
	
    return 0;
}
