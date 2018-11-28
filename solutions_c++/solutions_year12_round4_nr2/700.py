#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<time.h>
using namespace std;
__int64 X[11];
__int64 Y[11];
__int64 R[11];
int W,H;
int N;
int globalgood=false;
bool check(int id)
{
	
	for(int i=0;i<=id;i++)
	{
		if(X[id]>W || Y[id]>H )return false;
		for(int j=i+1;j<=id;j++)
		{
			if((X[i]-X[j])*(X[i]-X[j]) + (Y[i]-Y[j])*(Y[i]-Y[j]) <=(R[i]+R[j])*(R[i]+R[j]) )return false;
		}

	}
	return true;
}

bool tryid(int id)
{

	if(globalgood)return true;
	if(id==N)
	{
		globalgood=true;
		return true;
	}
	for(int i=0;i<150;i++)
	{
		X[id]=(rand()*1123132ll)%W;
		Y[id]=(rand()*1142411ll)%H;
		if(check(id))
		{
			if(tryid(id+1))return true;
		}
	}
	return false;
}
int main()
{
	freopen("D:\\gcj\\B-small-attempt4.in","r",stdin);
	srand(time(0));
	//	printf("%d\n",rand());
    freopen("D:\\gcj\\B-small-attempt4.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=0;test<tests;test++)
	{
		
	   scanf("%d %d %d",&N,&W,&H);
	   for(int i=0;i<N;i++)
	   {
		   scanf("%d",&R[i]);
	   }
	   globalgood=false;
	   bool resp=tryid(0);
	   if(!resp)
	   {
		   printf("FAILED!!!\n");
	   }
	   printf("Case #%d: ",test+1);
	   if(!check(N-1))
	   {
		   printf("EPIC FAIL");
	   }
	   for(int i=0;i<N;i++)
	   {
		   if(i!=0)printf(" ");
		   printf("%d %d",(int)X[i],(int)Y[i]);
	   }
	   printf("\n");

	}
}