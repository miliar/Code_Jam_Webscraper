#include<iostream>
#include<list>
#include<cstdio>

using namespace std;

void main()
{
	//list<comb> CombList;
	//list<oppo> OppoList;
	//list<char> Seq;
	int T,C,D,N;
	int c,d,n;
	char Combs[38][5];
	char Oppos[30][4];
	char arr[110];
	char out[110];
	//char OppoA, OppoB;
	int top;
	int exist,nextcell;
	cin>>T;
	for(int cases=1;cases <= T;cases++)
	{
		scanf("%d",&C);
		for(c=0;c<C;c++)
			scanf("%s",&Combs[c]);
		
		scanf("%d",&D);
		for(d=0;d<D;d++)
			scanf("%s",&Oppos[d]);

		scanf("%d",&N);
		scanf("%s",arr);

		top=0;
		out[0] = arr[0];

		for(n=1;n<N;n++)
		{
			out[++top] = arr[n];

			if(top == 0 )
				continue;
			
			exist=0;
			for(c=0;c<C;c++)
			{
				if((Combs[c][0] == out[top-1] && Combs[c][1] == out[top]) || (Combs[c][1] == out[top-1] && Combs[c][0] == out[top]) )
				{
					exist = 1;
					break;
				}
			}

			if(exist==1)
			{	out[--top]=Combs[c][2];
			}
			else
			{
				for(d=0;d<D;d++)
				{
					nextcell = -1;
					if(Oppos[d][0] == out[top] )
						nextcell = 1;
					else if(Oppos[d][1] == out[top] )
						nextcell = 0;
				
					if(nextcell != -1)
					{
						for(int l=0;l<=top-1;l++)
						{
							if(Oppos[d][nextcell] == out[l])
							{
								top = -1;
								exist = 1;
								break;
							}
						}
					
					}

					if(exist == 1 )
						break;
				}


			}

		}
		cout<<"Case #"<<cases<<": [";
		for(int t=0;t<=top;t++)
			cout<<out[t]<<((t==top)?"":", ");
		cout<<"]"<<endl;
		
	}

}