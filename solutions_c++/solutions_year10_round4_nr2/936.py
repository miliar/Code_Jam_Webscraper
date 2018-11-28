
#include<iostream>
using namespace std;


int M[1100],tick[11100];
int pt[1100];
int need[1100];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int T;
	cin>>T;
	int cas=1;
	while(T--)
	{
	//	init();
		int P;
		cin>>P;

		memset(pt,-1,sizeof(pt));
		int s=0,e=(1<<P)/2;
		while(e-s>1)
		{
			int w=e;
			for(int i=s;i<e;i+=2)
			{
				pt[i]=w;
				pt[i+1]=w++;
			}
			s=e;
			e=w;
		}

		for(int i=0;i<1<<P;i++)
		{
			cin>>M[i];
		}

		int id=0;
		for(int i=1;i<=P;i++)for(int j=0;j<1<<(P-i);j++)
		{
			cin>>tick[id];
			id++;
		}

		memset(need,0,sizeof(need));
		int res=0;
		for(int i=0;i<1<<P;i++)
		{
			int id2=i/2;
			while(M[i])
			{
				id2=pt[id2];
				M[i]--;
			}
			while(id2!=-1)
			{
				if(!need[id2])
				{
					need[id2]=1;
					res++;
				}
				id2=pt[id2];
			}
		}


		cout<<"Case #"<<cas++<<": "<<res<<'\n';




	}
	return 0;
}