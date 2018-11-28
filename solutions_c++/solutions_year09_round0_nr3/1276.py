
#include <iostream>
#include <cstdio>
using namespace std;

//int notim;
int x,n,sum;
int i,ii,le1,le2;
int ar[20][501];
char st[502];
char st2[20];

int main()
{
    
    cin >> n;
    gets(st);
    
    st2[0] = 'w';
    st2[1] = 'e';
    st2[2] = 'l';
    st2[3] = 'c';
    st2[4] = 'o';
    st2[5] = 'm';
    st2[6] = 'e';
    st2[7] = ' ';
    st2[8] = 't';
    st2[9] = 'o';
    st2[10] = ' ';
    st2[11] = 'c';
    st2[12] = 'o';
    st2[13] = 'd';
    st2[14] = 'e';
    st2[15] = ' ';
    st2[16] = 'j';
    st2[17] = 'a';
    st2[18] = 'm';
    
    for(x=1;x<=n;x++)
    {
                     
    gets(st);
    //cout << st;
    //cout << '\n';
    //cin >> notim;
    i=0;
    while(st[i]!=0) i++;
    
    le1 = 19;
    le2 = i;
    
    
    
    for(i=0;i<le1;i++)
     for(ii=0;ii<le2;ii++)
     {
     ar[i][ii] = 0;
     }
     
    for(ii=0;ii<le2;ii++) if (st[ii]==st2[0]) ar[0][ii]=1;
    
    for(i=1;i<le1;i++)
    {
    sum = 0;
     for(ii=0;ii<le2;ii++)
     {
     if(st[ii]==st2[i]) ar[i][ii] = sum%10000;
     sum+=ar[i-1][ii];
     }     
    }
    
    sum = 0;
    for(ii=0;ii<le2;ii++) sum += ar[i-1][ii];
    sum = sum%10000;
    
    //cout << st;
    printf("Case #%d: ",x);
    
    if(sum<1000) cout << "0";
    if(sum<100) cout << "0";
    if(sum<10) cout << "0";
    
    cout << sum;
    
    cout << '\n';
    }
}
