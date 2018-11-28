#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define ROW1 100
#define COL 50
#define ROW2 1000

ifstream fp_in;


class universe
{
	private:
		int s,q;
		char search[ROW1][COL];
		char query[ROW2][COL];
		int s_flag[ROW1];
		int change;
		char current[COL];
	public:
		void init()
		{
			int r,c;
			change=0;
			for(r=0;r<ROW1;r++)
			{
				s_flag[r]=0;
				for(c=0;c<COL;c++)
					search[r][c]=NULL;
			}
			for(r=0;r<ROW2;r++)
				for(c=0;c<COL;c++)
					query[r][c]=NULL;
			for(c=0;c<COL;c++)
				current[c]=NULL;
		}

		void set_s()
		{
			fp_in>>s;
			char temp[2];
			fp_in.getline(temp,2,'\n');
			for(int i=0;i<s;i++)
				fp_in.getline(search[i],COL,'\n');
		}

		void set_q()
		{
			fp_in>>q;
			char temp[2];
			fp_in.getline(temp,2,'\n');
			for(int i=0;i<q;i++)
				fp_in.getline(query[i],COL,'\n');
		}

		int all_one()
		{
			for(int i=0;i<s;i++)
				if(s_flag[i]==0)
					return 0;
			return 1;
		}

		void set_flag()
		{
			for(int i=0;i<ROW1;i++)
				s_flag[i]=0;
		}

		int calc()
		{
			int r,c,i,k;
			for(i=0;i<q;i++)
			{
				for(k=0;k<s;k++)
				{
					if(strcmp(query[i],search[k])==0)
					{
						s_flag[k]=1;
						if(all_one()==1)
						{
							strcpy(current,search[k]);
							change++;
							set_flag();
							s_flag[k]=-1;

						}
						break;
					}
				}
			}
			return(change);
		}




};

void main()
{
	clrscr();
	fstream fp_out;
	fp_out.open("saving.txt",ios::out,ios::in);
	int n,i,change;
	//location of input file (need this name only)
	fp_in.open("a.in");
	fp_in>>n;
	universe obj;
	for(i=0;i<n;i++)
	{
		obj.init();
		obj.set_s();
		obj.set_q();

		change=obj.calc();
		fp_out<<"Case #"<<i+1<<": "<<change<<endl;
	}
	fp_out.close();
	fp_in.close();
}