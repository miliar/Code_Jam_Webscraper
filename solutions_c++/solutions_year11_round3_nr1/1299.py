#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <bitset>

#define loop(i,n)	for(int i=0;i<(n);++i)
#define loope(i,n)	for(int i=0;i<=(n);++i)
#define loop1(i,n)	for(int i=1;i<(n);++i)

using namespace std;


void main()
{
	ifstream in ("input.in");
	ofstream out("output.out");

	double T;
	double Case=0;
	char ch[51][51];

	in>>T;
	
	for(Case = 1;Case<=T;Case++)
	{
		out<<"Case #"<<Case<<": "<<endl;
		int R,C;
		in>>R;
		in>>C;
		loop(i,R)
			loop(j,C)
			{
				in>>ch[i][j];		
			}

		bool flag1=false;
		bool flag2=false;

		loop(i,R-1)
		{
			loop(j,C-1)
			{
				if(ch[i][j]=='#')
				{
					if(		(ch[i][j]=='#'&&ch[i][j+1]=='#')
						&&	(ch[i+1][j]=='#'&&ch[i+1][j+1]=='#')
					)
					{
						ch[i][j]	='/';
						ch[i][j+1]	='\\';
						ch[i+1][j]	='\\';
						ch[i+1][j+1]='/';
					}
					else
					{
						flag2=true;
						out<<"Impossible"<<endl;
						break;
					}
				}
				if(flag2==false&&j==(C-2) && ch[i][j+1]=='#' && ch[i][j]!='#')
				{
					flag2=true;
					out<<"Impossible"<<endl;
					break;
				}
			}
			if (flag2==true) break;
		}
		if(flag2==false)
			{
				//check last line
				loop(j,C)
				{
					if(ch[R-1][j]=='#')
					{			
						flag2=true;
						out<<"Impossible"<<endl;
						break;
					}
				}
			}

		if(flag2==false)
			loop(i,R)
			{	
				loop(j,C)
				{
					out<<ch[i][j];
				}
				out<<endl;
			}
	}
	in.close();
	out.close();
}
