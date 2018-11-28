#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int generatenextnumber(int number,int bitnumber)
{
	int result=number/10;
	int remain=number%10;
	return (int)(remain*pow(10.0,bitnumber-1))+result;
}

int getbitnumber(int number)
{
	int bitnumber=1;
	int tocompare=10;
	for(bitnumber=1;bitnumber<10;bitnumber++)
	{
		if(tocompare>number)
			break;
		tocompare*=10;
	}
	return bitnumber;
}

int main(int argc,char * argv[])
{
	int casenumber;
	int low,high;
	int number;
	int tempnumber;
	int bitnumber;
	int temp1,temp2;
	char * tocheck=new char[3000000];
	ifstream infile("C-large.in");
	ofstream outfile("result.txt");
	string readresult;
	if(infile&&outfile)
	{
		infile>>casenumber;
		for(int j=0;j<casenumber;j++)
		{
			infile>>low>>high;
			number=0;
			memset(tocheck,0,3000000);
			for(int i=high;i>=low;i--)
			{
				if(tocheck[i]==0)
				{
					tempnumber=1;
					bitnumber=getbitnumber(i);
					temp1=i;
					tocheck[temp1]=1;
					for(int k=1;k<bitnumber;k++)
					{
						temp2=generatenextnumber(temp1,bitnumber);
						if(temp2>=low&&temp2<=high&&tocheck[temp2]==0&&getbitnumber(temp2)==bitnumber)
						{
							tempnumber++;
							tocheck[temp2]=1;
						}
						temp1=temp2;
					}
					if(tempnumber>=2)
						number+=tempnumber*(tempnumber-1)/2;
				}
			}
			outfile<<"Case #"<<j+1<<": "<<number<<endl;
		}
		infile.close();
		outfile.close();
	}
	return 0;
}
