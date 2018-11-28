#include<cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int n_case;
	char mat[4][4];
	cin>>n_case;
	for(int i=0;i<n_case;i++)
	{
		int n_p=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>mat[j][k];
				if(mat[j][k]=='.')
				{
					n_p++;
				}
			}
		}
		/*
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cout<<mat[j][k];
			}
			cout<<endl;
		}
		cout<<endl;
		*/
		cout<<"Case #"<<i+1<<": ";
		
		bool fine=false;
		
		for(int j=0;j<4;j++)
		{
			char sym=mat[j][0];
			int cont=1;
			if(sym!='.')
			{
				for(int k=1;k<4;k++)
				{
					if(sym=='T')
					{
						sym=mat[j][1];
						cont++;
					}
					else
					{
						if( (mat[j][k]==sym || mat[j][k]=='T') && mat[j][k]!='.' )
						{
							cont++;
						}
					}
				}
			}
			if(cont==4)
			{
				cout<<sym<<" won\n";
				fine=true;
				break;
			}
		}
		
		if(!fine)
		{
			for(int j=0;j<4;j++)
			{	
				char sym=mat[0][j];
				int cont=1;
				if(sym!='.')
				{
					for(int k=1;k<4;k++)
					{
						if(sym=='T')
						{
							sym=mat[1][j];
							cont++;
						}
						else
						{
							if((mat[k][j]==sym || mat[k][j]=='T') && mat[j][k]!='.')
							{
								cont++;
							}
						}
					}
				}
				if(cont==4)
				{
					cout<<sym<<" won\n";
					fine=true;
					break;
				}
			}
		}
		
		if(!fine)
		{
			char sym=mat[0][0];
			int cont=1;
			if(sym!='.')
			{
				for(int k=1;k<4;k++)
				{
					if(sym=='T')
					{
						sym=mat[1][1];
						cont++;
					}
					else
					{
						if((mat[k][k]==sym || mat[k][k]=='T') && mat[k][k]!='.')
						{
							cont++;
						}
					}
				}
			}
			if(cont==4)
			{
					cout<<sym<<" won\n";
					fine=true;
			}
		}
		
		if(!fine)
		{
			char sym=mat[0][3];
			int cont=1;
			if(sym!='.')
			{
				for(int k=1;k<4;k++)
				{
					if(sym=='T')
					{
						sym=mat[1][2];
						cont++;
					}
					else
					{
						if((mat[k][3-k]==sym || mat[k][3-k]=='T') && mat[k][3-k]!='.')
						{
							cont++;
						}
					}
				}
			}
			if(cont==4)
			{
					cout<<sym<<" won\n";
					fine=true;
			}
		}
		
		if(!fine)
		{
			if(n_p!=0)
			{
				cout<<"Game has not completed\n";
			}
			else
			{
				cout<<"Draw\n";
			}
		}
	}
}
