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

	__int64 tc,tcounter,i,j,n,c;
	long double m,x,t,L;
	vector<long double> d;
	scanf("%I64d",&tc);
	tcounter = 0;

	while(tcounter++<tc)
	{
		
		scanf("%lf%lf%I64d%I64d",&L,&t,&n,&c);
		//cin >> L>>t>>n>>c;		

		d.clear();

		for(i=0;i<c;i++)
		{
			scanf("%lf",&x);
			//cin >> x;
			d.push_back(x);
		}

		for(i=c;i<n;i++)
		{
			d.push_back(d[i%c]);
		}
		long len = d.size();
		vector<long double> temp(d);

		long double first = temp[len-1];
		long double second = temp[len-2];
		long double output = 0,tp;
		for(i=0;i<len;i++)
		{
			tp = output + d[i]/0.5;
			
			if(L==0)
				output += d[i]/0.5;
			else if(L>=1 && tp<t)
				output += d[i]/0.5;
			else if(tp>=t)
			{
				output = t; 
				tp = (tp-t)*0.5;
				temp.clear();
				temp.push_back(tp);
				for(i+=1;i<len;i++)
				{
					temp.push_back(d[i]);
				}

				vector<long double > tmp(temp);
				sort(tmp.begin(), tmp.end());
				
				if(tmp.size()>0)first = tmp[tmp.size()-1];
				if(tmp.size()>1)second = tmp[tmp.size()-2];

				len = tmp.size();


				for(i=0;i<len-2;i++)
				{
					output += tmp[i]/0.5;
				}
				if(L==1)
				{
					if(len>1)
						output += tmp[len-1]+(tmp[len-2]/0.5);
					else if(len==1)
						output += tmp[len-1];
					else if(len==0)
						output += 0;
				}
				if(L==2)
				{
					if(len>1)
						output += tmp[len-1]+tmp[len-2];
					else if(len==1)
						output += tmp[len-1];
					//else if()
				}

				break;
			}
		}

	
		printf("Case #%I64d: %.0lf\n",tcounter, output);




	}
	
    return 0;
}
