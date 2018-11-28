#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int main()
{
	int i,j,x[30],y,p,N;
/*	int M,N;
	M=1000000;
	N=30;
	int a[M][N];
	for(j=0;j<N;j++)
	{
		for(i=0;i<M;i++)
		{
			x=(int)pow(2,j+1);
			y=(int)(x/2) - 1;
			if(i%x<=y) a[i][j]=0;
			else a[i][j]=1;
		}
	}
	
/*	for(i=0;i<M;i++)
	{
		for(j=0;j<N;j++)
		cout<<a[i][j]<<" ";
		cout<<"\n";
	}

*/
	ifstream input;
	ofstream output;
	input.open("A.in");
	output.open("A.out");
	input>>N;
for(j=0;j<30;j++)	
x[j] = (int)pow(2,j+1);

		for(p=1;p<=N;p++)	
		{
		input >> j >> i;
		
		int flag=0;
//		cout<<j<<" "<<i<<"\n";	
		for(int k=j-1;k>=0;k--)
		{
		if(i%x[k]<=(x[k]/2 -1))
		{output<<"Case #"<<p<<": OFF\n"; flag=1;
		break;}
		}
		if(flag==0)
		output<<"Case #"<<p<<": ON\n";
		
	
		}

input.close();
output.close();

return 0;
}
