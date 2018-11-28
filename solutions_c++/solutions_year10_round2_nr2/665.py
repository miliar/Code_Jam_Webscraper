#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;


int main()
{
	ifstream fi("credit.in");
	ofstream fo("credit.out");

	int C, N, K, B, T;
	int x[60];
	int v[60];
	fi>>C;

	for(int c=1; c<=C; c++)
	{
		fo<<"Case #"<<c<<": ";

		fi>>N>>K>>B>>T;

		for(int i=0;i<N;i++)
			fi>>x[i];
		for(int i=0; i<N;i++)
			fi>>v[i];

		int countPass=K;
		int swap=0;
		bool pass[60];
		fill(pass,pass+60,false);
		for(int i=N-1; i>=0; i--)
		{
			int S=v[i]*T+x[i];

			if(S>=B)
			{
				pass[i]=true;			
				countPass--;
			}
		}

		if(countPass>0)
		{
			fo<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			int count=0;
			for(int i=N-1; i>=0; i--)
			{
				if(pass[i])
				{
					for(int j=i+1; j<N; j++)
					{
						if(!pass[j])
							swap++;
					}
					count++;
				}
				if(count==K) break;
			}
			fo<<swap<<endl;
		}

	}
}
	

		 
		