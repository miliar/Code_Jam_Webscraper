
#include "stdafx.h"
#include<algorithm>
#include<map>
#include<set>
#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
long long process(string );
long long power(long long ,long long );
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}
long long process(string word)
{
	int number[100];
	
	int pointer;
	char alpha;
	memset(number,-1,sizeof(number));
	
		
		alpha=word[0];
		number[0]=1;
		int save=700;
		bool flag=true;
		for(int l=1;l<word.length();l++)
		{
			if(word[l]!=alpha&&flag)
			{
				save=l;
				flag=false;
			}
			if(word[l]==alpha)
                 number[l]=1;

		}
	
		if(save<word.length()&&save>-1)
		{
		number[save]=0;
		alpha=word[save];
		for(int m=save+1;m<word.length();m++)
		{
			if(word[m]==alpha)
                 number[m]=0;

		}
		}
	
		
	long long count=2;
	
	for(int j=0;j<word.length();j++)
	{
		if(number[j]==-1)
		{
		alpha=word[j];
		number[j]=count;
		for(int l=j+1;l<word.length();l++)
		{
			if(word[l]==alpha)
                 number[l]=count;

		}
		count++;
		}
	}
	long long sum=0;
	
   for(long long k=0;k<word.length();k++)
   {
      sum=sum+number[word.length()-k-1]*power(count,k);
   }

return sum;



}
long long power(long long x,long long y)
{
	long long num=1;
	for(int i=0;i<y;i++)
        num=num*x;
	return num;
}





void main()
{

	ifstream cin("1.txt");
   ofstream cout("2.txt");
    int cases;
	string word;
	cin>>cases;
	for(int i=0;i<cases;i++)
	{
         cin>>word;
		 
		 cout<<"Case #"<<i+1<<": ";
		 cout<<process(word)<<endl;
	}




}