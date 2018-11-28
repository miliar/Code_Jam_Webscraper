#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;




int main()
{
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("A-small.out");
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");


	long long test;
	cin>>test;

	for(long long j=0;j<test;j++)
	{
		char arr[100][100];
		long long r,c;
		cin>>r>>c;

		for(long long i=0;i<r;i++)
		{
			
			for(long long q=0;q<c;q++)
			{
				char c;
				cin>>c;
				arr[i][q]=c;
			}
		}

		bool in=false;
		for(long long i=0;i<r;i++)
		{
			
			for(long long q=0;q<c;q++)
			{
				if(arr[i][q]=='#' && arr[i+1][q]=='#' && arr[i][q+1]=='#' && arr[i+1][q+1]=='#')
				{
					arr[i][q]='/';
					arr[i+1][q]='\\';
					arr[i][q+1]='\\';
					arr[i+1][q+1]='/';
				}
				else if(arr[i][q]=='#')
				{
					in=true;
					break;
				}
			}
			if(in)
				break;
		}
		cout<<"Case #"<<j+1<<":\n";
		if(in)
		{
			cout<<"Impossible\n";
		}
		else
		{
			for(long long i=0;i<r;i++)
			{
				for(long long q=0;q<c;q++)
				{
					cout<<arr[i][q];
				}
				cout<<endl;
			}
		}

		
	}

	//system("pause");
	return 0;
}