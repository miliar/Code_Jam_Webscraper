#include<iostream>
#include<fstream>

using namespace std;


void snap(int snapper[],int N,int i)
{
	if(i==N)return;
	else if(snapper[i]==0)snapper[i]=1;
	else
	{
		snapper[i]=0;
		snap(snapper,N,i+1);
	}
}

main()
{
	ifstream infile("input.txt");
	ofstream outfile("output.txt");
	int snapper[10];int flag;
	int T,N,K;


	infile>>T;
	for(int i=0;i<T;i++)
	{
		infile>>N>>K;
		for(int j=0;j<10;j++)snapper[j]=0;
		for(j=0;j<K;j++)
			snap(snapper,N,0);
		flag=1;
		for(j=0;j<N;j++)
			flag=flag&&snapper[j];
		if(flag==1)
			outfile<<"Case #"<<i+1<<": ON"<<endl;
		else 
			outfile<<"Case #"<<i+1<<": OFF"<<endl;

	}
	return 0;
}
