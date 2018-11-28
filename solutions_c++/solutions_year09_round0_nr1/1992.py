// CJ_Q_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <stdio.h>

typedef struct words
{
    std::string word;   
};

struct point
{
	char value;
	point * next[100];
	point()
	{
		for (int i=0; i<100; i++) next[i]=NULL;
		value='0';
	}
};

void parse(std::string code,std::string* p)
{
	bool b = false;
	int j=0;
	for (int i=0; i<code.length(); i++)
	{
		if (code[i]=='(')
		{
			b=true;
		}
		else if (code[i]==')')
		{
			b=false;
			j++;
		}
		else
		{
			p[j]+=code[i];
			if (b==false) j++;
		}
	}
}


void getone(std::string* p,int i,int L,point* tree,char* x,int &sum)
{
	bool ok=false;
	
	int m=0;
	if (i>0)
	{
		
		while (m<100 && tree->next[m]!=0 && !ok)
		{
			if (tree->next[m]->value==x[i-1])
			{
				ok = true;
				m--;
			}
			m++;
		}
	}

	if (i>0 && ok==false) return;
	
	if (i>=L)
	{
		sum++;
		return;
	}

	for (int j=0; j<p[i].length(); j++)
	{
		char t =p[i].c_str()[j];
		x[i] = t;
		//printf("%c",t);
		if (i==0) getone(p,i+1,L,tree,x,sum);
		else getone(p,i+1,L,tree->next[m],x,sum);
	}
}

int count(std::string* p,point* tree,int L)
{
	char* x= new char[L+1];
	memset(x,0,L+1);
	int sum=0;
	getone(p,0,L,tree,x,sum);
	return sum;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE * fout;
    fout = fopen("F:\\CodeJam\\\Al.out","w+b");
    std::string str_in = "F:\\CodeJam\\\A-large.in";
    std::ifstream is(str_in.c_str());
    std::string line;

    int N;
    int L;
    int D;
    is >> L;//length
    is >> D;//words
    is >> N;//number of cases
	std::string code;
	std::string* p = new std::string[L];
    words *w = new words[5000];
    point tree;
	point* t;
	
	t =&tree;
    for (int i=0; i<D; i++)
    {
        is >> w[i].word; 
		t =&tree;
		bool ok=false;
		for (int j=0; j<L; j++)
		{
			for (int k=0; k<100; k++)
			{
				if (t->next[k]!=0 && t->next[k]->value==w[i].word[j])
				{
					t=t->next[k];
					ok = true;
					break;
				}
				if (t->next[k]==0)
				{
					t->next[k] = new point;
					t=t->next[k];
					t->value=w[i].word[j];
					break;
				}
			}		
		}
    }

    for (int i=0; i<N; i++)
    {    
		printf("%d\n",i);
		is >> code;
		parse(code,p);
		int sum = count(p,&tree,L);
		for (int j=0; j<L; j++) p[j].clear();
		char out[100];
		sprintf(out,"Case #%d: %d\n",i+1,sum);
		fwrite(out,strlen(out),1,fout);

    }
   

    fclose(fout); 
	return 0;
}

