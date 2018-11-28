#include<iostream>
#include<fstream>
#include<conio.h>
//#include<inttypes.h>
#include<iomanip>
#include<assert.h>
#include<ctype.h>
#include<errno.h>
#include<float.h>
#include<limits.h>
#include<locale.h>
#include<math.h>
#include<string.h>
#include<stdarg.h>
#include<stddef.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<wchar.h>
#include<wctype.h>
#include<queue>
#include<vector>
#include<list>
//#include<E:\gcj\header\BigInt\BigInt.h>
//#include<E:\gcj\header\BigInt\BigInt.cpp>
#define bigint CBigInt
#define max(a,b) a>b?a:b
#define min(x,y) x>y?y:x
//#include<E:\gcj\header\ritwik.H>
using namespace std;	
/*long long int smooth(int *a,int n,int k,int d,int i,int m)
{
	int j,x;
	long long int ans=0;
	if(k==1)
		return 0;
	else
	{
		ans=smooth(a,n,k-1,d,i,m);
		if(abs(a[k-1]-a[k])<=m)
		{
			return ans;
		}
		else
		{

		}
	}
}*/
/*class CPolygon {
  private:
    int width, height;
  public:
    void set_values (int a, int b)
      { width=a; height=b;}
  };

class CRectangle: public CPolygon {
  public:
    int area ()
      { return (width * height); }
  };

class CTriangle: public CPolygon {
  public:
    int area ()
      { return (width * height / 2); }
  };*/
int valid(long long int n)
{
	char str[10];
	int i=0;
	while(n!=0)
	{
		str[i++]=n%10+'0';
		n/=10;
	}
	str[i]='\0';
	for(i=0;i<strlen(str)-1;i++)
	{
		if(str[i]<str[i+1])
			return 0;
	}
	return 1;
}
int allsame(long long int n)
{
	int digit=n%10;
	while(n!=0)
	{
		if(n%10!=digit)
			return 0;
		n/=10;
	}
	return 1;
}
long long int cycle(long long int n,int l)
{
	int str[10],i,len,first,temp;
	long long int sum=0;
	i=0;
	while(n!=0)
	{
		str[i++]=n%10;
		n/=10;
	}
	len=i;
	while(l--)
	{
		first=str[0];
		for(i=0;i<len-1;i++)
			str[i]=str[i+1];
		str[len-1]=first;
	}
	for(i=0;i<len;i++)
	{
		sum+=str[i]*pow(10.0,i);
	}
	return sum;
}
int samedig(long long int n1,long long int n2)
{
	int l1,l2;
	l1=l2=0;
	while(n1!=0)
	{
		l1++;
		n1/=10;
	}
	while(n2!=0)
	{
		l2++;
		n2/=10;
	}
	if(l1==l2)	return 1;
	else	return 0;
}
void main()
{
	int test;
	//cout<<cycle(120,1);
	int a,b,i,j,binary,end,value,flag;
	long double k,key,ans,p[100000];
	long double prob[10000];
	ifstream fin("A-small-attempt1.in",ios::binary|ios::in);
	ofstream fout("outputAs1.out",ios::out);
	fin>>test;
	for(int t_c=0;t_c<test;t_c++)
	{
		fin>>a>>b;
		ans=0;
		for(i=0;i<a;i++)
			fin>>p[i];
		for(i=0;i<10000;i++)
			prob[i]=1;
		binary=0;
		end=pow(2.0,a);
		for(j=0;j<end;j++)
		{
			binary=j;
			for(i=0;i<a;i++)
			{
				if(binary%2==0)
				{
					prob[j]*=(1-p[i]);
				}
				else
				{
					prob[j]*=p[i];
				}
				binary/=2;
			}
		}
		//keep typing
		key=0;
		for(j=0;j<end-1;j++)
		{
			key+=prob[j]*(2*b-a+2);
		}
		key+=prob[j]*(b-a+1);
		ans=key;
		//cout<<key<<endl;
		//backspace
		for(int backspace=1;backspace<=a;backspace++)
		{
			key=k=0;
			k+=backspace;
			k+=(b-a+1+backspace);
			for(j=0;j<end;j++)
			{
				binary=j;
				value=a-backspace;
				flag=1;
				for(i=0;i<value;i++)
				{
					if(binary%2==0)
					{
						flag=0;
						break;
					}
					binary/=2;
				}
				if(flag==0)
					key+=prob[j]*(k+b+1);
				else
					key+=prob[j]*k;
			}
			//cout<<key<<endl;
			if(ans>key)
				ans=key;
		}
		//enter
		key=0;
		key+=2+b;
		//cout<<key<<endl;
		if(ans>key)
			ans=key;
		fout<<"Case #"<<t_c+1<<": "<<fixed<<setprecision(6)<<ans<<endl;
		cout<<"Case #"<<t_c+1<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}
	//cout<<sizeof(int)<<" "<<sizeof(long int)<<" "<<sizeof(long long int);
	fin.close();
	fout.close();
	/*CRectangle rect;
	CTriangle trgl;
	rect.set_values (4,5);
	trgl.set_values (4,5);
	cout << rect.area() << endl;
	cout << trgl.area() << endl;*/
	getch();
}
