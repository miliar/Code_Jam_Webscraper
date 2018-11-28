#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <valarray>
#include <bitset>
#include <iostream>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
long long saca1(vector <long long> v1,vector <long long> v2)
{	long long cont=0;
	for(long long i=0;i<v1.size();i++)
	{
		if(v1[i]%3==0&&v2[i]%3==0)
			cont++;
	}
return cont;
}
bool es(long long x1,long long x2,long long x3,long long y1,long long y2,long long y3)
{
	if((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0)
		return true;
	return false;

}
void ingresa(long long X, long long Y,vector <long long> &v1,vector <long long> &v2)

{
	for(long long i=0;i<v1.size();i++ )
	{
		if(v1[i]==X&&v2[i]==Y)
			return;
	}
	v1.push_back(X);
	v2.push_back(Y);
	return ;
}
int main()
{
int sal=1;
int N;
cin>>N;
//falta el numero d casos
while(N)
{
	long long n, A, B, C, D, x0, y0,M;
	cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
	vector <long long> v1;
	vector <long long> v2;
	long long X=x0,Y=y0;
	v1.push_back(X);
	v2.push_back(Y);
	for(long long i=1;i<=n-1;i++)
	{
		X=(A * X + B)%M;
		Y = (C * Y + D)%M;
		ingresa(X,Y,v1,v2);
	}
	long long num=0;
	//num=saca1(v1,v2);
	
	for(long long i=0;i<v1.size()-2;i++)
	{
		for(long long j=i+1;j<v1.size()-1;j++)
		{
			for(long long k=j+1;k<v1.size();k++)
			if(es(v1[i],v1[j],v1[k],v2[i],v2[j],v2[k]))
				num++;
		
		}
	
	
	}




//falta la salida
cout<<"Case #"<<sal<<": "<<num<<endl;
sal++;
N--;
}
//system("pause");



return 0;
}

