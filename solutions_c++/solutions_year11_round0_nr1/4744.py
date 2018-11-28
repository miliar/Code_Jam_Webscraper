#include<iostream>
#include<cstdio>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	int t,O,B,N,to,tb,last;
	char c;
	scanf("%d",&t);
	for(int ca = 1;ca<=t;ca++)
	{
		scanf("%d",&N);
		O=1;B=1;last=0;
		to=0;tb=0;
		while(N--)
		{
			int but;
			cin>>c>>but;
			if(c=='B')
			{
				tb = max(last,tb+abs(B-but))+1;
				B=but;
				last = tb;
			}
			else
			{
				to = max(last,to+abs(O-but))+1;
				O=but;
				last = to;
			}
		}
		printf("Case #%d: %d\n",ca,max(to,tb));
	}
	return 0;
}