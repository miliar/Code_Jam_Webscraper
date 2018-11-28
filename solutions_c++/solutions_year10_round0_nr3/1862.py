//Compiler:visual c++(vs 2008)
#include<stdio.h>
__int64 Count[1005];
__int64 Next[1005];
__int64 Groups[1005];
int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
	__int64 t,R,k,N;
	__int64 SumOfeveryt;
	scanf("%I64d",&t);
	for(__int64 i=0;i<t;i++)
	{
        scanf("%I64d %I64d %I64d",&R, &k,&N);
		 SumOfeveryt=0;
		for(__int64 j=0;j<N;j++)
		{
			scanf("%I64d",&Groups[j]);
		    SumOfeveryt+=Groups[j];
		}
		
		for(__int64 j=0;j<N;j++)//Count Forward Sum
		{
		 if(k>=SumOfeveryt)Count[j]=SumOfeveryt;else Count[j]=0;
  		}
		__int64 bufk=k%SumOfeveryt;
		if(k>=SumOfeveryt)bufk=0;
		for(__int64 j=0;j<N;j++)////Count Forward Sum Remainders
		{
            __int64 CurrentSum=0;
			__int64 CurJ=j;
			while(CurrentSum+Groups[CurJ]<=bufk)
			{
				CurrentSum+=Groups[CurJ];
				CurJ=(CurJ+1)%N;
                    
			}
			Count[j]+=CurrentSum;
			Next[j]=(CurJ)%N;
		}
		__int64 CurI=0;
		__int64 Answer=0;
		for(__int64 Round=0;Round<R;Round++)
		{
           Answer+=Count[CurI];
		   CurI=Next[CurI];

		}
		printf("Case #%I64d: %I64d\n",i+1,Answer);


	

	}

}