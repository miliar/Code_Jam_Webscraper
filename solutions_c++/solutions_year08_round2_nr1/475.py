#include <stdio.h>

#include <string>


long long n,A,B,C,D,x0,y0,M;

long long data[110000][4][3][3];



long long make()
{
	int i,t1,t2;
	long long X,Y;

	memset(data,0,sizeof(data));
	i = 0;
	X = x0;
	Y = y0;
	
	data[0][1][X%3][Y%3] = 1;

	for(i = 1;i<n;i++)
	{
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		
		for(t1=0;t1<3;t1++)
		for(t2=0;t2<3;t2++)
			data[i][1][t1][t2] += data[i-1][1][t1][t2];		//not taken


		data[i][1][X%3][Y%3]++;		//taken	

		for(t1=0;t1<3;t1++)
		for(t2=0;t2<3;t2++)
			data[i][2][t1][t2] += data[i-1][2][t1][t2];		//not taken

		for(t1=0;t1<3;t1++)
		for(t2=0;t2<3;t2++)
			data[i][2][(t1+X)%3][(t2+Y)%3] += data[i-1][1][t1][t2];		//taken

		for(t1=0;t1<3;t1++)
		for(t2=0;t2<3;t2++)
			data[i][3][t1][t2] += data[i-1][3][t1][t2];		//not taken

		for(t1=0;t1<3;t1++)
		for(t2=0;t2<3;t2++)
			data[i][3][(t1+X)%3][(t2+Y)%3] += data[i-1][2][t1][t2];		//taken
	}

	return data[n-1][3][0][0];
}

int main()
{
	int i,N;
	freopen("output.txt","w",stdout);
	scanf("%d",&N);

	for(i=0;i<N;i++)
	{
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		printf("Case #%d: %lld\n",i+1,make());
	}
	return 0;
}