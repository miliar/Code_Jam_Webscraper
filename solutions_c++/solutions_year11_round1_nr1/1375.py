#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#pragma comment(linker, "/STACK:167772160")
typedef long long int64;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define PB push_back 
#define MP make_pair
using namespace std;
string s1,s2;
int tes,o,n,p1,p2,j,d;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tes;
	s1="Possible";
	s2="Broken";
	for(o=1;o<=tes;o++)
	{
		cin>>n>>p1>>p2;

		if(p1==0)j=0;else
		for(j=1;j<=n;j++)if((p1>0 && (100*j)%p1==0) || j>100)break;
		
		string is=s1;
		if(j>100 || j>n)is=s2;
		if(p1>0 && (100*j)/p1>n)is=s2;
		if(p1!=0 && p2==0)is=s2;
		if(p1!=100 && p2==100)is=s2;

		cout<<"Case #"<<o<<": "<<is<<endl;
	}
}