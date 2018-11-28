#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>
#include <bitset>

using namespace std;

int doForOne(vector<int> t,int l, int h)
{
	for(int i=l;i<=h;i++)
	{
		int flag=1;
		for(int j=0;j<t.size();j++)
			if(t[j]%i != 0 && i%t[j] != 0)
			{
				flag=0;
				break;
			}
		if(flag==1)
			return i;
	}
	return -1;
}
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	
	int T;
	cin>>T;
	int R,C;
	for(int i=1;i<=T;i++)
	{
		int N,L,H;
		vector<int> x;
		cin>>N>>L>>H;
		for(int i=0;i<N;i++)
		{
			int t;
			cin>>t;
			x.push_back(t);
		}
		int val = doForOne(x,L,H);
		printf("Case #%d: ",i);
		if(val==-1)
			printf("NO");
		else
			printf("%d",val);
		if(i!=T)
			printf("\n");
	}
	return 0;
}
