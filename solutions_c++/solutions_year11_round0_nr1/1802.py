#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
ifstream in("A-large.in");
ofstream out("A-large.out");
//ifstream in(stdin);
//ofstream out(stdout);
struct node
{
	char col;
	int pos;
	//node(char c,int p):col(c),pos(p){}
}seq[201];

int o[101];
int b[101];

int main()
{
	int t;
	int k,oi,bi,opos,bpos;
	in>>t;
	for(int ii=1;ii<=t;ii++)
	{
		oi = bi = 0;
		opos = bpos = 1;
		in>>k;
		for (int i=0;i<k;i++)
		{
			in>>seq[i].col>>seq[i].pos;
			if (seq[i].col == 'O')
				o[oi++] = seq[i].pos;
			else
				b[bi++] = seq[i].pos;
		}
		int ans=0;
		int nexto,nextb;
		int i = 0,j = 0;
		nexto = nextb = -1;
		int p = 0;

		if (oi > 0)
			nexto = o[i++];
		if(bi > 0)
			nextb = b[j++];

		while (p < k)
		{
			node target = seq[p++];

			if (target.col == 'O')
			{
				int cost = abs(target.pos - opos) + 1;
				ans+=cost;
				opos = target.pos;
				if (i < oi)
					nexto = o[i++];
				else
					nexto = -1;

				if (nextb != -1)
				{
					int need = abs(nextb - bpos);
					if(need <= cost)
						bpos = nextb;
					else
					{
						if(nextb > bpos)
							bpos +=cost;
						else
							bpos -=cost;
					}
				}
			}
			else
			{
				int cost = abs(target.pos - bpos) + 1;
				ans+=cost;
				bpos = target.pos;
				if(j<bi)
					nextb = b[j++];
				else
					nextb = -1;
				if (nexto != -1)
				{
					int need = abs(nexto - opos);
					if(need <= cost)
						opos = nexto;
					else
					{
						if(nexto > opos)
							opos +=cost;
						else
							opos -=cost;
					}
				}
				
			}

		}
		out<<"Case #"<<ii<<": "<<ans<<endl;
	}
	//system("pause");
	return 0;
}