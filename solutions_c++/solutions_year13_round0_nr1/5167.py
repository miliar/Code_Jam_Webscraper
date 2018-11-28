#include<fstream>
#include<string>
using namespace std;
const int M1 = 5;
ifstream fin("A-large.in");
ofstream fout("aout.txt");

char mat[M1][M1];
void work(int i,int j,int&cx,int& co);
int main()
{
    int T;
	fin>>T;
	for(int c=1;c<=T;++c)
	{   for(int i=0;i!=4;++i)
	        fin>>mat[i];
		int cx=0,co=0;
		bool bx=false,bo=false,fini=true;
		for(int i=0;i!=4&&!bx&&!bo;++i)
		{   cx=0;co=0;
		    for(int j=0;j!=4&&!bx&&!bo;++j)
		    {   if(mat[i][j]=='.') fini = 0;
			    work(i,j,cx,co);
			}
			if(co>=4)
			    bo = 1;
			if(cx>=4)
				bx = 1;
		}
		for(int j=0;j!=4&&!bx&&!bo;++j)
		{   cx=0;co=0;
		    for(int i=0;i!=4&&!bx&&!bo;++i)
		    {   if(mat[i][j]=='.') fini = 0;
			    work(i,j,cx,co);
			}
			if(co>=4)
			    bo = 1;
			if(cx>=4)
				bx = 1;
		}
		cx=co=0;
		for(int i=0;i!=4&&!bx&&!bo;++i)
		{   if(mat[i][i]=='.') fini = 0;
		    work(i,i,cx,co);
		}
		if(co>=4)
			bo = 1;
		if(cx>=4)
			bx = 1;
		cx=co=0;
		for(int i=0;i!=4&&!bx&&!bo;++i)
		{   if(mat[i][3-i]=='.') fini = 0;
		    work(i,3-i,cx,co);
		}
		if(co>=4)
			bo = 1;
		if(cx>=4)
			bx = 1;
	    fout<<"Case #"<<c<<": ";
		if(bx)
		    fout<<"X won\n";
		else if(bo)
		    fout<<"O won\n";
		else if(fini)
		    fout<<"Draw\n";
		else
		    fout<<"Game has not completed\n";
	}
	
    return 0;
}
void work(int i,int j,int&cx,int& co)
{
    if(mat[i][j]=='O')
		++co;
	else if(mat[i][j]=='X')
		++cx;
	else if(mat[i][j]=='T')
	{   ++co;++cx;
	}
}