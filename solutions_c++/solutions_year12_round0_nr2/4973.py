#include<iostream>

using namespace std;

int main()
{
	int T;
	int N[100];
	int S[100];
	int p[100];
	int ti[100][100];
	int NoG[100];
	for (int i = 0 ; i<100;++i)
	{	
		N[i] = -1;
		S[i] = -1;
		p[i] = -1;
		NoG[i]= 0;
		for (int j =0; j<100 ; ++j)
			ti[i][j] = -1;
	}
		
	cin>>T;
	//Read data
	for ( int i =0 ; i<T ; ++i)
	{
		cin>>N[i];
		cin>>S[i];
		cin>>p[i];
		for (int j =0 ;j<N[i];++j)
			cin>>ti[i][j];
	}//end of for i

	for(int i =0; i<T ; ++i)
	{

	if(p[i]==0) {NoG[i] = N[i];}
	
	if(p[i]==1) 
	{
		for(int j=0; j<N[i];++j)
			if(ti[i][j]>0)
				++NoG[i];
	}
	else if(p[i]>=2)
	{
		for(int j=0; j<N[i];++j)
			{if(ti[i][j]>=3*p[i]-2)
				++NoG[i];
			if(ti[i][j] == 3*p[i]-3||ti[i][j] == 3*p[i]-4)
				{if(S[i]==0);
				else {++NoG[i];--S[i];continue;}
				}}
	}
	}
	//output printing
	for(int i =0;i<T ;++i)
		cout<<"Case #"<<i+1<<':'<<' '<<NoG[i]<<'\n';  
}//end of main
