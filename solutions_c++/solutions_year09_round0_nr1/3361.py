#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<process.h>
#include<string.h>

char **arr_create(int rows, int cols)
{
	char **p;
	p = new char *[rows];
	for (int i=0;i<rows;i++)
	p[i]=new char [cols];
	return p;
}

void show(char **p,int rows,int cols)
{
	int i,j;
	for(i=0;i<rows;i++)
	{
	cout << endl;
	for(j=0;j<cols;j++)
	cout <<p[i][j]<<" ";
	}
}
//////////////////////////////////////MAIN/////////////////////////
void main()
{

int L,D,N;
char **dic;
char **pat,**cur_pat;
int tmp_col,cur_row,cur_col;
char ch,flag,tmp_chr;
int status,word_cnt;
fstream infile;
fstream outfile;

clrscr();

//////////////////////////////////////////////////////////////////
infile.open("c:\\tc\\bin\\code_jam\\rough\\A-small.in" , ios::in);
if(infile.fail())
{
cout <<"IN Error";
getch();
exit(1);
}
//////////////////////////////////////////////////////////////////
infile >> L;
infile >> D;
infile >> N;
cout <<L<<" "<<D<<" "<<N;

dic = arr_create(D,L);
pat = arr_create(N,(26*L));
cur_pat = arr_create(L,26);
////////////////////////////read date/////////////////////////////
for(int temp=0;temp<D;temp++)
{
infile >> dic[temp];
//cout << endl;
//cout << dic[temp];
}
cout << endl;

for(temp=0;temp<N;temp++)
{
infile >> pat[temp];
//cout << endl;
//cout << pat[temp];
}
//cout<<endl;

/////////////////////////out file////////////////////////////////
outfile.open("c:\\tc\\bin\\code_jam\\rough\\A-small.out" , ios::out);
if(outfile.fail())
{
cout <<"out Error";
getch();
exit(1);
}

//////////////////////////process///////////////////////////////
for (temp=0;temp<N;temp++)
{
	word_cnt=0;
	tmp_col=0;
	cur_row=0;
	cur_col=0;
	ch=pat[temp][tmp_col];
	flag='f';
	while (ch!='\0')
	{

		if(ch=='(')
		{
		flag='t';
		}
		else if(ch==')')
		{
		cur_pat[cur_row][cur_col]='\0';
		cur_row++;
		cur_col=0;
		flag='f';
		}
		else if(flag=='t')
		{
		cur_pat[cur_row][cur_col]=ch;
		cur_col++;
		}
		else
		{
		cur_pat[cur_row][cur_col]=ch;
		cur_col++;
		cur_pat[cur_row][cur_col]='\0';
		cur_row++;
		cur_col=0;
		}
	//cout <<endl<<ch;
	tmp_col++;
	ch=pat[temp][tmp_col];
	}
	 //////////////////////////////////////////////////
	for(int k=0;k<D;k++)
	{
	 status=0;
	 for(int l=0;l<L;l++)
	 {
	 tmp_chr = dic[k][l];
	 if( strchr(cur_pat[l] ,tmp_chr ) )
	 status++;
	 else
	 continue;
	 }
	 //cout<<status<<endl;
	 if(status==L)
	 word_cnt++;
	}
	///////////////////////////////////////////////////
outfile<<"Case #"<<(temp+1)<<": "<<word_cnt<<endl;
}

//cout <<cur_pat[0]<<endl;
//show(cur_pat,L,26);
////////////////////////////////////////////////////////////////


getch();
}

