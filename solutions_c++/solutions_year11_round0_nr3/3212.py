// GCJ_2011_1.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

int max(int a, int b)
{
	return a>b?a:b;
}

int allot(int i,int nmax,int * belongsto,int* candies)
{
	if(i==nmax)
	{
		int wsum0,wsum1,sum0,sum1;
		wsum0=wsum1=sum0=sum1=0;
		for(int j=0;j<nmax;j++)
		{
			if(belongsto[j]==0) {wsum0 ^= candies[j]; sum0 += candies[j]; }
			if(belongsto[j]==1) {wsum1 ^= candies[j]; sum1 += candies[j]; }

		}
			if((wsum0 == wsum1) && sum0 && sum1) return max(sum0,sum1);
			else return -1;
	}
	else
	{
		
		int case1;
		belongsto[i]=0;
		case1=allot(i+1,nmax,belongsto,candies);
		if(i!=0)
		{
		 int case2;
		 belongsto[i]=1;
		 case2=allot(i+1,nmax,belongsto,candies);
		 case1 = max(case2,case1);
		}
		return case1;
	}

}
void givehim()
{
	int i,n_candies,candies[1000];
	int belongsto[1000];
	cin>>n_candies;
	for(int i=0;i<n_candies;i++) cin>>candies[i];
	int solun=allot(0,n_candies,belongsto,candies);
	if(solun==-1)
		cout<<"NO";
	else cout<<solun;
	cout<<"\n";

}


int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		givehim();
		//<<getmintime2()<<"\n";
	}
	return 0;
}

