
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back
#define LL long long
#define LD long double



int main()
{
	ifstream in("C-small-attempt0.in");

	FILE* out = fopen("C-out-SMALL.out", "w");
	int t,l,h,n;
	in>>t;

	for(int i=1;i<=t;i++)
	{
		in>>n>>l>>h;
		vi freq(n);
		for(int j=0;j<n;j++)
			in>>freq[j];

		fprintf(out, "Case #%d: ",i);
		bool flag = true;
		for(int j=l;j<=h;j++)
		{
			flag = true;
			int k;
			for(k=0;k<n;k++)
			{
				int mi=min(j, freq[k]);
				int mx = max(j, freq[k]);

				if(mx%mi==0)
				{
					continue;
				}

				flag = false;
				break;
			}

			if(flag)
			{
				fprintf(out, "%d\n", j);
				break;
			}
		}
		
		if(!flag)
			fprintf(out, "NO\n");
	}

	fclose(out);
	return 0;
}