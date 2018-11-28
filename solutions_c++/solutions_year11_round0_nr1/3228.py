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

#define MAX 100
int N, arr[MAX];

int f()
{	
	int i,j;
	int Opos=1,Bpos=-1;
	int Otime=0,Btime=0;
	int time=0;

	rep(i,N)
	{
		if(arr[i]>0)//O
		{
			if(time-Otime>abs(Opos-arr[i])) time+=1;
			else
				time+=abs(Opos-arr[i])-(time-Otime)+1;

			Otime=time;
			Opos=arr[i];
		}
		else//B
		{
			if(time-Btime>abs(Bpos-arr[i])) time+=1;
			else
				time+=abs(Bpos-arr[i])-(time-Btime)+1;
			Btime=time;
			Bpos=arr[i];
		}
	}
	return time;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount,i,j;
	char R[2];
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);
		rep(j,N)
		{
			fscanf(In,"%s%d",R,arr+j);
			if(R[0]=='B') arr[j]*=-1;
		}

		int res=f();
		fprintf(Out,"%d\n",res);
	};
	fclose(In);
	fclose(Out);
	return 0;
}