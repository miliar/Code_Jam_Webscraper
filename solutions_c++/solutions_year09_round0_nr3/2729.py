#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;


//int w,e1,l,c1,o1,m1,e2,s1,t,o2,s2,c2,o3,d,e3,s3,j,a,m2=0;
ofstream fout("out.txt");

int text[19];
void decode(char ch, int index[], int no)
{
   if (ch=='w')
   {
	text[0]++;
	return;
   }
	
   for(int i=0; i<no; i++)
   {
	if(text[index[i]-1]>0)
	{
		text[index[i]]+=text[index[i]-1];
//		text[index[i]-1]=0;
	}
   
   	if(text[index[i]]>10000)
		text[index[i]]%=10000;
   }
}

void zeroes(int a)
{
	if(a<10)fout<<"000";
	else if(a<100)fout<<"00";
	else if(a<1000)fout<<"0";
	fout<<a;
}

int main()
{
	ifstream fin("in.txt");
	
	int aw[1]={0};
	int ae[3]={1,6,14};
	int al[1]={2};
	int ac[2]={3,11};
	int ao[3]={4,9,12};
	int am[2]={5,18};
	int as[3]={7,10,15};
	int at[1]={8};
	int ad[1]={13};
	int aj[1]={16};
	int aa[1]={17};
	int cases=1;
	string aaaa;
	getline(fin,aaaa);
	stringstream sstr(aaaa);
	sstr >> cases;
	string st[cases];
	for(int i=0; i<cases; i++)
	{
		for(int j=0; j<19; j++)
		text[j]=0;
		getline(fin,st[i]);
		int in=0;
		int s=st[i].length();
		while (s--)
		{
			if(st[i][in]=='w')
				decode('w',aw,1);
			if(st[i][in]=='e')
				decode('e',ae,3);
			if(st[i][in]=='l')
				decode('l',al,1);
			if(st[i][in]=='c')
				decode('c',ac,2);
			if(st[i][in]=='o')
				decode('o',ao,3);
			if(st[i][in]=='m')
				decode('m',am,2);
			if(st[i][in]==' ')
				decode(' ',as,3);
			if(st[i][in]=='t')
				decode('t',at,1);
			if(st[i][in]=='d')
				decode('d',ad,1);
			if(st[i][in]=='j')
				decode('j',aj,1);
			if(st[i][in]=='a')
				decode('a',aa,1);
			in++;
		}
		fout<<"Case #"<<i+1<<": ";
		zeroes(text[18]);
		fout<<endl;
				
	}	

}
