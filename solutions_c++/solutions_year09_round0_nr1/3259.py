#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define ROW1 25
#define COL1 10
#define ROW2 10

ifstream fp_in;
fstream fp_out;


class alien
{
	private:
		int l,d,n;
		char lang[ROW1][COL1];
		char search[ROW2][28*COL1];
		int chk[ROW1];
		char temp;
		int pos,num;
	public:
		void init()
		{
			int r,c;
			pos=0;
			num=0;
			temp=NULL;
			for(r=0;r<ROW1;r++)
			{
				chk[r]=0;
				for(c=0;c<COL1;c++)
					lang[r][c]=NULL;
			}
			for(r=0;r<ROW2;r++)
			{
				chk[r]=0;
				for(c=0;c<(28*COL1);c++)
					search[r][c]=NULL;
			}
		}

		void input()
		{
			fp_in>>l;
			fp_in>>d;
			fp_in>>n;
			int i;
		    for(i=0;i<d;i++)
				fp_in>>lang[i];
			for(i=0;i<n;i++)
				fp_in>>search[i];

		}

		void check()
		{
			for(int i=0;i<d;i++)
			{
				if(lang[i][pos]==temp)
					chk[i]++;
			}
		}

		void calc()
		{
			int i,j,k;
			for(i=0;i<n;i++)
			{
				num=0;
				pos=0;
				for(j=0;j<strlen(search[i]);j++)
				{
					temp=search[i][j];
					if(temp=='(')
					{
						do
						{
							temp=search[i][++j];
							check();
						}while(temp!=')');
					}
					else
						check();
					pos++;
				}
				for(k=0;k<d;k++)
				{
					if(chk[k]==pos)
						num++;
					chk[k]=0;
				}
				fp_out<<"Case #"<<i+1<<": "<<num<<endl;
			}
		}




};

void main()
{
	clrscr();
	fp_out.open("A-small.out",ios::out,ios::in);
	//location of input file (need this name only)
	fp_in.open("A-small.in");
	alien obj;
	obj.init();
	obj.input();
	obj.calc();
	fp_out.close();
	fp_in.close();
}