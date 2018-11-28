/*Vladimir Ignatiev*/
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

#define rep(A,B) for(A=0;A<B;++A)
#define repi(A,I,B) for(A=I;A<B;++A)
#define repd(A,B) for(A=B-1;A>=0;--A)
#define repdi(A,I,B) for(A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

int A, B;

int GetM(int val)
{
	int M=1;
	val/=10;
	while(val)
	{
		M*=10;
		val/=10;
	}
	return M;
};

bool Rec(int& Val,int nM)
{
	bool res;
	int rem=Val%10;
	Val/=10;
	Val+=rem*nM;
	return rem?true:false;
}

int f()
{	
	int val,valR,i,res=0;
	
	repi(val,A,B)
	{
		valR=val;
		int nM=GetM(valR);
		do
		{
			if(Rec(valR,nM)&&(valR>val)&&(valR<=B)) res++;
		}
		while(valR!=val);
	}

	return res;
}

int main()
{
	FILE* In=fopen("C-large.in","r");if(!In) return 1;
	FILE* Out=fopen("C-large2.res","w");if(!Out) return 2;

	int nCount,i;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d",&A,&B);

		int res=f();
		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}