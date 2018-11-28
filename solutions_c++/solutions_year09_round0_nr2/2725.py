#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define HMAX 50
#define WMAX 50

ifstream fp_in;
fstream fp_out;
int t=0,h=0,w=0,p=0;
char curr_char='a';

struct data
{
	int alt;
	char base;
}dat[HMAX][WMAX];

struct path
{
	int row,col;
}var[HMAX*WMAX];

void reset()
{
	int i,j,k,l;
	for(i=0;i<HMAX;i++)
	{
		for(j=0;j<WMAX;j++)
		{
			dat[i][j].alt=0;
			dat[i][j].base=NULL;
		}
	}
	for(i=0;i<(HMAX*WMAX);i++)
	{
		var[i].row=0;
		var[i].col=0;
	}
	h=0;
	p=0;
	w=0;
	curr_char='a';
}

void input()
{
	fp_in>>h;
	fp_in>>w;
	for(int i=0;i<h;i++)
		for(int j=0;j<w;j++)
			fp_in>>dat[i][j].alt;
}

void pop(char basin)
{
	for(int ctr=p-1;ctr>=0;ctr--)
	{
		dat[var[ctr].row][var[ctr].col].base=basin;
		cout<<"val: "<<var[ctr].row<<" "<<var[ctr].col<<" "<<dat[var[ctr].row][var[ctr].col].base<<endl;
	}
}

void check_neighbours(int r,int c)
{
	int lowest;
	int flag=0;
	int lr,lc;
	lr=r;
	lc=c;
	do{
		lowest=dat[r][c].alt;
		flag=0;
		//lr=0;
		//lc=0;
		if(r>0)
			if(lowest>dat[r-1][c].alt)
			{
				lowest=dat[r-1][c].alt;
				lr=r-1;
				lc=c;
				flag=1;
			}
		if(c>0)
			if(lowest>dat[r][c-1].alt)
			{
				lowest=dat[r][c-1].alt;
				lr=r;
				lc=c-1;
				flag=1;
			}
		if(c<w-1)
			if(lowest>dat[r][c+1].alt)
			{
				lowest=dat[r][c+1].alt;
				lr=r;
				lc=c+1;
				flag=1;
			}
		if(r<h-1)
			if(lowest>dat[r+1][c].alt)
			{
				lowest=dat[r+1][c].alt;
				lr=r+1;
				lc=c;
				flag=1;
			}
		if(dat[lr][lc].base!=NULL)
		{
			pop(dat[lr][lc].base);
			p=0;
			cout<<"\nover here\t"<<lr<<" "<<lc;
			break;
		}
		if(flag==1)
		{
			var[p].row=lr;
			var[p].col=lc;
			p++;
			//check_neighbours(lr,lc);
			r=lr;
			c=lc;
		}
	}while(flag==1);
	if(flag==0)
	{
		pop(curr_char);
		//cout<<"\nThen: "<<curr_char;
		curr_char++;
		p=0;
	}
}


void calc()
{
	int i,j,k;
	for(i=0;i<h;i++)
	{
		for(j=0;j<w;j++)
		{
			if(dat[i][j].base==NULL)
			{
				var[p].row=i;
				var[p].col=j;
				p++;
				check_neighbours(i,j);
			}
		}
	}
}

void disp(int num)
{
	fp_out<<"Case #"<<num+1<<":\n";
	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)
			fp_out<<dat[i][j].base<<" ";
		fp_out<<endl;
	}
}


void main()
{
	clrscr();
	fp_out.open("B-SMALL.out",ios::out,ios::in);
	//location of input file (need this name only)
	fp_in.open("B-SMALL.in");
	fp_in>>t;
	for(int i=0;i<t;i++)
	{
		input();
		calc();
		disp(i);
		reset();
	}
	fp_out.close();
	fp_in.close();
}