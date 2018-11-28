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

int N, M[1000], s[1000][10];

int arr[1000];

bool go(int x)
{
	rep(j,M[x])
	{
		arr[s[x][j]]++;
		if(arr[s[x][j]]>1) return true;
		if(go(s[x][j])) return true;
	};
	return false;
}

int f()
{	
	rep(i,N)
	{
		memset(arr,0,sizeof(arr));
		if(go(i))return 1;
	}
	
	return 0;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);

		rep(j,N)
		{
			fscanf(In,"%d",M+j);
			rep(k,M[j])
			{
				fscanf(In,"%d",&s[j][k]);
				s[j][k]--;
			}
		}

		if(f()==1)
			fprintf(Out,"Yes\n");
		else
			fprintf(Out,"No\n");

	};
	fclose(In);
	fclose(Out);
	return 0;
}