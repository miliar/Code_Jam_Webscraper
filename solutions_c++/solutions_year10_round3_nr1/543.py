#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <utility>
#include <iostream>
#include <algorithm>
#define CASEID printf("Case #%d: ",iD++)
#define CASES  for(scanf("%d",&cases);cases--;)
using namespace std;

int N,A[1005],B[1005];

int main()
{
	int cases,iD=1;

	CASES
	{
		cin>>N;
		for(int i=0;i<N;i++)
			cin>>A[i]>>B[i];
		
		int cnt=0;

		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(A[i]>A[j] && B[i]<B[j])
					cnt++;
				else if(A[i]<A[j] && B[i]>B[j])
					cnt++;
			}
		}
		CASEID;
		printf("%d\n",cnt/2);
	}
	return 0;
}

