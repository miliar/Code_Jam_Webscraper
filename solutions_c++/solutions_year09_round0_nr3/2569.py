// Welcometo.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;
char welcome[100]="welcome to code jam";
int count;
int size;
char tmp[1000];
int memo[1000][100];

int bt(int pos, int iw)
{
    if(memo[pos][iw]!=-1)
    {
        return memo[pos][iw];
    }

    if(iw==strlen(welcome))
    {
        //count=(count+1)%1000;
        memo[pos][iw]=1;
        return memo[pos][iw];
    }
    if(pos==size)
    {        
        return 0;
    }
    
    int c=0;
    for(int i=pos;i<size;i++)
    {
        
        if(tmp[i]==welcome[iw])
        {
             c=(bt(i+1,iw+1)+c)%10000;
        }
       
     
    }
    memo[pos][iw]=c;
    return c;

}

int _tmain(int argc, _TCHAR* argv[])
{

    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int n;
    int i;
    scanf("%d\n", &n);
    for(i=0;i<n;i++){
        count=0;
        memset(memo,-1,sizeof(memo));
        size=0;
        char t;
        scanf("%c", &t);
        while(t!='\n')
        {
            tmp[size]=t;
            size++;
            scanf("%c", &t);
        }
        
        count=bt(0,0);
        printf("Case #%d: %04d\n", i+1,count);

    }

    

	return 0;
}

