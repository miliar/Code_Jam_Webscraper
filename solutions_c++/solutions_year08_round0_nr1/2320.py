#include <iostream>
#include <cstring>
#include <map>
#include <fstream>
using namespace std;

ifstream fin("A-small.in");
ofstream fout("A-small.out");


int N,M;
string name[1000];
map<string,int> nametoid;
int Query[2000];

int dp[2000][200];


void init()
{
    char temp[2000];
    fin>>N;
    fin.getline(temp,1500,'\n');
    
    for (int i=1;i<=N;++i)
    {
        fin.getline(temp,1500,'\n');
        string s(temp);
        nametoid[s]=i;
    }
    
    fin>>M;
    fin.getline(temp,1500,'\n');
    
    for (int i=1;i<=M;++i)
    {
        fin.getline(temp,1500,'\n');
        string s(temp);
        Query[i]=nametoid.find(s)->second;
    }    
}

int curid;

void start()
{
    int i,j,k;
    for (i=1;i<=N;++i) if (Query[1]!=i) dp[1][i]=0; else dp[1][i]=999999;
    
    for (k=2;k<=M;++k)
    {
        for (i=1;i<=N;++i) dp[k][i]=999999;
        for (i=1;i<=N;++i) if (Query[k] != i) 
        {
            for (j=1;j<=N;++j) 
            {
                if (j==i && dp[k-1][j]<dp[k][i]) dp[k][i]=dp[k-1][j];
                if (dp[k-1][j]+1<dp[k][i]) dp[k][i]=dp[k-1][j]+1;
            }
        }
    }
    
    int ans=999999;
    for (i=1;i<=N;++i) if (dp[M][i]<ans) ans=dp[M][i];
    
    fout<<"Case #"<<curid<<": "<<ans<<endl;
}


void deal()
{
    init();     
    start();
}



int main()
{
    int t;
    fin>>t;
    for (curid=1;curid<=t;++curid) deal();
    
    system("pause");
}
