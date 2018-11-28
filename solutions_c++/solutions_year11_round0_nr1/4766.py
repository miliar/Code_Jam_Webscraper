#include <iostream>

using namespace  std;

int O[101],B[101];
int On,Bn,time,N,po,pb;
bool S[101];

int fbs(int a)
{
	return a>0?a:-a;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int T,i,j,p;
	char c;

	cin>>T;
	for (i=1;i<=T;++i)
	{
		cin>>N;
		On=Bn=0;
		for (j=0;j<N;++j)
		{
			cin>>c>>p;
			if (c=='O')
			{
				O[On++]=p;
				S[j]=0;
			}else
			{
				B[Bn++]=p;
				S[j]=1;
			}
		}
		time=0;
		po=pb=1;
		int curo=0,curb=0;
		p=0;
		while (p<N)
		{
			if (S[p]==0)
			{
				int tp=fbs(O[curo]-po)+1;
				time+=tp;
				po=O[curo];
				if (tp>=fbs(B[curb]-pb))
				{
					pb=B[curb];
				}else
				{
					pb=(B[curb]>pb)?(pb+tp):(pb-tp);
				}
				curo++;
			}else
			{
				int tp=fbs(B[curb]-pb)+1;
				time+=tp;
				pb=B[curb];
				if (tp>=fbs(O[curo]-po))
				{
					po=O[curo];
				}else
				{
					po=(O[curo]>po)?(po+tp):(po-tp);
				}
				curb++;
			}
			p++;
		}
		cout<<"Case #"<<i<<": "<<time<<endl;

	}
}