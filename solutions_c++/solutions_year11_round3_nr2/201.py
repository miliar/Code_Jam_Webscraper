#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include<math.h>
#include<sstream>
#include<fstream>
#include <algorithm>
using namespace std;
long long a[1000006], b[1000006];
int main()
{
	//__int64 kk;
	ofstream fo("G:\\Ans.txt",ios_base::out);
	//fo.setf(ios::fixed);
   // fo.setf(ios::showpoint);
    //fo.precision(8);
	ifstream fi("G:\\Cin.txt",ios_base::in);

	long long  t,l,n,c,i;
	long long  ti,t1,t2;
	//scanf("%d", &t);
	fi>>t;
	for (int k = 1; k<= t; k++)
	{
		fi>>l;
		fi>>ti;
		fi>>n;
		fi>>c;
		for (i=0;i<c;i++)
			fi>>a[i];
		for (i=0;i<n;i++)
			b[i] = a[i%c];
		i=0; t1 = 0;
		while(i<n && t1 < ti)
		{
			t1 = t1 + b[i] * 2;

			if (t1 == ti)
			{
				i++;
				break;
			}
			else if (t1 > ti)
			{
				t1 = t1 - b[i] * 2;
				t2 = ti - t1;
				t1 = t1+t2;
				t2 = t2/2;
				b[i] = b[i] -t2;
				break;
			}

			i++;
		}

		fo<<"Case #"<<k<<": ";
		if (i == n)
		{
			fo<<t1<<endl;
			continue;
		}

		sort(b + i, b+n);

		n--;
		while(n>=i)
		{
			if (l>0)
			{
				l--;
				t1 = t1+b[n];
			}
			else
			{
				t1=t1+b[n]*2;
			}
			n--;
		}

		fo<<t1<<endl;		
	}
	return 0;
}