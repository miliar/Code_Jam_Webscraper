//CODEJAM

#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main()
{
	//vars
	ifstream f ("A-large.in");
	ofstream g ("A-large.out");
	int t,tt;
	int n,q,a,b,c;
	string s;
	char s2[1000];
	static int dyn[2000][200];
	string eng[200];
	map <string,int> M;
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> n;
			f.getline(s2,1000,'\n');
			n++;
				for (a=1; a<n; a++)
				{
					f.getline(s2,1000,'\n');
					eng[a]=s2;
					M[eng[a]]=a;
				}
			f >> q;
			f.getline(s2,1000,'\n');
			//dynamic
			memset(dyn,100,sizeof(dyn));
				for (a=1; a<n; a++)
					dyn[0][a]=0;
				for (a=0; a<q; a++)
				{
					f.getline(s2,1000,'\n');
					s=s2;
						for (b=1; b<n; b++)
							if (M[s]==b)	//must switch
							{
								for (c=1; c<n; c++)
									if (c!=b)
										if (dyn[a+1][c]>dyn[a][b]+1)
											dyn[a+1][c]=dyn[a][b]+1;
							}
							else				//don't switch
								if (dyn[a+1][b]>dyn[a][b])
									dyn[a+1][b]=dyn[a][b];
				}
			//output
			b=999999;
				for (a=1; a<n; a++)
					if (dyn[q][a]<b)
						b=dyn[q][a];
			cout << b << endl;
			g << "Case #" << t << ": " << b << endl;
			//clear map
				for (a=1; a<n; a++)
					M[eng[a]]=0;
		}
	return(0);
}