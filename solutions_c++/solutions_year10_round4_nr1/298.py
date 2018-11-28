#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int num[101][101];
	int k,t;
	int ii,i,j,kk;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{		
		ifs>>k;
		for(i=0; i<k; i++)
			for(j=0; j<=i; j++)
				ifs>>num[i][j];
		for(i=k-2; i>=0; i--)
			for(j=0; j<=i; j++)
				ifs>>num[k+k-i-2][j];


		int maxY=1;
		for(i=2; i<=k; i++)
		{
			for(j=0; j<i; j++)
			{
				int ll= (i-1+j)<k ? i+j : k+k-(i-1+j)-1;
				int pp=ll/2-(i-j)/2;
				for(kk=0; kk<i-j; kk++)
					if(num[i-1-j][kk] != num[i-1+j][kk+pp])
						break;
				if(kk<i-j)
					break;
			}
			if(j>=i)
				maxY=max(maxY,i);
		}
		for(i=2; i<k; i++)
		{
			for(j=0; j<i; j++)
			{
				int ll= (k+k-i-1-j)<k ? k+k-i-1-j+1 : k+k-(k+k-i-1-j)-1;
				int pp=ll/2-(i-j)/2;

				for(kk=0; kk<i-j; kk++)
					if(num[k+k-i-1-j][kk+pp] != num[k+k-i-1+j][kk])
						break;
				if(kk<i-j)
					break;
			}
			if(j>=i)
				maxY=max(maxY,i);
		}

		
		int maxX=1;
		for(i=2; i<=k; i++)
		{
			for(j=0; j<i; j++)
			{
				for(kk=0; kk<i-j; kk++)
				{
					if(num[k-1-j][kk] != num[k-1-j][i-j-kk-1])
						break;
					if(num[k-1+j][kk] != num[k-1+j][i-j-kk-1])
						break;
				}
				if(kk<i-j)
					break;
			}
			if(j>=i)
				maxX=max(maxX,i);
		}

		for(i=2; i<=k; i++)
		{
			for(j=0; j<i; j++)
			{
				for(kk=0; kk<i-j; kk++)
				{
					if(num[k-1-j][k-1-j-kk] != num[k-1-j][k-1-j-(i-j-kk-1)])
						break;
					if(num[k-1+j][k-1-j-kk] != num[k-1+j][k-1-j-(i-j-kk-1)])
						break;
				}
				if(kk<i-j)
					break;
			}
			if(j>=i)
				maxX=max(maxX,i);
		}


		cout<<maxY<<' '<<maxX<<endl;
		int k2=k+k-maxY + k-maxX;


		ofs<<"Case #"<<ii+1<<": "<<k2*k2-k*k<<endl;
	}
}
