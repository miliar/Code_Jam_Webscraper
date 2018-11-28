#include <iostream>
#include <cmath>
using namespace std;

int n;
int length;
char a[15];
int main()
{
	cin>>n;
	int ca=1;
	getchar();
	while(n--)
	{
		gets(a);
		long long int sum=0;
		length=strlen(a);
		if(length==1)
		{
			int nn=atoi(a);
			if(nn%2==0 || nn%3==0 || nn%5==0 || nn%7==0)
				sum=1;
		}else{
			int pos[14];
			int time=(int)pow(3.0, length-1);
			for(int i=0; i<time; i++)
			{
				int ss=i;
				for(int j=1; j<length; j++)
				{
					pos[j]=ss%3;
					ss=ss/3;
				}
				int start=1;
				pos[length]=-1;
				int end=0;
				int j=0;
				long long int sums=0;
				while(true)
				{
					long long int temp=0;
					while(pos[start]==0)
						start++;
					for( ; j<start; j++)
						temp=temp*10+(a[j]-'0');
					if(end==0)
						sums=temp;
					else if(end==1)
						sums+=temp;
					else if(end==2)
						sums-=temp;
					end=pos[start];

					if(end==-1)
						break;
					start++;
				}	
				if(sums%2==0 || sums%3==0 || sums%5==0 || sums%7==0)
					sum++;
			}
		}
		printf("Case #%d: %I64d\n", ca++, sum);
	}
	return 0;

}