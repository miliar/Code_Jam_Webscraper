#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>

using namespace std;

int findTriangles( vector <double> X, vector <double> Y)
{
	int counter=0;
	
//	cout<<endl<<endl<<X[0]<<endl<<X[1]<<endl<<X[2]<<endl<<X[3]<<endl<<endl;
	
	for (int i=0; i<X.size(); i++)
	{
		for (int j=i+1; j<Y.size(); j++)
		{
			for (int k=j+1; k<X.size(); k++)
			{
				if ( !(i==j || j==k || k==i))
				{
					double x=(X[i] + X[j] + X[k])/3;
					double y=(Y[i] + Y[j] + Y[k])/3;
//					for (int r=0; r<X.size(); r++)
						//if (X[r]==x && Y[r]==y)
						if ( (double) ((int)(x)) == x && (double) ((int)(y)) == y)
						{
							//cout<<X[i]<<","<<Y[i]<<endl;
							//cout<<X[j]<<","<<Y[j]<<endl;
							//cout<<X[k]<<","<<Y[k]<<endl;
							//cout<<x<<","<<y<<endl<<endl;
		//	X[i]=X[j]=X[k]=0.02367; 
							counter++;
						}
				}
			}
		}
	}
	return counter;
}

int main()
{
	ifstream fin;
	fin.open ("Desktop/A-small-attempt3.in");
	ofstream fout;
	fout.open("Desktop/A-small.out");

	char abc[10];
	
	int N;
	fin>>N;
	
//	N=2;
	for (int i=0; i<N; i++)
	{
		string tmp;
		
		long int n, A, B, C, D, x0, y0, M;
		fin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		//cout<<"Trees: "<<endl;
		long long int  X = x0, Y = y0;
		vector<double> Xcord, Ycord;
		
	//	cout<<n<<"\t"<<A<<"\t"<<B<<"\t"<<C<<"\t"<<D<<"\t"<<x0<<"\t"<<y0<<"\t"<<M<<endl;
			Xcord.push_back(X);
			Ycord.push_back(Y);

		//cout<<X<<", "<<Y<<endl;
		for (int t = 1; t<=n-1; t++)
		{	X = (A * X + B) % M;
			Y = (C * Y + D) % M;
//			if (i==8)
	//		cout<<X<<", "<<Y<<endl;
			Xcord.push_back(X);
			Ycord.push_back(Y);
		}

	
//		fout<<"Case #"<<i+1<<": "<<getSwitches(SearchEngines, Queries)<<endl;
		cout<<"Case #"<<i+1<<": "<<findTriangles(Xcord, Ycord)<<endl; 
		fout<<"Case #"<<i+1<<": "<<findTriangles(Xcord, Ycord)<<endl; 

	}			
	
	getchar();
}
