#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <string>
#include <cmath>

#define ll long long

using namespace std;

long long n,i,j,k,rag,rag1,l,d,t,sum,sum1;
vector <long long> divisors;
int a[60][60],b[60][60],c[60][60];

void clear(){
	int i,j;
	for (i=0;i<k;i++)
		for (j=0;j<k;j++)
			c[i][j]=0;
}

void solve(long long n){
	int i,j;
	if (n==1){
		for (i=0;i<k;i++)
			for (j=0;j<k;j++)
				b[i][j]=a[i][j];
	} else
	
	{
		solve(n/2);
		clear();
		for (i=0;i<k;i++)
			for (j=0;j<k;j++)
				for (l=0;l<k;l++)
					c[i][j]+=b[i][l]*b[l][j];
		if (n%2==1){
			int d[60][60];
			for (i=0;i<k;i++)
				for (j=0;j<k;j++)
					d[i][j]=0;
			for (i=0;i<k;i++)
				for (j=0;j<k;j++)
					for (l=0;l<k;l++)
						d[i][j]+=c[i][l]*a[l][j];
			for (i=0;i<k;i++)
				for (j=0;j<k;j++)
					c[i][j]=d[i][j];
		}
		for (i=0;i<k;i++)
			for (j=0;j<k;j++){
				c[i][j]=c[i][j]%2;
				b[i][j]=c[i][j];
			}
	}
}

int identity(){
	int i,j;
	for (i=0;i<k;i++)
		for (j=0;j<k;j++)
			if (i==j && c[i][j]!=1) return 0; else
				if (i!=j && c[i][j]==1) return 0;
	return 1;
}

string s;

int main(){
	freopen("c:\\input.txt","r",stdin);
	freopen("c:\\output.txt","w",stdout);
	cin>>t;
	for (int ii=1;ii<=t;ii++){
		cin>>s;
		sum=0;
		vector <int> roja;
		for(i=0;i<s.size();i++)
			if (s[i]=='?')
				roja.push_back(i); else
				if (s[i]=='1') sum+=1ll<<(s.size()-i-1);
		k=roja.size();
		n=s.size();
		for (i=0;i<(1ll<<k);i++){
			sum1=sum;
			for (j=0;j<k;j++)
				if ((i&(1ll<<j))>0){
					sum1+=(1ll<<(n-roja[j]-1));
				}
			long long sqr=(long long)sqrt(1.0*sum1+0.001);
			if (sqr*sqr==sum1){
				for (j=0;j<k;j++)
					if ((i&(1ll<<j))>0)
						s[roja[j]]='1'; else
						s[roja[j]]='0';
				break;
			}
		}
		cout<<"Case #"<<ii<<": "<<s<<endl;
	}
	
	return 0;
}