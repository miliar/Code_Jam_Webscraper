#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
using namespace std;

int T;
int R;
int k;
int n;
int money;

int main()
{
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	ifs>>T;
	
	for(int l=0;l<T;l++){
	ifs>>R>>k>>n;
	money=0;
	int g;
	queue<int>q;
	
	for(int i=0;i<n;i++)
	{
		ifs>>g;
		q.push(g);
	}

	for(int i=0;i<R;i++)
	{
		int sum=0;
		int id=0;
		int count=1;
		int fro=q.front();
		
		while(sum+fro<=k&&count<=n)
		{
			q.push(fro);
			q.pop();
			sum+=fro;
			fro=q.front();
			count++;
		}
		
		money+=sum;
	}
	
	ofs<<"Case #"<<l+1<<": "<<money<<endl;
	}

	
	return 0;
}
