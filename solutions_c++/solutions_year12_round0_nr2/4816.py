#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
	clrscr();
	int t;
	cin>>t;
	ofstream myfile;
	myfile.open ("example.txt");
	int n,s,p,a[100],c=0;
	for(int j=0;j<t;j++)
	{
		c=0;
		cin>>n>>s>>p;
		for(int i=0;i<n;i++)
		cin>>a[i];
		for(i=0;i<n;i++)
		{
			if(a[i]/3>=p)
			c++;
			else if((a[i]+1)/3>=p&&(a[i]-1)/3>=0)
			c++;
			else if((a[i]+2)/3>=p&&(a[i]-1>=0))
			c++;
			else if(((a[i]+3)/3>=p&&s>0&&(a[i]-2)>=0)||((a[i]+4)/3>=p&&s>0)&&(a[i]-2)>=0)
			{
				c++;
				s--;
			}
		}
		myfile<<"Case #"<<j+1<<": "<<c<<endl;
	}
	getch();
}