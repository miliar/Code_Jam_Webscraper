#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;
FILE *fp;

int cnt[45];
int t;
int n;
int main()
{
	fp = fopen("out.txt","w");
	cin >> t;
	int r = 1;
	while(--t >= 0)
	{
		cin >> n;
		memset(cnt,0,sizeof(cnt));
		for(int i = 1;i <= n;i ++)
		{
			string s;
			cin >> s;
			for(int j = s.size() - 1;j >= 0;j --)
			{
				if(s[j] == '0')
				{
					cnt[i] ++;
				}
				else
					break;
			}
		}

		int sum = 0;
		for(int i = 1;i <= n;i ++)
		{
			if(cnt[i] < n - i)
			{
				int pos;
				for(pos = i + 1;pos <= n;pos ++)
					if(cnt[pos] >= n - i)
						break;
				int cur = cnt[pos];
				for(int j = pos;j >= i + 1;j --)
					cnt[j] = cnt[j - 1];
				cnt[i] = cur;
				sum += pos - i;
			}
		}
				
				

	    fprintf(fp,"Case #%d: %d\n",r,sum);
		r ++;
		//cout << "Case #"<< r ++ <<": "; 
		cout << sum << endl;
	}



	return 0;
}