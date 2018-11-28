#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string w="welcome to code jam";// length = 19   0--18
string c;
int n;
int ans[505][20];

int f(int x, int y)
{
    int i,j,k;
    if (y==(w.length())) ans[x][y]=1;

    if (ans[x][y]==-1)
    {
        ans[x][y]=0;
        for (i=x+1;i<=c.length();i++) 
        {
            if (c[i-1]==w[y]) ans[x][y]+=f(i,y+1);
            ans[x][y]=ans[x][y]%10000;
        }
    }
    return ans[x][y];
}

int main()
{
    int i,j,k;
    ofstream fout("C-large.out");
    ifstream fin("C-large.in");

    fin>>n;    getline(fin,c);
    for (i=1;i<=n;i++)
    {
        getline(fin,c); 
        for (j=0;j<=504;j++) 
            for (k=0;k<=19;k++)  ans[j][k]=-1;
        fout<<"Case #"<<i<<": ";
        j=f(0,0);
        if (j<1000 && j>=100) fout<<"0";
        if (j<100  && j>=10) fout<<"00";
        if (j<10) fout<<"000";
        fout<<j<<endl;
    }
    
    
//   cout<<c[18]<<endl;
    
    //cin>>n;
    return 0;
}
