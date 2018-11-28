#include <stdio.h>
#include <iostream>
#include <fstream>
#include<math.h>
#include<string.h>
using namespace std;
void swap(char &a,char &b)
{
	char temp;
	temp = a;
	a=b;
	b=temp;
	//cout<<" swapping ";
}
string sort(string str3)
{
	int len,pos;
	char min;
	len = str3.length();
	for (int i=0;i<len ;i++ )
	{
		min = str3[i];
		pos = i;
		for (int j=i;j<len ;j++ )
		{
			if (str3[j]<str3[pos])
			{
				pos = j;
			}
		}
		swap(str3[i],str3[pos]);
	}
	return str3;
}
int distinct(string str,int *arr)
{
	int len,base = 1;
	str = sort(str);
	len = str.length();
	arr[0] = 0;
	for (int i=0;i<len-1 ;i++ )
	{
		if (str[i]!=str[i+1])
		{
			base++;
			arr[i+1] = arr[i]+1;
		}
		else
			arr[i+1] = arr[i];
	}
	return base;
}
int main(int argc, char *argv[])
{
	printf("Hello, world\n");
	string str;
	int base=1,T,arr[10],len;
	bool flag=0;
	long long number;
	ofstream outfile;
	outfile.open("A-small34.out");
	ifstream infile;
	infile.open("A-small-1234.in");
	infile>>T;
	for (int m=1;m<=T ;m++ )
	{
		number = 0;
		infile>>str;
		len = str.length();
		arr[0] = 0; base =0;
		for (int i=1;i<len ;i++ )
		{
			flag = 0;
			for (int j=i-1;j>=0 ;j-- )
			{
				if (str[i]==str[j])
				{
					arr[i]=arr[j];
					flag =1;
					break;
				}
			}
			if (flag ==0)
			{
				arr[i]=++base;
			}

			
		}
		for (int k=0;k<len ;k++ )
			{
				if (arr[k]==0)
				{
					arr[k]=1;
				}
				else if (arr[k]==1)
				{
					arr[k]=0;
				}
			}
			if (base ==0)
				base++;
			for (int i=0;i<len ;i++ )
			{
				number = long(pow(base+1,len-1-i)+0.5)*arr[i]+number;
			}
		outfile<<"Case #"<<m<<": "<<number<< " " <<endl;
			
	}
		return 0;
}
