#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream in("C-large.in");
ofstream out("C-large.out");


int T;

long long flag[1004];
long long d[1004];
int a[1004];

int r,k,n;
long long sum;

int main()
{
	in >> T;
	for(int cnt = 1;cnt <= T;cnt ++)
	{
		out << "Case #"<<cnt<<": ";
		sum = 0;
		in >> r >> k >> n;
		for(int i = 0;i < n;i ++)
			in >> d[i];


		int pos = 0;
		memset(flag,0,sizeof(flag));
		memset(a,-1,sizeof(a));
		for(int i = 0;i <= n;i ++)
		{
			long long temp = 0;
			int j;
			for(j = 0;j < n;j ++)
			{
				int tmp = (pos + j) % n;
				if(temp + d[tmp] <= k)
					temp += d[tmp];
				else
				{
					flag[pos] = temp;
					a[pos] = tmp;
					pos = tmp;
					break;
				}
			}
			if(j == n)
			{
				flag[pos] = temp;
				a[pos] = pos;
			}
			
			sum += temp;
			r --;
			if(r <= 0)
				break;
			if(a[pos] != -1)
			{
				break;
			}
		} 
		if(r <= 0)
		{
			out << sum << endl;
			continue;
		}
		long long temp = flag[pos];
		int tmp = pos;
		int count = 1;
		while(a[tmp] != pos)
		{
			count ++;
			temp += flag[a[tmp]];
			tmp = a[tmp];
		}

		sum += ((long long)r) / count * temp;

		count = r % count;
		tmp = pos;
		while(count > 0)
		{
			sum += flag[tmp];
			count --;
			tmp = a[tmp];
		}
		out << sum << endl;
	}
		

	return 0;
}

