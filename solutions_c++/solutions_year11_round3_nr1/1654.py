#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("al.out");
    char mat[60][60];
    int i,t,r,c,j,k=0;
    bool flag;
    cin>>t;
    while(t--)
    {
    	flag=1;
    	cin>>r>>c;
    	for(i=0;i<r;++i)
    	for(j=0;j<c;++j)
    		cin>>mat[i][j];
		for(i=0;i<r;++i)
		{
			if(flag)
				for(j=0;j<c;++j)
				{
					if(mat[i][j]=='#')
					{
						if(i+1==r||j+1==c)
						{
							flag=0;
							break;
						}
						else if(mat[i][j+1]!='#'||mat[i+1][j]!='#'||mat[i+1][j+1]!='#')
						{
							flag=0;
							break;
						}
						else
						{
							mat[i][j]='/';
							mat[i+1][j+1]='/';
							mat[i][j+1]=mat[i+1][j]='\\';
						}
					}
				}
		}
		cout<<"Case #"<<++k<<":"<<endl;

		if(flag)
		{
			for(i=0;i<r;++i)
			{
				for(j=0;j<c;++j)
					cout<<mat[i][j];
				cout<<endl;
			}
		}
		else cout<<"Impossible"<<endl;
    }
    return 0;
}
