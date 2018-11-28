#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,CASE=0;
	vector<int> A;
	vector<int> B;
	int i,j,k;
	int a,b,c;
	int count;

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0..out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d",&N);

		A.clear();
		B.clear();

		for(i=0; i<N; i++)
		{
			scanf("%d %d",&a,&b);
			A.push_back(a);
			B.push_back(b);
		}

		for(i=0,count=0; i<N; i++)
		{
			for(j=i+1; j<N; j++)
			{
				if(A[i] > A[j] && B[i] < B[j])
					count++;
				else if(A[i] < A[j] && B[i] > B[j])
					count++;
			}
		}

			
		printf("Case #%d: %d\n",CASE,count);



	}




}