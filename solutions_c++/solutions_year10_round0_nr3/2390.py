//VC++ 2008
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>

using namespace std;

long toInteger(string s)
{
	int len = s.length();
	long result = 0;
	for(int i = 0;i < len;i++)
	{
		result *= 10;
		result += s[i] - '0';
	}
	return result;
}

int main()
{
	FILE* inf;
	FILE* outf;
	inf = fopen("E:\\C-small-attempt0.in","r");
	outf = fopen("E:\\C-small-attempt0.out","w+");
	char rs[20];

	string trkng;
	long t,r,k,n;
	long g[1005];
	long long sum[1005];
	long next[1005];
	char c;
	set<long> all;
	long begin;
	long count;
	long long result;

	if(inf != NULL && outf != NULL)
	{
		while(c = fgetc(inf),c != '\n')
		{
			trkng += c;
		}
		t = toInteger(trkng);
		trkng = "";

		for(long i = 0;i < t;i++)
		{
			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				trkng += c;
			}
			r = toInteger(trkng);
			trkng= "";

			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				trkng += c;
			}
			k = toInteger(trkng);
			trkng = "";

			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				trkng += c;
			}
			n = toInteger(trkng);
			trkng = "";

			for(long j = 0;j < n;j++)
			{
				while(c = fgetc(inf),c >= '0' && c <= '9')
				{
					trkng += c;
				}
				g[j] = toInteger(trkng);
				trkng = "";
			}

			begin = 0;
			all.clear();
			
			while(all.find(begin) == all.end())
			{
				sum[begin] = g[begin];
				next[begin] = begin;
				count = (begin + 1) % n;
				all.insert(begin);
				while(count != begin)
				{
					sum[begin] += g[count];
					if(sum[begin] > k)
					{
						sum[begin] -= g[count];
						next[begin] = count;
						begin = count;
						break;
					}
					else
					{
						count = (count + 1) % n;
					}
				}
			}

			result = 0;
			count = 0;
			for(long j = 0;j < r;j++)
			{
				result += sum[count];
				count = next[count];
			}

			sprintf(rs,"Case #%d: %lld\n",i + 1,result);

			fputs(rs,outf);

		}


		fclose(inf);
		fclose(outf);
	}
	return 0;
}