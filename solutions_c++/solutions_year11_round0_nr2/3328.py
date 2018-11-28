#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
class combine
{
public:
	char b1,b2,nb;
	void setValue(char a,char b,char c)
	{
		b1=a;
		b2=b;
		nb=c;
	}
};
class opposed
{
public:
	char b1,b2;
	void setValue(char a,char b)
	{
		b1=a;
		b2=b;
	}
};
char * createList(combine * com,int csize,opposed * opp,int osize,char * arr,int size)
{
	char *list=new char [size+1];
	int i=1,j=1;
	list[0]=arr[0];
	while(i<size)
	{
	
		list[j]=arr[i];
		if(csize!=0 && j>=1)
		{
			for(int k=0; k<csize && j>=1 ; k++)
			{
				if((list[j]==com[k].b1 && list[j-1]==com[k].b2) || (list[j]==com[k].b2 && list[j-1]==com[k].b1))
				{
					j--;
					list[j]=com[k].nb;
				}
			}
		}
		if(osize!=0 && j>=1)
		{
			for(int l=j-1; l>=0 && j>=1; l--)
			{
				for(int m=0; m<osize && j>=1 ; m++)
				{
					
					if((opp[m].b1==list[l] && opp[m].b2==list[j]) || (opp[m].b2==list[l] && opp[m].b1==list[j]))
					{
						j=-1;
						
					}
				}
			}
		}
		i++;
		j++;
	}
	list[j]='\0';
	return list;
}
void main ()
{
	ifstream in ("B-large.in");
	ofstream out("output.txt");
	int T,C,D,N,ci=0,oi=0;
	combine com[36];
	opposed opp[28];
	char * arr;
	char * list;
	char a,b,c,ch;
	in>>T;
	for(int i=0; i<T; i++)
	{
		ci=0;
		oi=0;
		in>>C;
		in.get(ch);
		for(int j=0; j<C; j++)
		{
			in.get(a);
			in.get(b);
			in.get(c);
			com[ci].setValue(a,b,c);
			ci++;
			in.get(ch);
			if(ch!=' ')
			{
				in.seekg(-1,ios::cur);
			}

		}

		in>>D;
		in.get(ch);
		for(int k=0; k<D; k++)
		{
			in.get(a);
			in.get(b);
			opp[oi].setValue(a,b);
			oi++;
			in.get(ch);
			if(ch!=' ')
			{
				in.seekg(-1,ios::cur);
			}

		}
		in>>N;
		arr=new char[N+1];
		in.get(a);
		for( int l=0; l<N; l++)
		{
			in.get(a);
			arr[l]=a;

		}
		arr[l]='\0';
		if(l!=0)
		{
			list=createList(com,ci,opp,oi,arr,l);
			out<<"Case #"<<i+1<<": [";
			int n=0;
			while(list[n]!='\0')
			{
				out<<list[n];
				n++;
				if(list[n]!='\0')
				{
					out<<", ";
				}
			}
			out<<"]";
			if(i+1!=T)
			{
				out<<endl;
			}
		}
	}
}