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

long calSum(long l,long p,long c)
{
	long res = 0;
	while(l < p)
	{
		l *= c;
		res++;
	}
	return res;
}

long calAns(long sum)
{
	long ans = 0;
	while(sum != 1)
	{
		if(sum % 2 != 0)
			sum += 1;
		sum /= 2;
		ans++;
	}
	return ans;
}

int main()
{
	FILE* inf;
	FILE* outf;
	inf = fopen("E:\\B-small-attempt0.in","r");
	outf = fopen("E:\\B-small-attempt0.out","w+");
	char rs[20];
	char c;

	string tempStr = "";
	long t,l,p,cc;
	long result;
	long sum;


	if(inf != NULL && outf != NULL)
	{
		while(c = fgetc(inf),c != '\n')
		{
			tempStr += c;
		}
		t = toInteger(tempStr);
		tempStr = "";

		for(long i = 0;i < t;i++)
		{
			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				tempStr += c;
			}
			l = toInteger(tempStr);
			tempStr= "";

			result = 0;

			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				tempStr += c;
			}
			p = toInteger(tempStr);
			tempStr = "";


			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				tempStr += c;
			}
			cc = toInteger(tempStr);
			tempStr = "";

			sum = calSum(l,p,cc);
			result = calAns(sum);

			sprintf(rs,"Case #%ld: %ld\n",i + 1,result);

			fputs(rs,outf);

		}


		fclose(inf);
		fclose(outf);
	}
	return 0;
}