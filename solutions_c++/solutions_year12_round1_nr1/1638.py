#include<iostream>
#include<stdio.h>
float min(float a,float b)
{
if(a<b)return a;
else return b;
}
using namespace std;
int main()
{
	int ttt;
	cin>>ttt;
	for(int tttt=1;tttt<=ttt;tttt++)
	{
		int A,B;
		cin>>A;
		cin>>B;
		float prob[A+1];
		for(int i=0;i<A;i++)
			cin>>prob[i];
		float move[A+1][2];
		for(int i=0;i<=A;i++)
		{
			move[i][0]=1.0*(1.0*B-1.0*A+1.0+2.0*i);
			move[i][1]=move[i][0]+1.0*(1.0*B+1.0);

		}
		
		float expected=2*B;
		float P[A+2];
		P[0]=1;
		for(int i=1;i<=A;i++)
			P[i]=P[i-1]*prob[i-1];
		for(int i=0;i<=A;i++)
		{
			//	for(int j=1;j<=A-i;j++)
			//		P=P*prob[j];

			float temp=P[A-i]*move[i][0]+(1-P[A-i])*move[i][1];
	expected=min(temp,expected);
		}		

	if(A!=B)
		expected=min(expected,1.0*(B+2));


	cout<<"Case #"<<tttt<<": ";
printf("%.6f\n",expected);
}
}
