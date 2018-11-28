#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream cout("c:\\Prob1S.txt");
	long long Xs[105],Ys[105];
	long long N,M,X0,Y0,A,B,C,D;
	int n;
	cin>>n;
	int c=0;
	while(n--)
	{
		cin>>N;
		cin>>A>>B>>C>>D>>X0>>Y0>>M;
		Xs[0]=X0;
		Ys[0]=Y0;
		for(int i=1;i<N;i++)
		{
			Xs[i]=(A*Xs[i-1] + B) % M;
			Ys[i]=(C*Ys[i-1] + D) % M;
		}
		int Count=0;
		for(int j=0;j<N;j++)
			for(int k=j+1;k<N;k++)
				for(int t=k+1;t<N;t++)
					if((Xs[j]+Xs[k]+Xs[t])%3==0 && (Ys[j]+Ys[k]+Ys[t])%3==0)
						Count++;
		c++;
		cout<<"Case #"<<c<<": ";
		cout<<Count<<endl;


	}
	return 0; 
}