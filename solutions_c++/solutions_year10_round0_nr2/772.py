#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<iomanip.h>
#include<math.h>

long int hcf(long int m1,long int m2)
{
if(m2==0)	return m1;
	long int rem;
	rem=m1%m2;
	while(rem!=0)
	{
		m1=m2;
		m2=rem;
		rem=m1%rem;
	}
	return m2;
}

void main()
{
	/*bigint b,c,a;
	//a.FromDec("44444444441117772233382993");
	b.FromString("3430000000008888888888888888888");
	c=a+b;
	printf("%s\n",c.Format());
	printf("%d\n",sizeof(a));
	int64_t sum,cost;*/
	int t,i,j,n;
	long int *num,*diff,h,r;
	ifstream fi("B-small-attempt1.in",ios::binary|ios::in);
	ofstream fo("outputB.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n;
		num=new long int[n];
		diff=new long int[n-1];
		for(i=0;i<n;i++)
			fi>>num[i];
		for(j=0;j<n-1;j++)
		{
			diff[j]=abs(num[j+1]-num[j]);	
		}
		for(i=0;i<n-2;i++)
		{
			if(diff[i]<diff[i+1])
			{
				diff[i+1]=hcf(diff[i+1],diff[i]);
			}
			else if(diff[i]>diff[i+1])
			{
				diff[i+1]=hcf(diff[i],diff[i+1]);
			}
		}
		h=diff[n-2];
		cout<<h<<endl;
		r=num[0]/h;
		if(num[0]%h==0)
			fo<<"Case #"<<(t_c+1)<<": "<<"0"<<endl;
		else
		{
			h=h*(r+1)-num[0];
			fo<<"Case #"<<(t_c+1)<<": "<<h<<endl;
		}
		cout<<t_c<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
