#include <iostream>
#include<stdio.h>
#include<set>
#include<map>
#include<cstring>
using namespace std;
int A[1001];
bool Z[1001]={0};
bool Z2[1001]={0};
double W[1001]={0};
long long F[1001]={0};
double fact(int n)
{
	if(n<=1)return 1;
	if(F[n])return F[n];
	return F[n]=min(fact(n-1)*((double)(n)),(double)(1LL<<50));
}
double w(int n)
{
	if(n==2)return 0.5;
	if(n<2)return 0;
	if(Z2[n])return W[n];
	
	Z2[n]=1;
	return W[n]=(n-1)*(w(n-1)+w(n-2)/(double)(n-1))/(double)n;
}
double E[1001];
double dp(int n)
{
	if(n==2)return 2;
	if(n<2)return 0;
	if(Z[n])return E[n];
	double sum=0;
	for(int k=2;k<n;k++)
	{
		double s=dp(k)*w(k);
		s/=fact(n-k);
		sum+=s;
		//cout<<s<<"."<<endl;
		
	}
	Z[n]=1;
	return E[n]=(sum+1)/(1.0-w(n));
}
int main (int argc, char * const argv[]) {
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	double temp=0;
	for(int k=0;k<5;k++)
	{
		temp+=w(k)*fact(5)/(fact(k-5));
	}
	//cout<<temp;
	//cout<<w(4)<<endl;
	int t;
	cin>>t;
	for(int caso=1;caso<=t;caso++)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>A[i];
			A[i]--;
			Z[i]=0;
		}
		
		int cont=0;
		for(int i=0;i<n;i++)if(i!=A[i])cont++;
		//cout<<cont<<endl;
		cout<<"Case #"<<caso<<": ";
		printf("%.7lf",dp(cont));
		cout<<endl;
		
	}
    return 0;
}
