#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char S[1010];
char T[1010];
int p[100];
int k;

int rle(char* x)
{
	int len=strlen(x);
	int ret=1;
	for(int i=1;i<len;i++)
		if (x[i]!=x[i-1]) ret++;
	//cout<<"ret="<<ret<<endl;
	return ret;
}

int main()
{
	int N;
	//printf("%d\n", rle("aabcaaaa"));
	scanf("%d",&N);
	for(int cas=1;cas<=N;cas++)
	{
		scanf("%d",&k);
		scanf("%s", S);
		int l=strlen(S);
		for (int i=0;i<k;i++) p[i]=i;
		int ret=1000000;
		do
		{
			
			int z=0;
			for(int i=0;i<l;i++)
			{
				if (i>0 && (i%k)==0) z++;
				T[i]=S[p[i%k]+(z*k)];	
			}
			
			T[l]=0;
			ret=min(ret, rle(T));
			//printf("%s\n",T);
		} while(next_permutation(p,p+k));
		printf("Case #%d: %d\n", cas, ret);
	}	
}
