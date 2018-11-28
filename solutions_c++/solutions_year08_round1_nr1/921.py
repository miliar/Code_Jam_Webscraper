#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define ROW 800


ifstream fp_in;


class vec
{
private:
	int v1[ROW];
	int v11[ROW];
	int v2[ROW];
	int v21[ROW];
	long sum1,sum2;
	int n;

public:
	void init()
	{
		for(int i=0;i<ROW;i++)
		{
			v1[i]=0;
			v11[i]=0;
			v2[i]=0;
			v21[i]=0;
			sum1=0;
			sum2=0;
			n=0;
		}
	}

	void input()
	{
		int i;
		fp_in>>n;
		char temp[2];
		fp_in.getline(temp,2,'\n');
		for(i=0;i<n;i++)
		{
			fp_in>>v1[i];
			v11[i]=v1[i];
		}
		fp_in.getline(temp,2,'\n');
		for(i=0;i<n;i++)
		{
			fp_in>>v2[i];
			v21[i]=v2[i];
		}
	}

	void sort()
	{
		int temp=0,i,j;
		for(i=0;i<n-1;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(v1[i]>v1[j])
				{
					temp=v1[i];
					v1[i]=v1[j];
					v1[j]=temp;
				}
				if(v2[i]>v2[j])
				{
					temp=v2[i];
					v2[i]=v2[j];
					v2[j]=temp;
				}
				if(v11[i]<v11[j])
				{
					temp=v11[i];
					v11[i]=v11[j];
					v11[j]=temp;
				}
				if(v21[i]<v2[j])
				{
					temp=v21[i];
					v21[i]=v21[j];
					v21[j]=temp;
				}
			}
		}
	}

	long calc()
	{
		for(int i=0;i<n;i++)
		{
			sum1=sum1+v1[i]*v21[i];
			sum2=sum2+v11[i]*v2[i];
		}
		if(sum1<sum2)
			return sum1;
		return sum2;
	}
};

void main()
{
	fstream fp_out;
	fp_out.open("vecotr_o.txt",ios::out,ios::in);
	int t,i;
	long sum;
	//location of input file (need this name only)
	fp_in.open("a.in");
	fp_in>>t;
	vec obj;
	for(i=0;i<t;i++)
	{
		obj.init();
		obj.input();
		obj.sort();
		sum=obj.calc();
		fp_out<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	fp_out.close();
	fp_in.close();
}