#include <iostream>

using namespace std;

int main()
{
	int r[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
	int t,T;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		int H,W;
		int i,j,k;
		int mat[100][100]={0};
		int pom[100][100]={0};
		int glob=1;
		cin>>H>>W;
		for(i=0;i<H;++i)
			for(j=0;j<W;++j)
				cin>>mat[i][j];
		for(k=0;k<=10000;++k)
			for(i=0;i<H;++i)
				for(j=0;j<W;++j)
					if(mat[i][j]==k)
					{
						int m_z=-1;
						int z;
						for(z=0;z<4;++z)
							if((i+r[z][0]>=0)&&(i+r[z][0]<H)&&(j+r[z][1]>=0)&&(j+r[z][1]<W)
								&&(pom[i+r[z][0]][j+r[z][1]]!=0)
								&&(mat[i][j]>mat[i+r[z][0]][j+r[z][1]]))
								if((m_z==-1)||(mat[i+r[m_z][0]][j+r[m_z][1]]>mat[i+r[z][0]][j+r[z][1]]))
									m_z=z;
						if(m_z==-1)
						{
							pom[i][j]=glob;
							++glob;
						}
						else
							pom[i][j]=pom[i+r[m_z][0]][j+r[m_z][1]];
					}
		int db[10000]={0};
		cout<<"Case #"<<t<<":"<<endl;
		int z=1;
		for(i=0;i<H;++i)
		{
			if(db[pom[i][0]]==0)
			{
				db[pom[i][0]]=z;
				++z;
			}
			cout<<(char)('a'+db[pom[i][0]]-1);
			for(j=1;j<W;++j)
			{
				if(db[pom[i][j]]==0)
				{
					db[pom[i][j]]=z;
					++z;
				}
				cout<<" "<<(char)('a'+db[pom[i][j]]-1);
			}
			cout<<endl;
		}
	}
	return 0;
}