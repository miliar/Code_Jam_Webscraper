#include <iostream>
#include <fstream>
using namespace std;

int is(int value,int p)
{
	int ret = 0;
	int y = value/3;
	if(!y)
	{
		if(p)
		{
			if(3*y+1==value)
			{
				if(p<=y+1)
					return 2;
			}
			if(3*y+2==value)
			{
				if(p<=y+2)
					return 1;
			}
			return 0;
		}
		else
			return 2;
	}
	if(y==10)
	{
		return 2;
	}
	int x = y-1;

	if(3*x+3==value)
	{
		if(p<=(x+1))
			return 2;
		else if(p<=(x+2))
			return 1;
	}
	if(3*x+4==value)
	{
		if(p<=(x+2))
			return 2;
	}
	if(3*x+5==value)
	{
		if(p<=(x+2))
			return 2;
		else if(p<=(x+3))
			return 1;
	}
	return 0;
}
int isOver(int value,int p)
{
	int ret = 0;
	int y = value/3;
	if(!y)
	{
		if(p)
			return 0;
		else
			return 2;
	}
	int x = y-1;
	
	//
	int v1 = value-2*x;
	if(v1<(x+2)&&(v1>=p))
	{
		return 2;
	}
	else if(v1==(x+2)&&(v1>=p))
	{
		ret = 1;
	}
	//
	if(x+2<=10)
	{
		v1 = value-(2*x+1);
		if(v1<(x+2)&&(v1>=p))
		{
			return 2;
		}
		if(!ret)
		{
			if(v1==(x+2))
			{
				if(v1>=p)
					ret = 1;
			}
		}
	}
	//
	v1 = value-(2*x+2);
	if(!ret)
	{
		if(v1<=(x+2)&&((x+2)>=p))
			ret = 1;
	}
	//
	
	v1 = value-(2*x+2);
	if(v1<(x+3)&&(v1>=p))
	{
		return 2;
	}
	if(!ret)
	{
		if(v1==(x+3))
		{
			if(v1>=p)
				ret = 1;
		}
	}
	
	//
	if(x+2<=10)
	{
		v1 = value-(2*x+3);
		if(v1<(x+3)&&(v1>x)&&(v1>=p))
		{
			return 2;
		}
		if(!ret)
		{
			if(v1==(x+3)||(v1==x))
			{
				if(v1>=p||((x+2)>=p))
					ret = 1;
			}
		}
	}
	
	//
	if(x+2<=10)
	{
		v1 = value-(2*x+4);
		if((v1>x)&&(v1>=p))
		{
			return 2;
		}
		if(!ret)
		{
			if((v1==x))
			{
				if(((x+2)>=p))
					ret = 1;
			}
		}
	}
	return ret;


}

int main()
{
	int T,N,S,p;
	int tArr[100];
	int retArr[100];
	int sum1;
	int sum2;
	int sum;
	ifstream in("bi.txt");
	ofstream out("bo.txt");
	in>>T;
	int i=0;
	int j;
	for(;i<T;i++)
	{
		in>>N>>S>>p;
		sum1=0;sum2=0;
		for(j=0;j<N;j++)
		{
			in>>tArr[j];
			int tmp = is(tArr[j],p);
			if(2==tmp)
				sum2++;
			else if(1==tmp)
				sum1++;
			
			
		}
		if(S>=sum1)
				sum=sum1+sum2;
			else
			{
				sum=S+sum2;
			}
		out<<"Case #"<<i+1<<": "<<sum<<endl;

	}
	return 0;
}

