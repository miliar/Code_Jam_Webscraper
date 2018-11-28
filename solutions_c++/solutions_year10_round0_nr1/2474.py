//VC++ 2008
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<math.h>
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
	inf = fopen("E:\\A-large.in","r");
	outf = fopen("E:\\A-large.out","w+");
	char rs[20];

	string tnk;
	long t,n,k;
	long base;
	char c;

	if(inf != NULL && outf != NULL)
	{
		while(c = fgetc(inf),c != '\n')
		{
			tnk += c;
		}
		t = toInteger(tnk);
		tnk = "";

		for(int i = 0;i < t;i++)
		{
			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				tnk += c;
			}
			n = toInteger(tnk);
			tnk = "";
			base = long(pow(double(2),double(n)));

			while(c = fgetc(inf),c >= '0' && c <= '9')
			{
				tnk += c;
			}
			k = toInteger(tnk);
			tnk = "";

			k += 1;
			if(k % base == 0)
			{
				sprintf(rs,"Case #%d: ON\n",i + 1);
			}
			else
			{
				sprintf(rs,"Case #%d: OFF\n",i + 1);
			}

			
			fputs(rs,outf);

		}
		

		fclose(inf);
		fclose(outf);
	}
	return 0;
}