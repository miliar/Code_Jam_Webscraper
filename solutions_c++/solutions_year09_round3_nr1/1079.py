#include<iostream>
#include<fstream>

using namespace std;

long ConvertL(char *, char *);
long Base(char *, long b, long size);

long main()
{
	long cases;
	char line[256];
	char conv[256];
	long b;

	ifstream file;
	ofstream file1;

	file.open("A-small-attempt1.in");
	file1.open("out.txt");
	

	file>>cases;
	file.getline(line,256,'\n');

	for(long i=0;i<cases;i++)
	{
		file.getline(line,256,'\n');
		
		b = ConvertL(line,conv);

		file1<<"Case #"<<i+1<<": "<<Base(conv,b,strlen(line))<<endl;

	}
	return 0;


}

long ConvertL(char * arr, char * conv)
{
	long s=0;
	long c=0;
	long n=1;

	char check[256];
	char num[256];

	bool chk=false;

	for(long i=0;i<strlen(arr);i++)
	{
		for(long j=0;j<s;j++)
		{
			if(arr[i]==check[j])
			{
				chk=true;
				conv[c]=num[j];
				c++;
				break;
			}

		}

		
		if(chk!=true)
		{
			check[s]=arr[i];
			num[s]=n+48;

			if(n==1)
			{
				n=0;
			}
			else
			if(n==0)
			{
				n=2;
			}
			else
			{
				n++;
			}

			

			conv[c]=num[s];
			s++;
			c++;
		}

		chk=false;
	}

	conv[c]='\n';

	return n;
}


long Base(char *arr, long b, long size)
{
	long sum=0;
	long bp=0;
	long cal=1;

	if(b<=1)
	{
		b=2;
	}

	for(long i=size-1;i>=0;i--)
	{
		for(long j=0;j<bp;j++)
		{
			cal = cal*b;
		}

		sum = sum + ((arr[i]-48)*cal);
		cal=1;
		bp++;
	}

	return sum;
}