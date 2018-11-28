/*Written by Vladimir Ignatiev*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

typedef long long int64;
#define abs64(A) _abs64((int64)A)
#define INT64_MAX   0x7fffffffffffffffLL
#define INT64_MIN   (-INT64_MAX - 1LL)

int N, M;

struct P
{
	int64 x;
	int X;
};

P A[100],B[100];

struct POS
{
	POS(int a,int b) {x1=a;x2=b;p1=A[a].x;p2=B[b].x;}
	int64 x1;
	int64 x2;
	int p1;
	int p2;
};

bool operator < (const POS& s1,const POS& s2)
{
	if(s1.p1<s2.p1) return 1;
	else if(s1.p1>s2.p1) return 0;

	if(s1.p2<s2.p2) return 1;
	else if(s1.p2>s2.p2) return 0;

	if(s1.x1<s2.x1) return 1;
	else if(s1.x1>s2.x1) return 0;

	if(s1.x2<s2.x2) return 1;
	else if(s1.x2>s2.x2) return 0;

	return 0;
}

map<POS,int64> idx;



int64 iter(int a,int b)
{
	int64 res=0;
	POS pss(a,b);
	map<POS,int64>::iterator pos=idx.find(pss);
	if(pos!=idx.end())
	{
		return pos->second;
	}

	if(a>=N) return 0;
	if(b>=M) return 0;
	if(A[a].x<=0) {res=iter(a+1,b);goto end;}
	if(B[b].x<=0) {res=iter(a,b+1);goto end;}
	
	if(A[a].X==B[b].X)
	{
		if(A[a].x==B[b].x) {res=iter(a+1,b+1)+A[a].x; goto end;}

		if(A[a].x>B[b].x) {A[a].x-=B[b].x; res=iter(a,b+1)+B[b].x; A[a].x+=B[b].x; goto end;}
		else			  {B[b].x-=A[a].x; res=iter(a+1,b)+A[a].x; B[b].x+=A[a].x; goto end;}
	}
	else
	{
		res=max(iter(a+1,b),iter(a,b+1));
	}

end:;
	idx[pss]=res;
	return res;
}

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		idx.clear();

		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d",&N,&M);
		rep(j,N)
			fscanf(In,"%I64d%d",&A[j].x,&A[j].X);
		
		rep(k,M)
			fscanf(In,"%I64d%d",&B[k].x,&B[k].X);
		
		fprintf(Out,"%I64d\n",iter(0,0));
	};
	fclose(In);
	fclose(Out);
	return 0;
}