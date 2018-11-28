#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<map>
using namespace std;

void solve(int t)
{
int N,L,H;
int f[100];
cin>>N>>L>>H;
int i;
for(i=0;i<N;i++)
cin>>f[i];

int j;
for(i=L;i<=H;i++)
{
for(j=0;j<N;j++)
{
	if(i%f[j]&&f[j]%i)
		break;
}
if(j==N)break;
}

cout<<"Case #"<<t<<": ";
if(i==H+1)
cout<<"NO";
else
cout <<i;
cout<<endl;
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
