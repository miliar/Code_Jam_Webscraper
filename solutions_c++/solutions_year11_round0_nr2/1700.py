#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std ;
char output[200];
struct base 
{
	char a;
	char b;
	char c ;
}b[40];
struct oppose
{
	char a ;
	char b;
}o[40];
int c, d;
char can_con(char aa , char bb)
{
	for(int i=0;i<c;i++)
	{
		char cha=b[i].a;
		char chb=b[i].b;
		if((cha==aa&&chb==bb)||(cha==bb&&chb==aa))
		{
			return b[i].c;
		}
	}
	return 0;
}
bool is_present(char ch , int pos)
{
	for(int i=0;i<=pos;i++)
	{
		if(output[i]==ch)
			return true ;
	}
	return false;
}
int is_opposed(char ch , int pos )
{
	for(int i=0;i<d;i++)
	{
		if(o[i].a==ch)
		{
			if(is_present(o[i].b, pos))
				return 1 ;						
		}
		else if(o[i].b==ch)
		{
			if(is_present(o[i].a, pos))
				return 1;
		}
	}
	return 0;
}
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int C;
		cin>>C;
		//if(C)
			//cin.getline(NULL ,0);
		for(c=0;c<C;c++)
		{
			scanf(" %c%c%c",&b[c].a,&b[c].b,&b[c].c);			
		}
		int D;
		cin>>D;
		//if(D)
			//cin.getline(NULL, 0);
		for(d=0;d<D;d++)
		{
			scanf(" %c%c",&o[d].a , &o[d].b);
		}
		int N;
		cin>>N;
		char ch ;
		int pos=0;
		scanf(" %c",&ch);
		output[pos]=ch;
		int prev_base=ch;
		for(int n=1;n<N;n++)
		{
			scanf(" %c",&ch);
			char pr=output[pos];
			char cat;
			if(pos!=-1&&(cat=can_con(pr , ch))!=0)
			{
				output[pos]=cat;
			}
			else if((pos>=0)&&is_opposed(ch , pos))
			{
				pos=-1;	
			}
			else
			{
				output[++pos]=ch;
			}			
		}
		printf("Case #%d: [",t+1);	
		for(int i=0;i<pos;i++)
		{
			printf("%c, ",output[i]);
		}
		if(pos!=-1)
			printf("%c]\n",output[pos]);
		else
			puts("]");
		pos=-1;
		//puts("]");
	}
	return 0;
}
