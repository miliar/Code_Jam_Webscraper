#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>

using namespace std;

int Ap[101],Ad[101],Bp[101],Bd[101];

int compare(const void *a,const void *b)
{
  return *(int*)a - *(int*)b;
}


int main()
{
    string s,u;
    int ncase,ccase;
    int t,na,nb;
    int x,y,z,mark;
    int jad,jap,jbd,jbp;
    int ka,kb;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        cin >> t;
        cin >> na >> nb;
        
        for(x = 0;x < na;x++)
        {
            cin >> s >> u;
            
            y = ((((s[0] - '0') * 10) + (s[1] - '0')) * 60) + (((s[3] - '0') * 10) + (s[4] - '0'));
            Ap[x] = y;
            y = ((((u[0] - '0') * 10) + (u[1] - '0')) * 60) + (((u[3] - '0') * 10) + (u[4] - '0'));
            Bd[x] = y + t;
        }
        qsort(Ap,na,sizeof(int),compare);
        qsort(Bd,na,sizeof(int),compare);
        
        for(x = 0;x < nb;x++)
        {
            cin >> s >> u;
            
            y = ((((s[0] - '0') * 10) + (s[1] - '0')) * 60) + (((s[3] - '0') * 10) + (s[4] - '0'));
            Bp[x] = y;
            y = ((((u[0] - '0') * 10) + (u[1] - '0')) * 60) + (((u[3] - '0') * 10) + (u[4] - '0'));
            Ad[x] = y + t;
        }
        qsort(Bp,nb,sizeof(int),compare);
        qsort(Ad,nb,sizeof(int),compare);
        
        jad = 0; jap = 0;
        jbd = 0; jbp = 0;
        y = 0; z = 0; mark = 0;
        ka = 0; kb = 0;
        for(x = 0;x < 1440;)
        {
            mark = 0;
            if(jad < nb)
            {
                if(Ad[jad] == x)
                {
                    y++;
                    jad++;
                    mark = 1;
                }
            }
            if(jbd < na)
            {
                if(Bd[jbd] == x)
                {
                    z++;
                    jbd++;
                    mark = 1;
                }
            }
            if(jap < na)
            {
                if(Ap[jap] == x)
                {
                    if(y == 0)
                        ka++;
                    else
                        y--;
                    jap++;
                    mark = 1;
                }
            }
            if(jbp < nb)
            {
                if(Bp[jbp] == x)
                {
                    if(z == 0)
                        kb++;
                    else
                        z--;
                    jbp++;
                    mark = 1;
                }
            }
            if(mark == 0)
                x++;
        }
        
        cout << "Case #" << ccase << ": " << ka << " " << kb << endl;
    }
    
    return 0;
}
