#include<stdio.h>
#include<vector>
using namespace std;

#define MAX_N 1007

typedef __int64 Long;

long Num[ MAX_N+7];
long Run,Cap,N;

long Visit[ MAX_N+7];
long True;

Long Run_Index[ MAX_N+7];
Long Run_Earn[ MAX_N+7];
Long Index_St[ MAX_N+7];

Long Cycle_St,Cycle_Run,Cycle_Len,Cycle_Earn;
Long Ans;


void Check_Cycle( void)
{
	long St =0,End;
	Long Earn =0;
	long Count =0;

	True++;
	while( Visit[ St] != True){

		Count++;//printf("Run %ld St %ld ",Count,St);

		Visit[ St] =True;
		Run_Index[ Count] =St;
		Index_St[ St] =Count;


		Long Tot =Num[ St];
		for( End =(St+1)%N;End != St;End =(End+1)%N){//printf("%ld\n",Tot);
			if( Tot + Num[End] <=Cap) Tot +=Num[End];
			else break;
		}
		Earn +=Tot;
		Run_Earn[ Count] =Earn;//printf("%ld\n",Earn);

		St =End;
	}//printf("Run %ld St %ld\n",Count+1,St);

	Cycle_St =St;
	Cycle_Run =Index_St[ St];
	Cycle_Len =Count -Cycle_Run +1;
	Cycle_Earn =Run_Earn[ Count] -Run_Earn[ Cycle_Run-1];	
}


void Calc_Ans( void)
{
	Ans =0;
	if( Cycle_Run > Run){
		Ans =Run_Earn[ Run];
		return;
	}

	
	Ans =Run_Earn[ Cycle_Run-1];//printf("here %ld\n",Cycle_Earn);

	long Kept_Run =Run -Cycle_Run+1;
	long V =Kept_Run /Cycle_Len;
	Ans +=V *Cycle_Earn;

	Kept_Run =Kept_Run %Cycle_Len;
	Ans += Run_Earn[ Cycle_Run-1+Kept_Run] - Run_Earn[ Cycle_Run-1];
}




int main( void)
{
	long Icase,t;

	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%ld",&Icase);
	for( t=1;t<=Icase;t++){
		scanf("%ld%ld%ld",&Run,&Cap,&N);

		long i;
		for( i=0;i<N;i++){
			scanf("%ld",&Num[i]);
		}

		Check_Cycle();
		Calc_Ans();
		printf("Case #%ld: %I64d\n",t,Ans);
	}

	return 0;
}


