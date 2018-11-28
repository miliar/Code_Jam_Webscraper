#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

vector<char> myvec;
map<char,int> mymap;
char mark[10][10][2];

int main()
{
    int i,j,k,t,T,n;
    char p,q;
    string str;

    mymap['Q']=1;
    mymap['W']=2;
    mymap['E']=3;
    mymap['R']=4;
    mymap['A']=5;
    mymap['S']=6;
    mymap['D']=7;
    mymap['F']=8;

    freopen("b.in","r",stdin);
    freopen("bout.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        myvec.clear();

        for(i=1;i<9;i++)
        {
            for(j=1;j<9;j++)
            {
                mark[i][j][0]='x';
                mark[i][j][1]='x';
            }
        }

        scanf("%d",&n);

        for(i=0;i<n;i++)
        {
            cin>>str;

            mark[mymap[str[0]]][mymap[str[1]]][0]=str[2];
            mark[mymap[str[1]]][mymap[str[0]]][0]=str[2];
        }

        scanf("%d",&n);

        for(i=0;i<n;i++)
        {
            cin>>str;


                mark[mymap[str[0]]][mymap[str[1]]][1]='y';
                mark[mymap[str[1]]][mymap[str[0]]][1]='y';

        }

        scanf("%d",&n);

        cin>>str;

        for(i=0;i<n;i++)
        {
            //printf("now i is %d\n",i);

            if(myvec.empty())
            {
                myvec.push_back(str[i]);
            }

            else
            {
                p=myvec[myvec.size()-1];

                if(mymap[p] && mark[mymap[str[i]]][mymap[p]][0]!='x')
                {
                    myvec.pop_back();
                    myvec.push_back(mark[mymap[str[i]]][mymap[p]][0]);
                }

                else
                {
                    for(j=0;j<myvec.size();j++)
                    {
                        //printf("now j is %d\n",j);

                        k=1;
                        if(mymap[myvec[j]] && mark[mymap[str[i]]][mymap[myvec[j]]][1]=='y')
                        {
                            myvec.clear();
                            k=0;
                            break;
                        }

                    }

                    if(k) myvec.push_back(str[i]);


                }
            }
        }

        printf("Case #%d: [",t);

        if(myvec.size()!=0) printf("%c",myvec[0]);

        for(i=1;i<myvec.size();i++) printf(", %c",myvec[i]);

        printf("]\n");
    }

    return 0;
}




