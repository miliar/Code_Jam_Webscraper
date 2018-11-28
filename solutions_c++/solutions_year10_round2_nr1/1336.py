// 1B-A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<cstring>
using namespace std;

FILE *in,*out;

char given[100][100]={0},want[100][100]={0},total[100000]={0},tmp[100];
int n,m,i,j,tt,t,tlen,counting;


void add(int i)
{
    char tmp[100];
    int ii,jj,len;
    ii=1;
    len=1;
    memset(tmp,0,sizeof(tmp));
    tmp[0]='.';
    while (given[i][ii])
    {
        if (given[i][ii]!=47)
        {
            tmp[len]=given[i][ii];
            len++;
        }
        else
        {
            tmp[len]='.';
            if (!strstr(total,tmp))
                strcat(total,tmp);
        }
        ii++;
    }
    tmp[len]='.';
    if (!strstr(total,tmp))
        strcat(total,tmp);
}
    

void checkNadd(int i)
{
    char tmp[100];
    int ii,jj,len;
    ii=1;
    len=1;
    memset(tmp,0,sizeof(tmp));
    tmp[0]='.';
    while (want[i][ii])
    {
        if (want[i][ii]!=47)
        {
            tmp[len]=want[i][ii];
            len++;
        }
        else
        {
            tmp[len]='.';
            if (!strstr(total,tmp))
            {
                counting++;
                strcat(total,tmp);
            }
        }
        ii++;
    }
    tmp[len]='.';
    if (!strstr(total,tmp))
	{
		counting++;
        strcat(total,tmp);
	}
}
    
    
     


int _tmain(int argc, _TCHAR* argv[])
{
	in=freopen("A-small-attempt0(2).in","r",stdin);
    out=freopen("A-small.out","w",stdout);
    
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        counting=0;
        memset(total,0,sizeof(total));
        tlen=0;
        cin>>n>>m;
        for (i=0;i<n;i++)
        {
            scanf("%s",given[i]);
            add(i);
        }
        for (i=0;i<m;i++)
        {
            scanf("%s",want[i]);
            checkNadd(i);
        }
        cout<<"Case #"<<tt<<": "<<counting<<endl;
    }
    fclose(in);
    fclose(out);
	return 0;
}

