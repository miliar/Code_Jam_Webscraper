#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("cpout1.txt","w",stdout);
        int t,tt,r,c,rc[50][50];
        char tile;
        cin >> tt;
        bool imp = false;
        for(t=1 ; t<=tt ; t++)
        {
                cin >> r >> c;
                cout << "Case #" << t << ":"<<endl;
                for(int i=0; i<r; i++)
                {
                    for(int j=0;j<c;j++)
                    {
                        cin >> tile;
                        if(tile=='.')
                            rc[i][j] = 0;
                        if(tile=='#')
                            rc[i][j] = 1;
                    }
                }
                for(int i=0; i<r; i++)
                {
                    for(int j=0;j<c;j++)
                    {
                        if(rc[i][j]==1)
                        {
                            if(r<2 || c <2)
                                imp = true;
                            if((i<r-1)&&(j<c-1))
                            {
                                if((rc[i][j+1]==1)&&(rc[i+1][j]==1)&&(rc[i+1][j+1]==1))
                                {
                                    rc[i][j]=2;rc[i][j+1]=3;
                                    rc[i+1][j]=3;rc[i+1][j+1]=2;
                                }
                                else
                                {
                                    imp = true;
                                }
                            }
                        }
                    }
                }
                for(int i=0; i<r; i++)
                {
                    for(int j=0;j<c;j++)
                    {
                        if(rc[i][j]==1)
                        {
                            imp = true;
                        }
                    }
                }
                if(imp)
                {
                    cout<<"Impossible"<<endl;
                    imp = false;
                    continue;
                }
                for(int i=0; i<r; i++)
                {
                    for(int j=0;j<c;j++)
                    {
                        if(rc[i][j]==0)
                            cout<<".";
                        else if(rc[i][j]==1)
                            cout<<"#";
                        else if(rc[i][j]==2)
                            cout<<"/";
                        else if(rc[i][j]==3)
                            cout<<"\\";
                    }
                    cout<<endl;
                }
        }
        return 0;
}
