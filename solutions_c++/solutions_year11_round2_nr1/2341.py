#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<cstdio>
#include<map>
using namespace std;
char mat[200][200];
int a[200],b[200];
double Calc_win(int pos,int ind)
{
    int game=0,cnt=0,i,j;
    for(i=0;i<ind;i++)
    {
        if(mat[pos][i]=='1')
            {cnt++;game++;}
        else if(mat[pos][i]=='0')
             game++;
    }
    a[pos]=cnt;
    b[pos]=game;

    if(game)
       return cnt/(double)game;
    return game;
}
int main()
{
    freopen("A.txt","r",stdin);
    freopen("A1.txt","w",stdout);
    int i,j,m,n,ca,k=1;

    double WP[200],OWP[200],OOP[200];
    scanf("%d",&ca);
    while(ca--)
    {
        cin>>m;
        for(i=0;i<m;i++)
        cin>>mat[i];

    for(i=0;i<m;i++)
    {
        WP[i]=Calc_win(i,m);
       // cout<<WP[i]<<endl;
    }

    int v1,v2;

    for(i=0;i<m;i++)
    {   double res=0.0;
        for(j=0;j<m;j++)
        {
            if(i==j)continue;
            if(mat[j][i]=='1')
            {
                v1=a[j]-1;
                v2=b[j]-1;
                res+=(v1/(double)v2);
            }
            else if(mat[j][i]=='0')
            {
                v1=a[j];
                v2=b[j]-1;
                res+=(v1/(double)v2);
            }
        }
        OWP[i]=res/(double)b[i];
       // cout<<"owp:"<<OWP[i]<<endl;
    }
    int x;

            for(i=0;i<m;i++)
            {
            double res=0.0;
            OOP[i]=0;
            x=0;
            for(j=0;j<m;j++)
            {
                if(i==j)continue;
                if(mat[i][j]=='0'||mat[i][j]=='1')
                {
                    res+=OWP[j];
                    x++;
                }
            }
            if(x)
                OOP[i]=(res/(double)x);
            //cout<<"ii:"<<OOP[i]<<endl;
            }
        printf("Case #%d:\n",k);
        k++;
        for(i=0;i<m;i++)
        {
            cout<<0.25*WP[i]+0.50*OWP[i]+0.25*OOP[i]<<endl;
        }
    }
    return 0;
}
