#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <assert.h>

using namespace std;
//#define DBG_PRINT printf
#define DBG_PRINT 

typedef struct  
{
	int X;
	int Y;
}PAIR;
typedef vector<PAIR> CUSTOMER_INFO;
typedef vector<CUSTOMER_INFO> ALL_INFO;

bool test(ALL_INFO &AI,long Num,int NumOfMF)
	{
		//≈–î‡Num «∑ÒùM◊„AI
		//bool ret = true;
		int NumOfCust = AI.size();
		//char *ArrayManZu = new char[NumOfCust];//1ùM◊„£¨0Œª‘LÜñ
		//memset(ArrayManZu,0,NumOfCust*sizeof(char));

		for(int j=0;j<NumOfCust;j++)
		{
			CUSTOMER_INFO & CI = AI[j];
			int num = CI.size();

			bool ManZu = false;

			for (int k=0;k<num;k++)
			{
				PAIR &pr = CI[k];
				int Value = (Num>>(pr.X))&1;
				if( pr.Y==Value)
				{
					ManZu=true;
					break;
				}
			}

			if(!ManZu)
				return false;
		}

		//delete []ArrayManZu;
		return true;
	}
	int main()
	{
		int C,N,M;
		
		scanf("%d\n",&C);//num of test case
		DBG_PRINT("C %d\n",C);
		for (int i=0;i<C;i++)
		{
			ALL_INFO Info;
			scanf("%d\n",&N);//num of milkshake flavors.
			scanf("%d\n",&M);//num of customers
			DBG_PRINT("N %d M %d\n",N , M);
			Info.reserve(M);
			for (int j=0;j<M;j++)//each customer
			{
				int T;//number of milkshake types the customer likes,
				scanf("%d",&T);
				DBG_PRINT("T %d\n",T);
				CUSTOMER_INFO CI;
				CI.reserve(T);
				for (int k=0;k<T;k++)
				{
					PAIR pr;
					scanf("%d%d",&pr.X,&pr.Y);
					pr.X--;
					CI.push_back(pr);
					DBG_PRINT("pair[%d] %d %d\n",k,pr.X,pr.Y);
				}
				Info.push_back(CI);
			}
			
			bool bFind=false;
			long BestNum = 0;
			for (long l=0;l<(1<<N);l++)
			{
				if(test(Info,l,N))
				{
					bFind = true;
					BestNum = l;
					break;
				}
			}

			if(!bFind)
				printf("Case #%d: IMPOSSIBLE\n",i+1);
			else
			{
				printf("Case #%d:",i+1);
				for (int x=0;x<N;x++)
				{
					printf(" %d",(BestNum>>x)&1);
				}
				printf("\n");
			}
		}
		return 0;
	}
	