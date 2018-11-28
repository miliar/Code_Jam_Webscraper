#include<iostream>
using namespace std;
int main()
{
	int T,N;
	char R;
	int P;
	int O[100];
	int B[100];
	int i,j;
	//int oi,bi;
	int bit,oit;
	int bLast,oLast;
	int totalTime;
	cin>>T;		
	for(i=0;i<T;i++)
	{	
		totalTime = 0;
		oLast = 1;
		bLast = 1;
		bit = 0;
		oit = 0;
		cin>>N;
		
		//oi=0;bi=0;
		for(j=0;j<N;j++)
		{
			cin>>R>>P;
			//scanf(" %c %d",&R,&P);
			if(R=='B')
			{
				B[j]=P;
				O[j]=0;
				oit = oit + 1 + ((abs(B[j] - bLast) - bit) + abs(abs(B[j] - bLast) - bit))/2;
				totalTime = totalTime + 1 + ((abs(B[j] - bLast) - bit) + abs(abs(B[j] - bLast) - bit))/2;
				bit=0;
				bLast=B[j];
			}
			else
			{
				O[j]=P;
				B[j]=0;
				bit = bit + 1 + ((abs(O[j] - oLast) - oit) + abs(abs(O[j] - oLast) - oit))/2 ;
				totalTime = totalTime + 1 + ((abs(O[j] - oLast) - oit) + abs(abs(O[j] - oLast) - oit))/2;
				oit=0;
				oLast=O[j];
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<totalTime<<endl;
	}
	return 0;
}//main ends
