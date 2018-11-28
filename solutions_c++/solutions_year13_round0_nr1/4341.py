#include<iostream>
using namespace std;

int main()
{
	int test,x,o,t,x1,o1,t1,x2,o2,t2,dot,flag;
	char a[4][4];

	cin>>test;

	for(int m=1;m<=test;m++)
	{
		cout<<"Case #"<<m<<": ";

		dot=flag=0;

		for(int i=0;i<4;i++)
			{ 
				x=o=t=0;

				for(int j=0;j<4;j++)
					{ 
						cin>>a[i][j];
				  
						if(a[i][j]=='X')
							x++;
				  
						if(a[i][j]=='O')
							o++;
				  
						if(a[i][j]=='T')
							t++;
						
						if(a[i][j]=='.')
							dot++;

					}

		if((x==3&&t==1)||(x==4))
		{ cout<<"X won"<<endl; flag=1;}

		if((o==3&&t==1)||(o==4))
		{ cout<<"O won"<<endl; flag=1;}

		}

		if(flag==1)
			continue;

		x1=x2=o1=o2=t1=t2=flag=0;

		for(int i=0;i<4;i++)
			{ 
				x=o=t=0;

				for(int j=0;j<4;j++)
					{ 
						if(a[j][i]=='X')
							x++;
				  
						if(a[j][i]=='O')
							o++;
				  
						if(a[j][i]=='T')
							t++;

					}

						if((x==3&&t==1)||(x==4))
							{ cout<<"X won"<<endl; flag=1;break; }

						if((o==3&&t==1)||(o==4))
							{ cout<<"O won"<<endl; flag=1;break; }


				if(a[i][i]=='X')
					x1++;
				if(a[i][i]=='O')
					o1++;
				if(a[i][i]=='T')
					t1++;

				if(a[i][3-i]=='X')
					x2++;
				if(a[i][3-i]=='O')
					o2++;
				if(a[i][3-i]=='T')
					t2++;

		}
		if(flag==1)
			continue;


		if((x1==3&&t1==1)||(x1==4))
		{ cout<<"X won"<<endl; continue; }

		if((o1==3&&t1==1)||(o1==4))
		{ cout<<"O won"<<endl; continue; }

		if((x2==3&&t2==1)||(x2==4))
		{ cout<<"X won"<<endl; continue; }

		if((o2==3&&t2==1)||(o2==4))
		{ cout<<"O won"<<endl; continue; }

		if(dot==0)
		 cout<<"Draw"<<endl;
		else
		 cout<<"Game has not completed"<<endl;

		
	}

//	system("pause");

	return 0;
}


			




				  

