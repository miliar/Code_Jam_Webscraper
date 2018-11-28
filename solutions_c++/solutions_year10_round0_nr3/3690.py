#include <fstream>
#include <iostream>
#include <cstring>
#include <cassert>
#include <queue>
using namespace std;

int main(int argc, char *argv[])
{
	int t,r,n,k,i,l,j,p;
	queue<int> q;
	int sum;
	char dummy;
	fstream input("C-small.in");
	input >> t;
	input.getline(&dummy,1);
	for(i=0;i<t;i++)
	{
		input >> r;
		input >> k;
		input >> n;
		input.getline(&dummy,1);
		for(l=0;l<n;l++)
		{
			input >> j;
			q.push(j);
		}
		input.getline(&dummy,1);
		sum=0;
		for(j=0;j<r;j++)
		{
			p=0;
			l=q.size();
			while(p+q.front()<=k&&l!=0)
			{
				p+=q.front();
				q.push(q.front());
				q.pop();
				l--;
			}
			sum+=p;
		}
		q=queue<int>();
		cout << "Case #" << i+1 << ": " << sum <<endl;
	}
}