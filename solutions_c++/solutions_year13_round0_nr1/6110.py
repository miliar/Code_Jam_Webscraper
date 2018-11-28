#include<iostream>
#include<fstream>

using namespace std;

int check (char ch,int,int);

char a[5][5];

int main()
{
	
	int T;
		freopen("A-large.in","r",stdin);
	freopen("output7.in","w",stdout);
	
	cin>>T;
	cin.ignore();
	int no=T;
	while(T--)
	{
		
		int i=0,j=0,h=0,g=0,z=0,countx=0,county=0;;
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				a[i][j]=' ';
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
				if(a[i][j]=='.')
				z=1;		
			}
			cin.ignore();
		}
		
	
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
//				cout<<"i ="<<i<<endl<<"j is "<<j<<endl;
//				cout<<"Character is "<<a[i][j]<<endl;
			if(i==0||j==0)
			{
				if(a[i][j]=='X')
				{
					if(h==0)
					h=check('X',i,j);
				//	cout<<"h is "<<h<<endl;				
				}
				else if(a[i][j]=='O')
				{
						if(g==0)
						g=check('O',i,j);		
				}
				else if(a[i][j]=='T')
				{
					if(h==0)
					h=check('X',i,j);
				
					if(g==0)
					g=check('O',i,j);					
				}			
			}
			}
			if(h==1&&g==1)
			break;			
		}
		
				if(h==1)
				cout<<"Case #"<<no-T<<": "<<"X won "<<endl;
				else if(g==1)
				cout<<"Case #"<<no-T<<": "<<"O won"<<endl;
				else if(z==1)
				cout<<"Case #"<<no-T<<": "<<"Game has not completed"<<endl;
				else 
				cout<<"Case #"<<no-T<<": "<<"Draw"<<endl;
			
	}
}


int check (char ch,int i,int j)
{
	int f=0,r,s,cx1=0,cx2=0,di1=0,di2=0;
	if(j==0)
	{
//		cout<<endl<<"cHECKING rOW "<<endl;
		for(r=0;r<4;r++)
		{
			if(a[i][r]==ch||a[i][r]=='T')
			cx1++;
		}
	}
	if(i==0)
	{
//		cout<<endl<<"cHECKING coloumn "<<endl;
		for(r=0;r<4;r++)
		{
			if(a[r][j]==ch||a[r][j]=='T')
			cx2++;
		}	
	}
	
	if(i==0&&j==0)
	{
//		cout<<endl<<"cHECKING diagonal "<<endl;
		for(r=0;r<4;r++)
		{
			for(s=0;s<4;s++)
			{
				if(r==s)
				{
					if(a[r][s]=='T'||a[r][s]==ch)
					di1++;
				}
			}
		}
	}
	
	if(i==0&&j==3)
	{
//		cout<<endl<<"cHECKING diagonal 2 "<<endl;
		for(r=0;r<4;r++)
		{
			for(s=0;s<4;s++)
			{
				if(r+s==3)
				{
					if(a[r][s]=='T'||a[r][s]==ch)
					di2++;
				}
			}
		}
	}
//	cout<<endl<<cx1<<" "<<cx2<<" "<<di1<<" "<<di2<<endl;
	if(cx1==4||cx2==4||di1==4||di2==4)
	f=1;
	
	
				
				return(f);
}
