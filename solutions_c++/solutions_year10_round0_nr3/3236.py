#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int main() {
	freopen("C-small.in","r",stdin);
	long t,to=0;
	cin>>t;
	while(t--)
	{
    to++;
	long r,k,n,ban;
	cin>>r>>k>>n;
	vector<long> v(n);
	for(long c=0;c<n;c++)
	cin>>v[c];

	long sum=0,don=0;

	for(long j=0;j<r;j++)
	{
    long aux=0,ban2=0;

    for(long c=don;c<n;c++)
    {
    ban2++;

    if(ban2>n){ban=2;break;}

    aux=aux+v[c];

    if(aux>k)
    {
        ban=1;
        aux=aux-v[c];
        don=c;
        sum=sum+aux;
        break;
    }

    if(c==n-1)c=-1;

    }

    if(ban==2){sum=aux*r;break;}

    }
	cout<<"Case #"<<to<<": "<<sum<<endl;
	}

}
