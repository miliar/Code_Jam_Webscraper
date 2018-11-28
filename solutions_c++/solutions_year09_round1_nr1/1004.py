#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


int check[1000];

int ishappy(int num,int base)
{
	int tmpnum=num;
	int nextnum=0;
	int a;
	while(true)
	{
		nextnum=0;
		while(tmpnum)
		{
			a=tmpnum%base;
			nextnum+=a*a;
			tmpnum=tmpnum/base;
		}
		tmpnum=nextnum;
		if(nextnum==1)
		{
			return 1;
		}
		if(check[nextnum]==1)
		{
			return 0;
		}
		else
			check[nextnum]=1;
	}
}

int main(int argc,char** argv)
{
	ofstream out("..//output.txt");
	int result;
	int T;
	cin>>T;
	int base;
	vector<int> basevec;
	char inputbase;
	int m=1;
	int find=1;
	while(T)
	{
		basevec.clear();
		while(true)
		{
			cin>>base;
			inputbase=getchar();
			basevec.push_back(base);
			if(inputbase!=' ')break;
		}
		if(basevec.size()==1)
		{
			out<<"Case #"<<m<<": "<<basevec[0]<<endl;
		}
		for(int j=2;;j++)
		{
			for(int i=0;i<basevec.size();i++)
			{
				memset(check,0,sizeof(int)*1000);
				result=ishappy(j,basevec[i]);
				if(result==0)
					break;
			}
			if(result==1)
			{
				out<<"Case #"<<m<<": "<<j<<endl;
				break;
			}
		}
		m++;
		T--;
	}
	getchar();
	return 0;
}