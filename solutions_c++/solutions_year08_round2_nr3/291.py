#include<iostream.h>
#include<fstream.h>
int main()
{
	ifstream in("C-small-attempt0.in");
	int cases;
	in>>cases;
	for(int i=1;i<=cases;i++)
	{
		int n;
		in>>n;
		int A[n+1];
		for(int j=0;j<=n;j++)
			A[j]=0;
		int count=0;
			int k=1;
		for(int j=1; j <= n;j++)
		{
			count=0;
			while(1)
			{
				if (A[k] == 0) count++;
				if(j == count)
				{
					 A[k]=j;
					if(k==n)k=1; else k++;
					break;
				}
				if(k==n)k=1; else k++;
			}
		}
		cout<<"Case #"<<i<<": ";
		in>> k;
		for(int j=0;j<k;j++)
		{
			in>>count;
			cout<<A[count]<<" ";
		}
		cout<<endl;
		
	}
	return 0;
}
