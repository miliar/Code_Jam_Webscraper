#include<iostream>

using namespace std;

int main()
{
    int t,r[20],c[20],i,j,k,count,flag[20];
    char tile[20][6][6];
    cin>>t;

    for(i=0;i<t;i++)
    {
        r[i]=c[i]=flag[i]=0;
    }

    for(i=0;i<t;i++)
    {
        count=0;
        flag[i]=0;
        cin>>r[i];
        cin>>c[i];
        for(j=0;j<r[i];j++)
        {
            for(k=0;k<c[i];k++)
            {
                cin>>tile[i][j][k];
                if(tile[i][j][k]=='#')
                    count++;
            }
        }

        if(count%2==0)
        {
            for(j=0;j<r[i];j++)
            {
                for(k=0;k<c[i];k++)
                {
                    if(tile[i][j][k]=='#')
                    {
                        if(j!=r[i]-1 && k!=c[i]-1)
                        {

                        if(tile[i][j][k+1]=='#' && tile[i][j+1][k]=='#' && tile[i][j+1][k+1]=='#')
                        {
                            tile[i][j][k]=tile[i][j+1][k+1]='/';
                            tile[i][j][k+1]=tile[i][j+1][k]='\\';
                        }
                        else{flag[i]=1;}
                        }

                        else
                        {
                            flag[i]=1;
                        }


                    }
                }
            }
        }
        else{flag[i]=1;}



    }

    for(i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<":"<<endl;
        if(flag[i]==1)
            cout<<"Impossible"<<endl;
        else
        {
            for(j=0;j<r[i];j++)
            {
            for(k=0;k<c[i];k++)
            {
                cout<<tile[i][j][k];
            }
            cout<<endl;
            }
        }
    }

    return 0;
}
