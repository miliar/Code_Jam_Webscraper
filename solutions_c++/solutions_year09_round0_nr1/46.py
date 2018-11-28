#include<iostream>
#include<cstdio>
using namespace std;

const int MaxL = 15;
const int MaxD = 5000;
char dic[MaxD][MaxL+1];
char buf[1000];
int main()
{
	int cases=0;
	int l,d,n;
	cin>>l>>d>>n;
	for(int i=0;i<d;i++)
		cin>>dic[i];
	for(;cin>>buf;)
	{
		int sum = 0;
		for(int i=0;i<d;i++)
		{
			bool flag = true;
			for(int j=0,k=0;flag && j<l && buf[k];j++,k++)
				if(buf[k] == '(')
				{
					for(flag=false,k++;buf[k]!=')';k++)
						flag |= buf[k] == dic[i][j];
				}
				else
					flag = buf[k] == dic[i][j];
			if(flag) sum++;
		}
		cout<<"Case #"<<++cases<<": "<<sum<<endl;
	}
	return 0;
}
