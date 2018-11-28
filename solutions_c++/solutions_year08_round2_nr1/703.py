#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
typedef long long int llInt;
struct Point
{
	llInt x,y;
};

bool isInteger(double value)
{
	return value-floor(value) == 0 ? true:false;
}

bool checkValues(Point p1,Point p2,Point p3)
{
	return isInteger(((double)p1.x+p2.x+p3.x)/3) && isInteger(((double)p1.y+p2.y+p3.y)/3);
}

void storeValues(Point Array[],llInt n,llInt A,llInt B,llInt C,llInt D,llInt x0,llInt y0,llInt M)
{
	llInt X = x0, Y = y0;
	Array[0].x=x0;
	Array[0].y=y0;
	for(llInt i = 1;i <= n-1;i++)
  	{
		X = (A * X + B) % M;
  		Y = (C * Y + D) % M;
  		Array[i].x=X;
  		Array[i].y=Y;
	}
}
void display(Point Array[],llInt n)
{
	for(llInt i=0;i < n;i++)
	 cout<<"("<<Array[i].x<<", "<<Array[i].y<<")\t";
}
llInt calculate(Point Array[],llInt n)
{
	llInt i,j,k;
	llInt count=0;
	for(i=0;i <= n-3;i++)
	 for(j=i+1; j <= n-2;j++)
	  for(k=j+1; k <= n-1;k++)
	   if(checkValues(Array[i],Array[j],Array[k]))
	   	count++;
	return count;
}

void runTestCase(int i)
{
	llInt n, A, B, C, D, x0, y0, M;
	scanf("%I64d",&n);
	scanf("%I64d",&A);
	scanf("%I64d",&B);
	scanf("%I64d",&C);
	scanf("%I64d",&D);
	scanf("%I64d",&x0);
	scanf("%I64d",&y0);
	scanf("%I64d",&M);
	Point *Array=new Point[n];
	storeValues(Array,n,A,B,C,D,x0,y0,M);
	printf("Case #%d: %I64d\n",i,calculate(Array,n));
	delete[] Array;
}

int main()
{
	int N;
	scanf("%d",&N);
	for(int i=1;i <= N;i++)
	 runTestCase(i);
	return 0;
}
