#include<iostream>
#define MAXN 100
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		char col[MAXN];
		int btn[MAXN];
		cin>>n;
		int onext=0, oseq=n;
		int bnext=0, bseq=n;
		for(int j=0;j<n;j++)
		{
			cin>>col[j]>>btn[j];
			if(col[j]=='O' && onext==0)
			{
				onext=btn[j];
				oseq=j;
			}
			else if(col[j]=='B' && bnext==0)
			{
				bnext=btn[j];
				bseq=j;
			}
		}
		int opos=1,bpos=1;
		int pushed=0;
		int time=0;
		bool opushed=false;
		while(pushed!=n)
		{
			if(onext!=0)
			{
				//decide a move for o
				if(opos>onext)
				{
					opos--;
				}
				else if(opos<onext)
				{
					opos++;
				}
				else
				{
					if(bseq==n || oseq<bseq)
					{
						//push a btn
						pushed++;
						opushed=true;
						//find the next btn for o
						do
						{
							oseq++;
						}
						while(col[oseq]!='O' && oseq<n);
						if(oseq==n)
							onext=0;
						else
							onext=btn[oseq];
					}
				}
			}
			if(bnext!=0 && pushed<n) 
			{
				//decide a move for b
				if(bpos>bnext)
				{
					bpos--;
				}
				else if(bpos<bnext)
				{
					bpos++;
				}
				else if(!opushed)
				{
					if(oseq==n || bseq<oseq)
					{
						//push a btn
						pushed++;
						//find the next btn for o
						do
						{
							bseq++;
						}
						while(col[bseq]!='B' && bseq<n);
						if(bseq==n)
							bnext=0;
						else
							bnext=btn[bseq];
					}
				}
			}
			opushed=false;
			time++;
		}
		cout<<"Case #"<<i<<": "<<time<<endl;
	}
}
