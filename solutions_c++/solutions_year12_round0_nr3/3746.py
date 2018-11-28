#include<iostream>
#include<cmath>

using namespace std;

long score[2000001][10];

long numDigit(long i)
{
	long count=0;
	if(i==0) return 1;
	while(i!=0)
	{i/=10;count++;}
	return count;

}
long getScore(long i)
{
	long temp,count=0,mod=10;
	long numI = numDigit(i);
	while(1)
	{
		long temp1 = i%mod;		
		if(temp1 == i) break;
		temp = temp1 * pow(10,(double)numDigit(i/mod)) +(i/mod);
		if(i==temp) break;
		if(i<temp && numI == numDigit(temp))
		{
			count++;
			score[i][count] = temp;
		}
		mod*=10;
	}
	return count;
}

void pre()
{
	//getScore(12345);
	for(long i=0;i<=2000000;i++)
	{
		score[i][0] = getScore(i);
	}
}

int main()
{
	pre();

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	long count=1,cases,total,n,m;
	cin>>cases;
	while(cases--)
	{
		cin>>n>>m;	
		total = 0;
		for(long i=n;i<=m;i++)
		{
			for(long j=1;j<=score[i][0];j++)
				if(score[i][j]<=m)
			{
	//			cout<<i<<" --- "<<score[i][j]<<endl;
				total++;
			}
			//total+=score[i];
		}
		cout<<"Case #"<<count<<": "<<total<<endl;
		count++;
	}
	return 0;
}