// ProblemaB.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <set>
#include <stdio.h>

using namespace std;

typedef long long int64;

string Next(string N)
{
	int count['9'+1];
	memset(count,0,sizeof(count));
	//find changeing place
	char actual='0';
	int p=N.length()-1;
	while (true)
	{
		if (p==-1)
		{
			break;
		}
		count[N[p]]++;
		if (N[p]<actual)
		{
			break;
		}
		actual=N[p];
		p--;
	}
	if (p<0)
	{
		//need to add a 0
		count['0']++;
		N="";
		//find first non zero digit
		for (char c='1';c<='9';c++)
		{
			if (count[c]>0)
			{
				N=N+c;
				count[c]--;
				break;
			}
		}
		//append all the digits
		for (char c='0';c<='9';c++)
		{
			while (count[c]>0)
			{
				count[c]--;
				N=N+c;
			}
		}
	}
	else
	{
		actual=N[p];
		N=N.substr(0,p);
		//find first greater than actual
		for (char c=actual+1;c<='9';c++)
		{
			if (count[c]>0)
			{
				N=N+c;
				count[c]--;
				break;
			}
		}
		//append all the digits
		for (char c='0';c<='9';c++)
		{
			while (count[c]>0)
			{
				count[c]--;
				N=N+c;
			}
		}
	}
	return N;
}

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	int T;
	fscanf(entrada,"%d",&T);
	for (int t=1;t<=T;t++)
	{
		char N[1000];
		char c;
		fscanf(entrada,"%s%c",N,&c);
		fprintf(salida,"Case #%d: %s\n",t,Next(N).c_str());
	}

	fclose(entrada);
	fclose(salida);
	return 0;
}
