
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <fstream>

using namespace std;

#define LL long long
#define PI 3.14159265358979323846

void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		int p,k,l;
		in>>p>>k>>l;
		int i,sum=0;
		int d[1000];
		for(i=0;i<l;i++){
			in>>d[i];sum+=d[i];
		}
		if( p*k > sum)
			out<<"Case #"<<z+1<<": impossible\n";
		sort(d,d+l,greater<int>());
		int f=0;sum=0;
		for(i=0;i<l;i++)
		{
			if( i%k==0)
				f++;
			sum+=d[i]*f;
		}
		out<<"Case #"<<z+1<<": "<<sum<<"\n";



	}
}