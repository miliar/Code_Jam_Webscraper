#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("A-small.out");
	long long no;
	long long n,A,B,C,D,x0,y0,M;
	//char src[10000],tar[10000],val[10000];
	fin>>n;
	
	for(long long c=1; c<=n; c++)
	{
		fin>>no>>A>>B>>C>>D>>x0>>y0>>M;
		//cout<<s<<" "<<src<<" "<<tar<<"\n";
		long long count=0;
		long long tr[no][2]; 
		long long x,y;
		x = x0; y = y0;
		tr[0][0]=x0;tr[0][1]=y0;
		//cout<<x<<y<<endl;
		for(long long i = 1;i<no;i++)
		{
			x = (A * x + B)%M;
			y = (C * y + D)%M;
			tr[i][0]=x;
			tr[i][1]=y;
			//cout<<x<<y<<endl;
		}

		for(long long i=0;i<no-2;i++)
			for(long long j=i+1;j<no-1;j++)
				for(long long k=j+1;k<no;k++)
		{
			
			if((((tr[i][0]+tr[j][0]+tr[k][0])%3) == 0)&&(((tr[i][1]+tr[j][1]+tr[k][1])%3) == 0))
			{	count++;
			//cout<<tr[i][0]<<tr[j][0]<<tr[k][0]<<tr[i][1]<<tr[j][1]<<tr[k][1]<<endl;
			}
		}
		
		fout<<"Case #"<<c<<": "<<count<<"\n";
	
	}
	
	
	return 0;
}

