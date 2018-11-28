#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

char turn[300][300];
bool opp[300][300];
char stack[500];
int sz;

int main()
{
    int t,q,c,j,i,n,d;
    string tmp,seq;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        sz=0;
        for (i=0;i<300;i++)
          for (j=0;j<300;j++)
          {
            opp[i][j]=0;
            turn[i][j]=0;
          }
        cin>>c;
        for (i=0;i<c;i++)
        {
            cin>>tmp;
            turn[tmp[0]][tmp[1]]=tmp[2];
            turn[tmp[1]][tmp[0]]=tmp[2];
        }
        cin>>d;
        for (i=0;i<d;i++)
        {
            cin>>tmp;
            opp[tmp[0]][tmp[1]]=1;
            opp[tmp[1]][tmp[0]]=1;
        }
        cin>>n;
        cin>>seq;
        for (i=0;i<n;i++)
        {
            stack[sz++]=seq[i];
            if (sz>1 && turn[stack[sz-1]][stack[sz-2]]>0)
            {
                stack[sz-2]=turn[stack[sz-1]][stack[sz-2]];
                sz--;
            }
            else
              for (j=0;j<sz-1;j++)
              {
                  if (opp[stack[sz-1]][stack[j]]==1)
                    sz=0;
              }
        }
        //cout<<"!"<<seq<<"!"<<endl;
        printf("Case #%d: [",q+1);
        for (i=0;i<sz-1;i++)
          cout<<stack[i]<<", ";
        if (sz>0)
          cout<<stack[sz-1];
        cout<<"]\n";
    }
    return 0;
}
