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

#define rep(A,B) for(A=0;A<B;++A)
#define repi(A,I,B) for(A=I;A<B;++A)
#define repd(A,B) for(A=B-1;A>=0;--A)
#define repdi(A,I,B) for(A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

int N, S, p;
int A[100];

int f()
{	
	int res=0;
	int i,av,max;

	rep(i,N) 
	{
		switch (A[i]%3)
		{
			case 0: av=A[i]/3;   max=av+1;break;
			case 1: av=A[i]/3+1; max=av;  break;
			case 2: av=A[i]/3+1; max=av+1;break;
		}
		
		if(av>=p) ++res;
		else
			if((max>=p)&&(max>1)&&(S)) {++res;--S;}
	}
	
	return res;
}

int main()
{
	FILE* In=fopen("B-large.in","r");if(!In) return 1;
	FILE* Out=fopen("B-large.res","w");if(!Out) return 2;

	int nCount,i,n;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d%d",&N,&S,&p);
		rep(n,N) fscanf(In,"%d",&A[n]); 	
		int res=f();
		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}