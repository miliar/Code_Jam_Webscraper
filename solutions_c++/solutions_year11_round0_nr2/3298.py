#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
void add(char *out,char ch)
{
	int i=0;
	i=strlen(out);
	out[i]=ch;
	out[i+1]='\0';
}
void rem(char *out)
{
	int i=0;
	i=strlen(out);
	if(i==0)
		out[0]='\0';
	else
		out[i-1]='\0';
}
void check(char *out,int opp[26][26])
{
	int len;
	len=strlen(out);
	for(int i=0;i<len-1;i++)
		for(int j=i+1;j<len;j++)
			if(opp[out[i]-'A'][out[j]-'A']==1)
				out[0]='\0';
}
void main()
{
	int t,c,d,n,i,j,opposed[26][26],l;
	char **comb,**opp,*input,*output,combination[26][26];
	ifstream fi("B-large.in",ios::binary|ios::in);
	ofstream fo("outputBl.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		for(i=0;i<26;i++)
			for(j=0;j<26;j++)
			{
				combination[i][j]='0';
				opposed[i][j]=0;
			}
		fi>>c;
		if(c!=0)
		{
			comb=new char*[c];
			for(i=0;i<c;i++)
			{	
				comb[i]=new char[3];
				fi>>comb[i][0]>>comb[i][1]>>comb[i][2];
				cout<<comb[i][0]<<comb[i][1]<<comb[i][2]<<endl;
				combination[comb[i][0]-'A'][comb[i][1]-'A']=combination[comb[i][1]-'A'][comb[i][0]-'A']=comb[i][2];
			}
		}
		fi>>d;
		if(d!=0)
		{
			opp=new char*[d];
			for(i=0;i<d;i++)
			{	
				opp[i]=new char[2];
				fi>>opp[i][0]>>opp[i][1];
				cout<<opp[i][0]<<opp[i][1]<<endl;
				opposed[opp[i][0]-'A'][opp[i][1]-'A']=opposed[opp[i][1]-'A'][opp[i][0]-'A']=1;
			}
		}
		fi>>n;
		input=new char[n];
		output=new char[n];
		output[0]='\0';
		for(i=0;i<n;i++)
			fi>>input[i];
		l=strlen(output);
		for(i=0;i<n;i++)
		{
			if(l==0)
				add(output,input[i]);
			else if(combination[input[i]-'A'][output[l-1]-'A']=='0')
				add(output,input[i]);
			else
			{
				rem(output);
				add(output,combination[input[i]-'A'][input[i-1]-'A']);
			}
			check(output,opposed);
			l=strlen(output);
		}
		l=strlen(output);
		fo<<"Case #"<<t_c+1<<": [";
		for(i=0;i<l;i++)
			if(i==l-1)
				fo<<output[i];
			else
				fo<<output[i]<<", ";
		fo<<"]"<<endl;
		cout<<"Case #"<<t_c+1<<": "<<output<<endl;
	}
	fi.close();
	fo.close();
	_getch();
}