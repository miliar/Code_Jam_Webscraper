#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
using namespace std;

int cnt=0,s;
bool items[100];
short countset, forbid;
char names[100][101];
void initialize()
{
    int i;
    for(i=0;i<s;i++)
        items[i]=true;
    if(forbid<0)
    {
        countset=0;
        return;   
    }    
    items[forbid]=false;
    countset=1;
}
void chkitem(int itm)
{
    if(items[itm])
    {
        items[itm]=false;
        if(++countset==s)
        {
            forbid=itm;
            cnt++;
            initialize();
        }    
    }
}
int main()
{
    int i,j,k,n,q;
    short size = 101*sizeof(char);
    char temp[101];
    char *pos;
    cin>>n;
    for(i=0;i<n;i++)
    {
        forbid=-1;
        cnt=0;
        cin>>s;
        cin.getline(temp,101);
        for(j=0;j<s;j++)
            cin.getline(names[j],101);   
        qsort((void *)names,s,size,(int(*)(const void*,const void*)) strcmp);

        cin>>q;
        cin.getline(temp,101);
        initialize();
        for(j=0;j<q;j++)
        {
            cin.getline(temp,101);
            pos=(char *) bsearch((void *)temp,(void *)names,s,size,(int(*)(const void*,const void*)) strcmp);
            chkitem((pos-names[0])/size);
        }   
        printf("Case #%d: %d\n", i+1, cnt);
    }    
    return 0;
}
