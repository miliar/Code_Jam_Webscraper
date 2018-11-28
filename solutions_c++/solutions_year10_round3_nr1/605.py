
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG 1

bool intersection(int a1,int b1,int a2,int b2);
bool intersection(int a1,int b1,int a2,int b2)
{
    if((a1-a2)*(b1-b2)>0)
		return false;
	else
		return true;
}

int main()
{

#if DEBUG
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	///////////////////////////////////
	int T,Case=1;
	int N;
	int A[1005],B[1005];

	cin>>T;
	while(T--)
	{
		cin>>N;
		int i;
		for(i=0;i<N;i++)
		{
			scanf("%d%d",&A[i],&B[i]);
		}

		int count=0;
		for(i=0;i<N-1;i++)
		for(int j=i+1;j<N;j++)
		{
			if( intersection(A[i],B[i],A[j],B[j]) )
				count++;
		}

		printf("Case #%d: %d\n",Case++,count);
	}


	return 0;
}