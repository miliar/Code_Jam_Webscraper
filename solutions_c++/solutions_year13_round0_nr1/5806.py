#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>
char A[100];
void main()
{
clrscr();
ifstream infile ("A100.txt");
ofstream outfile("A1ans.txt");
char A[100];
infile.getline(A,100);
int T;
T=atoi(A);

for(int i=1;i<=T;i++)
	{
	 infile.getline(::A,100);
	char A[5][5];
	for(int j=0;j<4;j++)
	       {	infile.getline(A[j],6);
		cout<<A[j]<<endl;

		}
	       if(i%10==0)
			getch();

       int x=0,o=0; char ans=0;int num=0;
       for(int p=0;p<4;p++)
		{
		x=0,o=0;
		for(int k=0;k<4;k++)
			{
			 if(A[p][k]=='X')
				 { x++; num++;}
			 else if(A[p][k]=='O')
				{o++; num++;}
			 else if(A[p][k]=='T')
				{
				o++;x++;num++;
				}
			 }

		if (x==4)
			ans='x';
		else if(o==4)
			ans='o';
	       x=0,o=0;
	       for(int h=0;h<4;h++)
			{
			if(A[h][p]=='X')
				x++;
			else if(A[h][p]=='O')
				o++;
			else if(A[h][p]=='T')
				{
				o++;x++;
			 }	}
	       if(x==4)
			ans='x';
	       else if(o==4)
			ans='o';
			x=0;o=0;
		if(p==0||p==3)
			for(int u=0;u<4;u++)
				{
				if(p==0)
					{
					if(A[u][u]=='X')
						x++;
					else if(A[u][u]=='O')
						o++;
					else if(A[u][u]=='T')
						{
						x++;o++;
						}
				       }
				    }

			if(x==4)
				ans='x';
			else if(o==4)
				ans='o';
			 x=0;o=0;
			if(p==3)
				{
				for(int y=0,j=3;y<4,j>=0;y++,j--)
					{
					if(A[y][j]=='X')
						x++;
					else if(A[y][j]=='O')
						o++;
					else if(A[y][j]=='T')
						{
						x++;o++;
						}
					}
				}
			if(x==4)
				ans='x';
			else if(o==4)
				ans='o';
		}
		outfile<<"Case #"<<i<<": ";
		if(ans=='x'||ans=='X')
		       outfile<<"X won"<<endl;
		else if(ans=='o'||ans=='O')
			outfile<<"O won"<<endl;
		else if(num!=16)
			outfile<<"Game has not completed"<<endl;
		else
			outfile<<"Draw"<<endl;


	   }
	   }







