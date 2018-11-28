#include <iostream>
#include<fstream>

using namespace std;

ifstream fin("A+.in");
ofstream fout("A+.out");

int t,test,k,n,db,map[52][52],map2[52][52];

int grav(int n)    //jo
{
    for(int j=1;j<=n;j++)
    {
        int ures=n;
        for(int i=n;i>=1;i--)
        {
            if(map2[i][j]!=0)
            {
                map2[ures][j]=map2[i][j];
                ures--;
            }
        }
        while(ures>=1)
        {
            map2[ures][j]=0;
            ures--;
        }
    }
    return 0;
}

int forgat(int n)  //jo
{
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            map2[i][j]=map[n-j+1][i];
    return 0;
}

int jo(int x,int y)
{
    if(y+k-1<=n)
    {
        //1   jo
        int j=1,ok=1;
        while(ok==1&&j<=k-1)
        {
            if(map2[x][y+j]!=map2[x][y]) ok=0;
            j++;
        }
        if(ok==1) return 1;
        //4  jo
        if(x+k-1<=n)
        {
            int j=1,ok=1;
            while(ok==1&&j<=k-1)
            {
                if(map2[x+j][y+j]!=map2[x][y]) ok=0;
                j++;
            }
            if(ok==1) return 1;
        }
        //3
        if(x-k+1>0)
        {
            int j=1,ok=1;
            while(ok==1&&j<=k-1)
            {
                if(map2[x-j][y+j]!=map2[x][y]) ok=0;
                j++;
            }
            if(ok==1) return 1;
        }
    }
    //2
    if(x+k-1<=n)
    {
        int j=1,ok=1;
        while(ok==1&&j<=k-1)
        {
            if(map2[x+j][y]!=map2[x][y]) ok=0;
            j++;
        }
        if(ok==1) return 1;
    }
    return 0;
}

int szamol(int n)
{
    int db=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(map2[i][j]!=0&&jo(i,j)!=0)
                if(db==0) db=map2[i][j];
                else if(db!=map2[i][j]) return 3;
    return db;
}

int main()
{
    fin>>t;
    for(int test=1;test<=t;test++)
    {
        fin>>n>>k;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                char c[0];
                fin>>c[0];
                if(c[0]=='.') map[i][j]=0;
                if(c[0]=='R') map[i][j]=1;
                if(c[0]=='B') map[i][j]=2;
            }
        cout<<k<<"\n";
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
                cout<<map[i][j];
            cout<<"\n";
        }
        cout<<"\n";
        forgat(n);
        cout<<"\n";
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
                cout<<map2[i][j];
            cout<<"\n";
        }
        cout<<"\n";
        grav(n);
        cout<<"\n";
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
                cout<<map2[i][j];
            cout<<"\n";
        }
        cout<<"\n";
        db=szamol(n);
        fout<<"Case #"<<test<<": ";
        if(db==0) fout<<"Neither";
        else if(db==1) fout<<"Red";
             else if(db==2) fout<<"Blue";
                  else fout<<"Both";
        fout<<"\n";
        cout<<"Case #"<<test<<": ";
        if(db==0) cout<<"Neither";
        else if(db==1) cout<<"Red";
             else if(db==2) cout<<"Blue";
                  else cout<<"Both";

    }
    return 0;
}
