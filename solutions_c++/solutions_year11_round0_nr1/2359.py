#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
struct A{int o,b,i,s;}e,que[2000000],t;
int n;
int p[123];
char s[123];
int bj[123][123][123];
int ok(int z)
{
	return z>0&&z<101;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tes;
	cin>>tes;
	for(int cas=1;cas<=tes;cas++)
	{
		cin>>n;
		memset(bj,0,sizeof(bj));
		for(int i=0;i<n;i++)
		{
			cin>>s[i]>>p[i];
		}
		e.b=1,e.o=1,e.s=0;
		e.i=0;
		bj[0][1][1]=1;
		int l=0,r=0;
		que[r++]=e;
		while(1)
		{
			e=que[l++];
			//cout<<e.i<<endl;
			if(e.i==n)break;
			for(int i=-1;i<2;i++)
				for(int q=-1;q<2;q++)
				{
					t=e;
					t.s++;
					t.b+=i;
					t.o+=q;
					if(s[t.i]=='B')
					{
						if(e.b==p[t.i])
						{
							t.b=e.b;
							t.i++;
						}
					}
					else if(e.o==p[t.i])
					{
						t.o=e.o;
						t.i++;
					}
					if(ok(t.o)&&ok(t.b)&&!bj[t.i][t.o][t.b]++)que[r++]=t;
				}
		}
		printf("Case #%d: ",cas);
		cout<<e.s<<endl;
	}
}