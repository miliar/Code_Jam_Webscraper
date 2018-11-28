#include <iostream>
#include <fstream>

using namespace std;
char a[60][60];
void main()
{   ofstream outfile( "A-large.out" );
    ifstream infile( "A-large.in" );
    int T, R, C ,i, j, k, l, t;
    infile>>T;
    for(i=1;i<=T;i++)
    {
        infile>>R>>C;
        for (j=0;j<R;j++)infile>>a[j];
        bool flag=true;
        for (j=0;j<R;j++)
		{
            for (k=0;k<C;k++)
            {
                if (a[j][k]=='#')
                {
                    if (a[j][k+1]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#')
                    { a[j][k] = '/'; a[j][k+1] = '\\';
                      a[j+1][k] ='\\'; a[j+1][k+1] = '/';
                    }
                    else
                    { outfile<<"Case #"<<i<<":"<<endl<<"Impossible\n";flag=false;break;}
                }

            }
			if (flag==false)break;
		}
        if (flag == true)
        {  outfile<<"Case #"<<i<<":"<<endl;
           for (j=0;j<R;j++) outfile<<a[j]<<endl;
        }
    }

}