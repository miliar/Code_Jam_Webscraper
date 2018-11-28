#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

bool maz[51][51];
bool vis[51][51];
int X[3] = {1,0,1};
int Y[3] = {0,1,1};
char cm[51][51];
char Z[3] = {'\\','\\','/'};
bool flod(int I,int J,int R,int C)
{
    cm[I][J]='/';
    for(int i=0;i<3;i++)
    {
        if(I+X[i] < R && J+Y[i]<C &&!vis[I+X[i]][J+Y[i]] && maz[I+X[i]][J+Y[i]])

        {
            vis[I+X[i]][J+Y[i]]=1;
            cm[I+X[i]][J+Y[i]]= Z[i];
        }
        else
        return false;
    }
    return true;

}
int main()
{
    freopen("A-large(2).in","rt",stdin);

      freopen("out.out","wt",stdout);
    int T;
    cin>>T;

    for(int TT=1;TT<=T;TT++)
    {
        int R,C;
        cin>>R>>C;
      //  swap(R,C);
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                vis[i][j]=0;

                char c;
                cin>>c;
                cm[i][j]=c;
                if(c=='#')
                {//cout<<"Z";
                maz[i][j]=1;
                }else
                maz[i][j]=0;
            }

        }

        int cnt = 0;
        bool isGood =1;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(!vis[i][j]&&maz[i][j])
                {
                    cnt++;
                //    cout<<"X";
                    if(!flod(i,j,R,C))
                    {
                        isGood = 0;


                    }

                }
            }

        }



          cout<<"Case #"<<TT<<":"<<endl;
            if(!isGood)
            {
                cout<<"Impossible"<<endl;
            }else{
                for(int i=0;i<R;i++)
                {
                    for(int j=0;j<C;j++)
                    {
                        cout<<cm[i][j];
                    }cout<<endl;
                }

            }


    }

}
