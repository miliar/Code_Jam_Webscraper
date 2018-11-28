#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>


int count(int l,int d,char dict[25][11],char test[10][27])
{       int cnt=0,flag=0;char check[25][11];

	for(int i=0;i<d;i++)
	{       flag=0;
		for(int j=0;j<l;j++)
		{	for(int k=0;test[j][k]!='\0';k++)
			{	if(dict[i][j]==test[j][k])
				{	flag=flag+1;
				}
			}
		}
		if(flag==l)
		{	cnt++;
		}
	}


	cout<<cnt;
	return cnt;
}

void main()
{       clrscr();
	fstream f,o;
	f.open("alinput.in",ios::in);
	o.open("aloutput.out",ios::out|ios::app);
	int t,i=0,l,d,n,j=0,k,cnt=0;
	char ch,dict[25][11],test[10][27];

	f>>t;
	cout<<t;
	l=t;
	f>>t;
	cout<<t;
	d=t;
	f>>t;
	cout<<t;
	n=t;
	cout<<endl;
	for(i=0;i<d;i++)
	{
		for(j=0;j<l;j++)
		{	f>>ch;
			dict[i][j]=ch;
		}
		dict[i][j]='\0';
	}
	for(i=0;i<d;i++)
	{	cout<<dict[i]<<endl;
	}
	j=0;k=0;
	for(i=1;i<=n;i++)
	{       for(j=0;j<10;j++)
		{	for(k=0;k<26;k++)
			{	test[j][k]=0;
			}
		}
		j=0;k=0;
		while(j<l)
		{
			{	f>>ch;
				if(ch=='(')
				{	f>>ch;
					while(ch!=')')
					{ 	test[j][k]=ch;
						f>>ch;
						k++;
					}
					test[j][k]='\0';
					j++;k=0;

				}
				else if(ch!='(' && ch!=')')
				{	test[j][k]=ch;
					test[j][1]='\0';
					j++;k=0;

				}

			}
		}

		for(j=0;j<l;j++)
		{	cout<<test[j]<<" ";
		}

		cnt=count(l,d,dict,test);
		cout<<endl<<endl;
		//cout<<"\n\nakhil"<<cnt;
		o<<"Case #"<<i<<": ";
		o<<cnt;
		o<<endl;
	}

	o.close();
	f.close();
	getch();
}