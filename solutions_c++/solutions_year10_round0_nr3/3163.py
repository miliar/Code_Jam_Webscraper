#include <iostream>
#include <fstream>

using namespace std;


int solve(int R,int k,int N,int * g)
{
	int front=0,back=N,euro=0;
	for(int i=0;i<R;++i)
	{
		int freeseats=k;
		int groups=0;
		while(freeseats>=g[front] && groups<N)
		{
			freeseats-=g[front];
			front=(front+1)%N;
			groups++;
		}
		int pass=k-freeseats;
		euro+=pass;
		back=(back+pass)%N;
	}
	return euro;
}

int main()
{
	int T;
	ifstream ifs("C-small-attempt1.in");
	ifs>>T;
	for(int i=1;i<=T;++i)
	{
		int R,k,N;
		ifs>>R>>k>>N;
		int g[11];
		for(int j=0;j<N;++j)
		{
			ifs>>g[j];
		}
		cout<<"Case #"<<i<<": "<<solve(R,k,N,g)<<endl;
	}
}
