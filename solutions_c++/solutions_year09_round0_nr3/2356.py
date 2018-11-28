#include <iostream>
#include <fstream>
#include <string>
#include <cstring>


using namespace std;


ifstream fin;
ofstream fout;


long double compute(const char sig[],char buffer[600]);
const char sig[] = "welcome to code jam";
long double d = 0;


int main()
{
	fin.open("small2.in");
	fout.open("small2.out");

	char numbers[10];

	fin.getline(numbers,10);

	int N;

	sscanf(numbers,"%d",&N);
	char  buffer[600];

	for (int i = 0; i < N; i++)
	{
        d = 0;
	    fin.getline(buffer,600);
        long double result = compute(sig,buffer);
		int result1 = result;
		char digits[4];
		int i1 = result1 % 10;
		digits[3] = i1 + '0';
		int i2 = (result1 / 10) % 10;
		digits[2] = i2 + '0';
		int i3 = (result1 / 100) % 10;
		digits[1] = i3 + '0';
		int i4 = (result1 / 1000) % 10;
		digits[0] = i4 + '0';
		fout<<"Case #"<<(i+1)<<": "<<digits[0]<<digits[1]<<digits[2]<<digits[3]<<endl;
	}
}

long double  compute(const char sig[],char buffer[600])
{

	char *temp = buffer;

    if (*sig == '\0')
	{   d=d+1;
		return d;
	}
	if (*temp == '\0')
		return 0;

    
    while(*temp != '\0')
	{
		if (*temp == *sig)
		{
			compute(sig+1,temp+1);
		}
		temp++;
	}

	return d;


}


