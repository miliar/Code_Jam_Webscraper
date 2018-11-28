#include<iostream>
using namespace std;

int main()

{

	int t,i,j,k;
	cin>>t;
	string s[4];
	for( i = 0; i<t;i++)
	{
		int rowx[4],rowo[4];
		int columnx[4],columno[4];
		int d1x=0,d2x=0,d1o=0,d2o=0;
		for( j=0;j<4;j++)
		{
			rowo[j]=rowx[j]=columno[j]=columnx[j]=0;
		}
		cin>>s[0];
		cin>>s[1];
		cin>>s[2];
		cin>>s[3];
		int flag = 0;
		for( j=0;j<4;j++)
		{
			//cout<<s<<endl;
			for( k=0;k<4;k++)
			{
				
				if(s[j][k]=='.')
					flag=4;
				else if(s[j][k]=='O')
				{
					rowo[j]++;
					columno[k]++;
					if(j==k)
					{
						d1o++;
					}
					if(j+k==3)
					{
						d2o++;
					}
					if(rowo[j]==4)
					{
						flag=1;
						break;
					}
					if(columno[k]==4)
					{
						flag=1;
						break;
					}
					if(d1o==4)
					{
						flag=1;
						break;
					}
					if(d2o==4)
					{
						flag=1;
						break;
					}				
						
				}
				else if(s[j][k]=='X')
				{
					rowx[j]++;
					columnx[k]++;
					if(j==k)
					{
						d1x++;
					}
					if(j+k==3)
					{
						d2x++;
					}
					if(rowx[j]==4)
					{
						flag=2;
						break;
					}
					if(columnx[k]==4)
					{
						flag=2;
						break;
					}
					if(d1x==4)
					{
						flag=2;
						break;
					}
					if(d2x==4)
					{
						flag=2;
						break;
					}	
				}
				else if(s[j][k]=='T')
				{
					rowo[j]++;
					columno[k]++;
					rowx[j]++;
					columnx[k]++;
					if(j==k)
					{
						d1o++;
					}
					if(j+k==3)
					{
						d2o++;
					}
					if(j==k)
					{
						d1x++;
					}
					if(j+k==3)
					{
						d2x++;
					}
					//cout<<rowx[j]<<"GGG\n";
					if(rowo[j]==4)
					{
						flag=1;
						break;
					}
					if(columno[k]==4)
					{
						flag=1;
						break;
					}
					if(d1o==4)
					{
						flag=1;
						break;
					}
					if(d2o==4)
					{
						flag=1;
						break;
					}
					if(rowx[j]==4)
					{
						
						flag=2;
						break;
					}
					if(columnx[k]==4)
					{
						flag=2;
						break;
					}
					if(d1x==4)
					{
						flag=2;
						break;
					}
					if(d2x==4)
					{
						flag=2;
						break;
					}	
				}
			}
			if(flag==1 || flag==2)
				break;
		}
		//cout<<i<<" "<<j<<" "<<k<<endl;
		cout<<"Case #"<<i+1<<":";
		switch(flag)
			{
				case 0:
					cout<<" Draw\n";
					break;
				case 1:
					cout<<" O won\n";
					break;
				case 2:
					cout<<" X won\n";
					break;
				case 4:
					cout<<" Game has not completed\n";
					break;
			}
	
	}
	
}
