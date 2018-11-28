#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

struct line
{
	int a;
	int b;
};

bool small(line a , line b)
{
	return a.a<b.a;
}

line ls[1100];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	for(int i=0;i<T;++i)
	{
		int n;
		cin>>n;
		int cnt =0;
		for(int j=0;j<n;++j)
		{
			cin>>ls[j].a>>ls[j].b;
		}
		sort(ls,ls+n,small);
		for(int j=1;j<n;++j)
		{
			for(int k=j-1;k>=0;--k)
			{
				if(ls[j].b<ls[k].b)cnt++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
}