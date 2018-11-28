#include <fstream>
using namespace std;


ifstream fin("train.in");
ofstream fout("train.out");


bool map[201][201],b[201];
long t,na,nb,father[201],train[201][2];

long gettime()
{
    string str;
    fin>>str;
    return ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
}

void init()
{
    fin>>t;
    fin>>na>>nb;
    memset(map,false,sizeof(map));
    memset(father,0,sizeof(father));
    for(long i=1;i<=na;i++)
    {
        train[i][0]=gettime();
        train[i][1]=gettime();
    }
    for(long i=na+1;i<=nb+na;i++)
    {
        train[i][0]=gettime();
        train[i][1]=gettime();
    }
}

void match()
{
    for (long i=1;i<=na;i++)
        for(long j=na+1;j<=nb+na;j++)
            if (train[i][1]+t<=train[j][0])
                map[i][j]=true;
    for (long i=1;i<=na;i++)
        for(long j=na+1;j<=nb+na;j++)
            if (train[j][1]+t<=train[i][0])
                map[j][i]=true;
}

bool dfs(long v)
{
    b[v]=false;
    if (v<=na)
    {
        for(long i=na+1;i<=na+nb;i++)
            if (map[v][i])
            {
                if((father[i]==0)||(b[father[i]]&&dfs(father[i])))
                {
                    father[i]=v;
                    b[v]=true;
                    return true;
                }
            }
    }
    if (v>na)
    {
        for(long i=1;i<=na;i++)
            if (map[v][i])
            {
                if((father[i]==0)||(b[father[i]]&&dfs(father[i])))
                {
                    father[i]=v;
                    b[v]=true;
                    return true;
                }
            }
    }
    return false;
}

void hungary()
{
    for (long i=1;i<=na+nb;i++)
    {
        memset(b,true,sizeof(b));
        dfs(i);
    }
    long sum=0;
    for (long i=1;i<=na;i++)
        sum+=(father[i]==0);
    fout<<sum<<' ';
    sum=0;
    for (long i=na+1;i<=na+nb;i++)
        sum+=(father[i]==0);
    fout<<sum<<endl;
}

int main()
{
	long n;
	fin>>n;
	for(long i=1;i<=n;i++)
	{
	    init();
	    match();
	    fout<<"Case #"<<i<<": ";
	    hungary();
	}
	return 0;
}
