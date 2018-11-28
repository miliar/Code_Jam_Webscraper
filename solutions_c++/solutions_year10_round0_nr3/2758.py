#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <fstream>
using namespace std;

int power(int x, int y)
{
    int s = 1;
    for (int i=0; i<y; i++)
        s = s * x;
    return s;    
}

int main()
{
	ifstream cin("C-small-attempt2.in");
	ofstream cout("c.txt");
	int T, R, k, N;
	cin >> T;
	int g[10];
	int s=0, sum=0, i=0, j=0, m=0;

	for(int q = 1; q <= T; q++)
	{
	    s = 0;
	    sum = 0;
	    j = 0;
	    m = 0;
	    
		cin >> R;
		cin >> k;
		cin >> N;
		//cout << "R=" << R << "k=" << k << "N=" << N << endl;
		for (i=0; i<N; i++)
		{
		    cin >> g[i];
		    //cout << "g[" << i << "]=" <<g[i] << endl;
		}
		for (i=0; i<R; i++)
		{
		    //if (N==1)
		    //{ 
		    //    if (g[0]<=k)
		    //    {
		    //        sum=sum+g[0];
		    //        continue;
		    //    }
		    //    else break;
		    //}
		    
		        
		    s=0;
		    m=0;
		    bool flag=true;
		    while (s<=k)
		    {
		        s = s + g[j];
		        j++;
		        j=j%N;
		        m++;
		        if (m>N) 
		        {
		         flag=false;
		         break;
		        }
		    }
		    j--;
		    if (j<0) j=j+N;
		    j=j%N;
		    //cout << "s=" << s << "  j=" << j << "  i=" << i << endl;
		    //if (flag==false)
		    //    sum = sum + s;
		    //else
		        sum = sum + s - g[j];
		    //cout << "sum=" << sum << "  j=" << j << endl;
		}
	    cout << "Case #" << q << ": " << sum << endl;  	
	}
	return 0;
}
