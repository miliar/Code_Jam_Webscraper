#include"vector"
#include"stdio.h"
#include"iostream"
#include"algorithm"
#include"list"
#include"string"
#include"map"
#include<math.h>

using namespace std;

long basetodec(long long base,int n)
{
	long var=0,j=0;
	for(long long i=base;i>0;)
	{
		var+=(i%10)*(long)pow((double)n,(int)j);
		j++;
		i=i/10;
	}
	return var;
}
int main()
{
    int n,m;
	cin>>n;
	m=n;
	while(n--)
	{
		char arr[256],cnt=0,base=2;
		memset(arr,0,255);
		string str,str1;
		char num[256];
		memset(num,0,255);
		cin>>str;
		str1=str;
		for(int i=0;i<str.size();i++)
		{
			if(arr[str[i]]==0)
			{
				cnt++;
				if(cnt==2)
				{arr[str[i]]='0';continue;}
				if(cnt>2)
					arr[str[i]]=cnt+'0'-1;
				else
				 arr[str[i]]=cnt+'0';
			}
		}
		if(cnt==1)
		{
			memset(num,'1',str.size());
			base=2;
		}
		else
		{
			for(int i=0;i<str.size();i++)
			{
				num[i]=arr[str[i]];
			}
			base=cnt;
		}
		long long num1=atoi(num);
		//cout<<num1<<endl;
		cout<<"Case #"<<m-n<<": "<<basetodec(num1,base)<<endl;

	}
	return 0;
}
