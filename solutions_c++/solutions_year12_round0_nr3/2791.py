#include<iostream>
#include<cmath>
using namespace std;


int main()
{
	long a,b,n,r[50];
	cin>>n;
	for(int i=0;i<n;i++)
	{r[i]=0;
		cin>>a>>b;
		int d=0;
		for(int j=a;j>0;j/=10,d++);
		if(d>1)
		{ long j2;
		  for(long j=a;j<b;j++)
		  { long c[]={0,0,0,0,0,0,0};
			for(int k=1;k<d;k++)
			{
				long last=j%((long)pow(10,k));
				if(last/(pow(10,k-1)!=0))
				{ j2=last*pow(10,d-k)+j/(pow(10,k));
				if(j2>j&&j2<=b)
				{ int f=0,l=0;
				for(;c[l]!=0;l++)
				{ if(j2==c[l]) {f=1; break;}}
				if(!f)
				{c[l]=j2;	r[i]++; }}}
			}
		  }
		}
	}
	for(int i=0;i<n;i++)
	                cout<<"Case #"<<i+1<<": "<<r[i]<<endl;

}
