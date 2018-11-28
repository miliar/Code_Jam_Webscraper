#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>


using namespace std;

FILE *fp;
int t;
string s;
long long ans ;

int idx[100];

bool flag[100];

inline int get(char ch)
{
	if(ch >= '0' && ch <= '9')
		return ch - '0';
	return ch - 'a' + 10;
}

int d[100];

long long pow(int n,int k)
{
	long long sum = 1;
	for(int i = 0;i < k;i ++)
		sum *= n;
	return sum;
}

int main()
{
	fp = fopen("out.txt","w");

	cin >> t;
	getline(cin,s);
	s.clear();
	int r = 1;
	while(--t >= 0)
	{
		getline(cin,s);
		memset(idx,-1,sizeof(idx));
		memset(flag,false,sizeof(flag));

		if(s.size() == 1)
		{
			ans = 1;
			fprintf(fp,"Case #%d: %lld\n",r,ans);
		    r ++;
			continue;
		}


		int base = 1;
		int temp = get(s[0]);
		idx[temp] = 1;
		d[0] = 1;
		flag[1] = true;

		for(int i = 1;i < s.size();i ++)
		{
			temp = get(s[i]);
			if(idx[temp] != -1)
			{
				d[i] = idx[temp];
				continue;
			}
			base ++;
			int j;
			for(j = 0;j < 36;j ++)
			{
				if(flag[j] == false)
				{
					break;
				}
			}
			idx[temp] = j;
			d[i] = j;
			flag[j] = true;
		}
		if(base == 1)
			base ++;

		ans = 0;

		for(int i = 0;i < s.size();i ++)
		{
			long long p = pow(base,s.size() - 1 - i);
			ans += p * (long long)d[i];
		}

		fprintf(fp,"Case #%d: %lld\n",r,ans);
		r ++;
	}
		


			





	

	return 0;
}