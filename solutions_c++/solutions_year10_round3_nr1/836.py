#include<iostream>
#include<queue>
#include<fstream>
#include<vector>
using namespace std;
#define N 1003
struct node
{
	int l,r;
}wires[N];
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A.txt","w",stdout);
	int T;
	cin>>T;
	int cases=0;
	int i,j;
	while(T-->0)
	{
		cases++;
		int counts=0;
		cout<<"Case #"<<cases<<": ";
		int n;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>wires[i].l>>wires[i].r;
		}

		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(wires[i].l>wires[j].l&&wires[i].r<wires[j].r)
					counts++;
				else if(wires[i].l<wires[j].l&&wires[i].r>wires[j].r)
					counts++;
			}
		}

		cout<<counts<<endl;
	}

	return 0;
}