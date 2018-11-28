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
	inf = fopen("E:\\A-large.in","r");
	outf = fopen("E:\\A-large.out","w+");
	char rs[20];
	char c;

	string tempStr = "";
	long t,n;
	long result;
	long allA[1005];
	long allB[1005];


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
			n = toInteger(tempStr);
			tempStr= "";

			result = 0;

			for(long j = 0;j < n;j++)
			{
				while(c = fgetc(inf),c >= '0' && c <= '9')
				{
					tempStr += c;
				}
				allA[j] = toInteger(tempStr);
				tempStr = "";


				while(c = fgetc(inf),c >= '0' && c <= '9')
				{
					tempStr += c;
				}
				allB[j] = toInteger(tempStr);
				tempStr = "";

				for(long k = 0;k < j;k++)
				{
					if((allA[j] < allA[k] && allB[j] > allB[k]) || (allA[j] > allA[k] && allB[j] < allB[k]))
						result++;
				}
			}

			sprintf(rs,"Case #%ld: %ld\n",i + 1,result);

			fputs(rs,outf);

		}


		fclose(inf);
		fclose(outf);
	}
	return 0;
}