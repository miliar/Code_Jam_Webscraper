/*Written by Vladimir Ignatiev aka Neacher (neacher@gmail.com)*/
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

int main()
{
	FILE* In=fopen("C.in","r");if(!In) return 1;
	FILE* Out=fopen("C.res","w");if(!Out) return 2;

	int N,C;
	int nCount,i,j;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);

		int Sum=0,MinC=INT_MAX,XorSum=0;
		rep(j,N) 
		{
			fscanf(In,"%d",&C);
			MinC=min(MinC,C);
			Sum+=C;
			XorSum^=C;
		}

		if(XorSum)
			fprintf(Out,"%s\n","NO");
		else
			fprintf(Out,"%d\n",Sum-MinC);
	};
	fclose(In);
	fclose(Out);
	return 0;
}