//CODEJAM - A

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//vars
	ifstream f ("A-large.in");
	ofstream g ("A-large.out");
	int t,tt,n,v,a,b,c,x,tmp;
	int dyn[10005][2];
	bool gate[10005];
	bool ch[10005];
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//init
			memset(dyn,100,sizeof(dyn));
			tmp=dyn[0][0];
			//input
			f >> n >> v;
				for (a=0; a<(n-1)/2; a++)
					f >> gate[a] >> ch[a];
				for (a=(n-1)/2; a<n; a++)
				{
					f >> b;
					dyn[a][b]=0;
				}
			//dynamic
				for (a=(n-1)/2-1; a>=0; a--)
					for (b=0; b<2; b++)
						if (dyn[a*2+1][b]!=tmp)
							for (c=0; c<2; c++)
								if (dyn[a*2+2][c]!=tmp)
								{
									//change
									if (ch[a])
									{
										if (gate[a])
											x=((b||c)?1:0);
										else
											x=((b&&c)?1:0);
										if (dyn[a][x]>dyn[a*2+1][b]+dyn[a*2+2][c]+1)
											dyn[a][x]=dyn[a*2+1][b]+dyn[a*2+2][c]+1;
									}
									//don't change
									if (gate[a])
										x=((b&&c)?1:0);
									else
										x=((b||c)?1:0);
									if (dyn[a][x]>dyn[a*2+1][b]+dyn[a*2+2][c])
										dyn[a][x]=dyn[a*2+1][b]+dyn[a*2+2][c];
								}
			//output
				if (dyn[0][v]==tmp)
				{
					cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
					g << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
				}
				else
				{
					cout << "Case #" << t << ": " << dyn[0][v] << endl;
					g << "Case #" << t << ": " << dyn[0][v] << endl;
				}
		}
	return(0);
}