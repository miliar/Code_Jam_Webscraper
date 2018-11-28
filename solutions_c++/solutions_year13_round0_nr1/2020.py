#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int rx[4],ro[4];
	int cx[4],co[4];
	int lrx,lro,rlx,rlo;
	int rt[4];
	int ct[4];
	int lrt,rlt;
	char g;
	int incom;
	for(int hh=1; hh<=t; hh++)
	{
		lrx = lro = rlx = rlo =0;
		lrt = rlt =0;
		incom = 0;
		for(int i=0; i<4; i++)
		{
			cx[i] = 0;
			co[i] = 0;
			ct[i] = 0;
		}
			
		for(int i=0; i<4; i++)
		{
			rx[i] = 0;
			ro[i] = 0;
			rt[i] = 0;

			for(int j=0; j<4; j++)
			{
				cin>>g;
				if(i==j)
				{
					if(g=='X')
						lrx++;
					else if(g=='O')
						lro++;
					else if(g=='T')
					{
						
						lrx++; lro++;lrt++;
					}		
				}
				else if(i+j==3)
				{
					if(g=='X')
						rlx++;
					else if(g=='O')
						rlo++;
					else if(g=='T')
					{
						rlx++; rlo++;rlt++;
					}		
				}
							
				if(g=='.')
					incom=1;
				else if(g=='O')
				{
					ro[i]++;
					co[j]++;
				}
				else if(g=='X')
				{
					rx[i]++;
					cx[j]++;
				}
				else
				{
					ro[i]++;
					co[j]++;		
					rx[i]++;
					cx[j]++;
					ct[j]++;
					rt[i]++;
				}
			}
		}
		for(int i=0; i<4; i++)
		{
			if((rx[i]==4 && rt[i]<=1) || (cx[i]==4 && ct[i]<=1))
			{
				cout<<"Case #"<<hh<<": X won\n";
				goto lst;
			}
			else if((ro[i]==4 && rt[i]<=1)|| (co[i]==4 && ct[i]<=1))
			{
				cout<<"Case #"<<hh<<": O won\n";
				goto lst;
			}
		}
		if((lro==4 && lrt<=1) || (rlo==4 && rlt<=1) )
		{
			cout<<"Case #"<<hh<<": O won\n";
			goto lst;
		}
		else if((lrx==4 && lrt<=1)|| (rlx==4&& rlt<=1) )
		{
			cout<<"Case #"<<hh<<": X won\n";
			goto lst;		
		}
		if(incom==1)
			cout<<"Case #"<<hh<<": Game has not completed\n";
		else
			cout<<"Case #"<<hh<<": Draw\n";
		lst:
		;	
	}
	return 0;
}			
