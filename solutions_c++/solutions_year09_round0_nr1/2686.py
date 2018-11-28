#include<stdio.h>
#include<vector>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
vector<string> Mass;
int main()
{
	int i,j,k,n,m,t,l;
	double a,b;
	cin>>l>>k>>n;
	string A;
	for(i=0;i<k;++i)
	{
		cin>>A;
		Mass.push_back(A);
	}
	char read;
	string B;
	vector<string> find;
	for(i=0;i<n;++i)
	{
		cin>>A;
		find.clear();
		for(t=0;t<A.size();++t)
		{
			B = "";
			if( A[t]=='(' )
			{
				t++;
				while(1)
				{
					if( A[t]==')' )
						break;
					B+=A[t++];
				}
				find.push_back(B);
			}
			else
			{
				B = A[t];
				find.push_back(B);
			}
		}
		int Massiv[5000];
		for(j=0;j<Mass.size();++j)
			Massiv[j]=1;
		int result = Mass.size();
		for(t=0;t<Mass.size();++t)
		{
			for(j=0;j<find.size();++j)
			{
				
				if( -1==find[j].find(Mass[t][j]) )
				{
					//Massiv[t] = 0;
					result--;
					break;
				}
			}
		}
		//result = 0;
		//for(j=0;j<Mass.size();++j)
		//	result+=Massiv[j];
		cout<<"Case #"<<(i+1)<<": "<<result<<"\n";
	}

	//for(i=0;i<Mass.size();++i)
	//	cout<<Mass[i]<<"\n";

	return 0;
}