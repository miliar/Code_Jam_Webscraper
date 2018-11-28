#include<iostream>
#include<stdio.h>
#include<fstream>
#include<cstdlib>
#include<cmath>
#include<queue>
using namespace std;
queue<int>Blue;
queue<int>Orange;
queue<char>UU;
int main()
{
	int T,Time,i,ca,n,y,temp,OKO,OKB;
	int B,O;
	char x;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(ca=1;ca<=T;++ca)
	{
		while(!Blue.empty())
		Blue.pop();
		while(!Orange.empty())
		Orange.pop();
		while(!UU.empty())
		UU.pop();
		Time=0;
		OKO=0;
		OKB=0;
		O=1;
		B=1;
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			cin>>x>>y;
			if(x=='B')
			{
				Blue.push(y);
				UU.push('B');
			}
			else if(x=='O')
			{
				Orange.push(y);
				UU.push('O');
			}
		}
		while(!(Blue.empty()&&Orange.empty()))
		{
			Time++;
			if(UU.front()=='B')
			{
				if(B>Blue.front())B--;
				else if(B<Blue.front())B++;
				else if(B==Blue.front())
				{
					Blue.pop();
					UU.pop();
					OKB=0;
				}
				if(!Orange.empty())
				{
					if(O>Orange.front())O--;
					else if(O<Orange.front())O++;
				}
			}
			else
			{					
				if(O>Orange.front())O--;
				else if(O<Orange.front())O++;
				else if(O==Orange.front())
				{
						Orange.pop();
						UU.pop();
						OKO=0;
				}
				if(!Blue.empty())
				{
					if(B>Blue.front())B--;
					else if(B<Blue.front())B++;
				}
			}
		}
		printf("Case #%d: %d\n",ca,Time);
	}
	return 0;
}
