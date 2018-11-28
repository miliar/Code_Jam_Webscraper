#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	int n;
	fin>>n;
	for (int i=1; i<=n; i++)
	{
		int m,ans(0),o(1),b(1),oc,bc,deltao(0),deltab(0);
		char c,cb('a');
		bool flag=false;
		fin>>m;
		for (int i=0; i<m; i++)
		{
			fin.ignore(1);
			fin>>c;
			if (c==cb||!flag)
			{
				if (c=='O') 
				{
					cb='O';
					fin>>oc;
					deltao+=abs(oc-o)+1;
					o=oc;
					if (i==m-1)
					{
						ans+=deltao;
					}
				}
				else
				{
					cb='B';
					fin>>bc;
					deltab+=abs(bc-b)+1;
					b=bc;
					if (i==m-1)
					{
						ans+=deltab;
					}
				}
				
			}
			else
			{	
				if (c=='O') 
				{
					cb='O';
					fin>>oc;
					deltao+=abs(oc-o);
					if (deltao>deltab)
					{
						ans+=deltao+1;
						deltab=deltab-deltao-1;
						deltao=0;
					}
					else
					{
						ans+=deltab+1;
						deltao=0;
						deltab=-1;
					}
					if (i==m-1)
					{
						ans+=deltao;
					}

					o=oc;
				}
				else
				{
					cb='B';
					fin>>bc;
					deltab+=abs(bc-b);
					if (deltab>deltao)
					{
						ans+=deltab+1;
						deltao=deltao-deltab-1;
						deltab=0;
					}
					else
					{
						ans+=deltao+1;
						deltao=-1;
						deltab=0;
					}
					if (i==m-1)
					{
						ans+=deltab;
					}

					b=bc;
				}
				

			}
		flag=true;	
		}
			fout<<"Case #"<<i<<": "<<ans<<endl;
	}

	fin.close();
	fout.close();
	return 0;
}