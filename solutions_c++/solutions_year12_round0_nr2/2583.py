#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;

//*
ifstream fin("B-large.in");
#define cin fin
ofstream fout("B-large.out");
#define cout fout
//*/

int main()
{
	int tc;
	cin>>tc;
	for(int t=1; t<=tc; t++)
	{
		int n,s,p;
		cin>>n>>s>>p;
		vector<int> a(n);
		for(int i=0; i<n; i++)
			cin>>a[i];
		
		//sort(a.begin(), a.end());
		int min1 = p + 2*max(0, p-1);
		int min2 = p + 2*max(0, p-2);

		int ans = 0;
		for(int i=0; i<a.size(); i++)
			if(a[i] >= min1)
				ans++;
			else
				if(s>0 && a[i] >= min2)
					++ans, --s; 
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}