#include<iostream>
#include<string>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<deque>
using namespace std;


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int CAS,Te=1;
	cin>>CAS;
	while(CAS--)
	{
		int L,P,C;
		cin>>L>>P>>C;
		
		int fuck=0;
		int ans =ceil(log(double(P)/double(L))/log(double(C)))-1;
		while (ans>0)
		{
			ans=(ans)/2;
			fuck++;
		}
		
		
		printf("Case #%d: ",Te++);
		printf("%d\n",fuck);
	}
}