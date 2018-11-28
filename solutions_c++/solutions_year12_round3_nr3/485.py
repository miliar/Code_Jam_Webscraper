#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#define MAX 1100

long long int maxx;
long long int n,m;
long long int btype[MAX],ttype[MAX],bn[MAX],tn[MAX];

void f(long long int box,long long int boxleft,long long int toy,long long int toyleft,long long int sum)
{
	long long int nbox, nboxleft, ntoy, ntoyleft, nsum;
	if(box >= n) return;
	if(toy >= m) return;
	
	nbox = box;
	nboxleft = nboxleft;
	ntoy = toy;
	ntoyleft = toyleft;
	nsum = sum;
	
	//printf("start %d %d %d %d %d\n",box,boxleft,toy,toyleft,sum);
	//cout<<btype[box]<<" "<<ttype[toy]<<endl;
	
	if(btype[box]==ttype[toy])
	{	
		if( boxleft <= toyleft)
		{
			sum += boxleft;
			toyleft = toyleft - boxleft;
			boxleft = 0;
		}
		else
		{
			sum += toyleft;
			boxleft = boxleft - toyleft;
			toyleft = 0;
		}
		
		if(sum>maxx) maxx = sum;
		
		//cout<<"-------- type match "<<sum<<" "<<maxx<<" ------"<<endl;
		
		if(toyleft == 0)
		{
			toy++;
			if(toy < m) toyleft = tn[toy];
			else return;
		}
		
		if(boxleft == 0)
		{
			box++;
			if(box < n) boxleft = bn[box];
			else return;
		}
		
		f(box,boxleft,toy,toyleft,sum);
	}
	else
	{
		//cout<<"try next toy"<<endl;
		if( (toy+1) < m ) f(box,boxleft,toy+1,tn[toy+1],sum);
	}
	
	//cout<<"try next box"<<endl;
	if( (nbox+1) < n ) f(nbox+1,bn[nbox+1],ntoy,ntoyleft,nsum);
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-out.txt","w",stdout);
	int t,T;
	long long int i;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld",&n,&m);
		for(i=0;i<n;i++) scanf("%lld %lld",&bn[i],&btype[i]);
		for(i=0;i<m;i++) scanf("%lld %lld",&tn[i],&ttype[i]);
		maxx = 0;
		f(0,bn[0],0,tn[0],0);
		printf("Case #%d: %lld\n",t,maxx);
	}
	return 0;
}




