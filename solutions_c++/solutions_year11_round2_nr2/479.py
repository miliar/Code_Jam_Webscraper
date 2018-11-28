#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int T, C, D,N;
vector<int> p;

void read_case()
{
	int x, y;
	
	cin>>C>>D;
	p.clear();
	N = 0;
	
	for (int i=0; i<C; i++)
	{
		cin>>x>>y;
		N += y;
		for (int j=0; j<y; j++)
			p.push_back(x);
	}
}

int go()
{
	int worst(0);
	
	for (int i=0; i<N; i++)
		for (int j=i+1; j<N; j++)
			worst = max(worst,D*(j-i) - (p[j]-p[i]));
	
	return worst;
}

int main()
{
	cin>>T;
	for (int i=0; i<T; i++)
	{
		read_case();
		cout<<"Case #"<<i+1<<": "<<setprecision(10)<<go()/2.0<<endl;
	}
		
	return 0;
}
