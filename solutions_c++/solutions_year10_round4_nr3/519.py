#include<iostream>
using namespace std;
int update(bool a[][110],bool b[][110])
{
    int i,j,t=0;
    b[0][0]=0;
    for(i=0;i<101;i++)
    {
        b[i][0]=b[0][i]=0;
    }
    for(i=1;i<101;i++)
        for(j=1;j<101;j++)
            if((a[i][j] && (a[i-1][j] || a[i][j-1]))
            ||((!a[i][j]) && a[i-1][j] && a[i][j-1]))
                b[i][j]=1,t++;
            else
                b[i][j]=0;
    return t;
                
}
int main()
{
    int t,r,i,j,x1,y1,p,q,x2,y2,tr=0;
    cin>>t;
    bool a[110][110],b[110][110];
    while(t>0)
    {
        tr++;
        t--;j=0;
        cin>>r;
        memset(a,0,sizeof(a));
        for(i=0;i<r;i++)
        {
            cin>>x1>>y1>>x2>>y2;
            for(p=x1;p<=x2;p++)
                for(q=y1;q<=y2;q++)
                    a[p][q]=1;
        }
        while(r>0)
        {
            r=update(a,b);j++;
            if(r<=0) break;
            r=update(b,a);j++;
        }
        cout<<"Case #"<<tr<<": "<<j<<endl;
    }
    //system("pause");
}
