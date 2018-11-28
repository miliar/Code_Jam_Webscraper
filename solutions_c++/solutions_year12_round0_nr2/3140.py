#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

#define MAX 35

int nonsurp[MAX],surp[MAX];

int maximum (int i, int j, int k)
{
	int m1 = (i>j)? i:j;
	return (k>m1)?k:m1;
}
int main()
{
	//Construct the 2 arrays using 3 for loops
	memset (nonsurp,-1,sizeof(nonsurp));
	memset (surp,-1,sizeof(nonsurp));

	for (int i=0;i<=10;i++)
	for (int j=0;j<=10;j++)
	for (int k=0;k<=10;k++)
	{
		//Non-surprising
		if (max(i,j)-min(i,j)<=1 && max(i,k)-min(i,k)<=1 && max(k,j)-min(k,j)<=1)
		{
			int m = maximum(i,j,k);
			if(m>nonsurp[i+j+k])	nonsurp[i+j+k]=m;
		}
		//surprising
		else if (max(i,j)-min(i,j)<=2 && max(i,k)-min(i,k)<=2 && max(k,j)-min(k,j)<=2)
		{
			int m = maximum(i,j,k);
			if(m>nonsurp[i+j+k])	surp[i+j+k]=m;
		}
	}

	//Begin solving  the problem
	ifstream fin ("CodeJam.in");
	ofstream fout("CodeJam.out");
	
	int tests;
	cin>>tests;

	for(int x=1;x<=tests;x++)
	{
		int N,S,P;	//N: number of googlers, S: number of surprising triplets, P: minimum best result

		cin>>N>>S>>P;
		vector<int> scores(N);
		int ret = 0;
		for (int i=0;i<N;i++)
		{
			cin>>scores[i];
			if (nonsurp[scores[i]]>=P)	ret++;
			else if (surp[scores[i]]>=P && S>0)	{ret++;S--;}
		}
		cout<<"Case #"<<x<<": "<<ret<<endl;
	}
	return 0;
}