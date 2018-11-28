#include <iostream>
#include <list>
//cout<<"Case #"<<45<<": "<<78<<endl;
using namespace std;
void Solve(int);
int main()
{
	int N;
	scanf("%d\n",&N);
	for(int i=0;i<N;i++)
		Solve(i+1);
	return 0;
}
void Solve(int x)
{
	int n,s1=0,s2=0;
	list<int> L1,L2;
	scanf("%d\n",&n);

	for(int i=0;i<n;i++)
	{
		int t;
		scanf("%d ",&t);
		L1.push_back(t);
	}
	for(int i=0;i<n;i++)
	{
		int t;
		scanf("%d ",&t);
		L2.push_back(t);
	}
	L1.sort();
	L2.sort();
	list<int>::iterator i1=L1.begin();
	list<int>::reverse_iterator i2=L2.rbegin();
	for(;i1!=L1.end() && i2!=L2.rend();i1++,i2++)
		s1+=(*i1)*(*i2);
	cout<<"Case #"<<x<<": "<<s1<<endl;
	
}
