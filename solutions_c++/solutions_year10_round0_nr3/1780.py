#include <iostream>
#include<fstream>
using namespace std;
long long min(long long a,long long b)
{
	if(a<=b)
	{
		return a;
	}
	else
	{
		return b;
	}
}
long long next(long long a,long long n)
{
	if(a<n-1)
	{
		a++;
	}
	else
	{
		a=0;
	}
	return a;

}
long long back(long long a,long long  n)
{
	if(a==0)
	{
		a=n-1;
	}
	else
	{
		a--;
	}
	return a;
}
int main()
{
	ifstream cin("d.in");
	ofstream cout("d.out");
	int t;
	long long r;
	long long k;
	long long n;
	long long g[1005];
	long long sum;
	long long max;
	long long rec;
	long long i,j,a,b,c;
	long long arrive[1005];
	long long con[1005];
	long long p;
	long long beforeRec;
	long long startRec;
	long long result;
	int jump;

	cin>>t;
	for(i=0;i<t;i++)
	{
		sum=0;
		max=0;
		result=0;

		cin>>r>>k>>n;
		for(j=0;j<n;j++)
		{
			cin>>g[j];
			max+=g[j];
			arrive[j]=-1;
			con[j]=-1;
		}

		//�����λ��a��ʼ�����Ե��ĵط��Լ�����ʱ���������������п��Եõ�ѭ����

		a=0;
		
		while(true)
		{
			sum=0;
			if(arrive[a]!=-1)
			{
				break;
			}
			//for(p=a;;p++)
			p=a;
			while(sum+g[p]<=k)
			{
				if(sum>max)
				{
					break;
				}
				sum+=g[p];
				p=next(p,n);

				
			}
			arrive[a]=back(p,n);
			con[a]=min(sum,max);
			a=p;
		}
		b=0;
		for(c=0;c<r;c++)
		{
			result+=con[b];
			b=next(arrive[b],n);
		}
		

		/*startRec=a;//startRec�д�ſ�ʼѭ����λ��
		beforeRec=0;
		for(b=0;b<startRec;b++)
		{
			beforeRec+=g[b];
		}
		//����ѭ���ĳ��ȣ���λ��strRec��ʼ������������arrive�������е���������
		rec=0;
		c=startRec;
		jump=0;
		while(true)
		{
			rec+=g[c];
			c=next(c,n);

			if(c==startRec)
			{
				jump++;
			}
			if(jump==2)
			{
				break;
			}
			
		}

		if(r=1)
		{
			result=beforeRec;
		}
		else
		{
			result=beforeRec+(r-1)*rec;
		}*/
		cout<<"Case #"<<i+1<<": "<<result<<endl;

	}

}