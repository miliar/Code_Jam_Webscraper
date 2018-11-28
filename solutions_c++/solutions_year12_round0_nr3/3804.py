
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <cmath>
//#include <map>
#include <hash_map>
//using namespace stdext;
using namespace std;

namespace std{
    using namespace __gnu_cxx;
}
int len;
int bits[10];//low to  high bit
int power[10]={1,10,100,1000,10000,100000};

class ClassA{
public:
	ClassA(int n1,int m1):n(n1),m(m1){}
public:
	int n,m;
};

struct hash_A
{
	size_t operator()(const class ClassA & a)const
	{
		return a.n * a.m;
	}
};
struct equal_A
{
    bool operator()(const class ClassA & a1, const class ClassA & a2)const
	{
		return  (a1.n==a2.n) && (a1.m==a2.m);
	}
};


void Preprocess(int n)
{
	len=0;
	while(n!=0)
	{
		len++;
		bits[len]=n%10;
		n/=10;
	}
}
void Solve(int A,int B,int t)
{
	int cnt=0;
	hash_map<ClassA, int,hash_A,equal_A> mymap;
	for(int n=A;n<B;n++)
	{
		Preprocess(n);//store bits,and compute len
		for(int i=len-1;i>=1;i--)
		{
			if(bits[i]>=bits[len])
			{
				int m=n%((int)(pow(10.0,i)));
				m*=(int)pow(10.0,len-i);
				m+=n/pow(10.0,i);
				int flag=mymap[ClassA(n,m)];
				if(m>n && m <= B && !flag)
				{
					mymap[ClassA(n,m)]=2;
					//printf("%d %d\n",n,m);
					cnt++;
				}
			}
		}
	}
	printf("Case #%d: %d\n",t,cnt);
}

int main(int argc, char* argv[])
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    //freopen("C-small-attempt0.out","w",stdout);
	int T,A,B;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d",&A,&B);
		Solve(A,B,i);
	}
	//
	return 0;
}

