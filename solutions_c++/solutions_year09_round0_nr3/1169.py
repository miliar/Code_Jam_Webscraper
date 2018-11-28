#include <fstream>
#include <string>
#include <iomanip.h>

using namespace std;

static ifstream in("C-large.in");

static int Num[501][20];

int Cal(string &A, string &B)
{
	int i,j,t,sum;
	int lengthA,lengthB,l;

	for(i=0;i<501;++i)
	{
		for(j=0;j<20;++j)
			Num[i][j]=0;
	}

	lengthA=A.length();
	lengthB=B.length();
	l=lengthB-1;
	for(i=lengthA-1;i>=0;--i)
	{
		if(A[i]==B[l])
			Num[i][l]=1+Num[i-1][l];
		else
			Num[i][l]=0;
	}
	
	for(i=lengthA-1;i>=0;--i)
	{
		for(j=l-1;j>=0;--j)
		{
			if(A[i]!=B[j])
			{
				Num[i][j]=0;
				continue;
			}
			else
			{
				sum=0;
				for(t=i+1;t<lengthA;++t)
				{
					if(A[t]==B[j+1])
						sum+=Num[t][j+1];

					if(sum>=10000)
						sum=sum%10000;
				}
				Num[i][j]=sum;
			}
		}
	}

	for(i=lengthA-1,sum=0;i>=0;--i)
	{
		if(A[i]==B[0])
			sum+=Num[i][0];

		if(sum>=10000)
			sum=sum%10000;
	}

	return sum;
}

int main()
{
	int i,N,res;
	string B("welcome to code jam");
	string A;

	in >> N;
	getline(in, A);
	for(i=0;i<N;++i)
	{
		getline(in, A);
		res=Cal(A, B);
		cout << "Case #" << i+1 << ": "; 
		cout << setw(4) << setfill('0') << res << endl;
	}

	return 0;
}