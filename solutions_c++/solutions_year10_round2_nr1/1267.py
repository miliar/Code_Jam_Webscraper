#include<iostream>
#include<cstdio>
#define N 100
#define M 100

using namespace std;
char paths[N+M][101];
char dirs[M][101];

int n,m;

int calcDiff(int p,int d)
{
    int i=0,lf=0;
    if(n!=0 && p>=0)
    {
    while(paths[p][i]==dirs[d][i])
    {
        if(paths[p][i]=='\0')
            return 0;
        if(paths[p][i]=='/')
            lf=i;
            i++;
    }
    if(paths[p][i]=='/' && dirs[d][i]=='\0')
        return 0;
    if(paths[p][i]!='\0' || dirs[d][i]!='/')
    i=lf;
    }
    int t=0;
    while(dirs[d][i]!='\0')
    {

        if(dirs[d][i]=='/')
        t++;
        i++;
    }
    return t;
}

void addDirToPath(int index)
{
    int i=0;
    while(dirs[index][i]!='\0')
    {
        paths[n][i]=dirs[index][i];
        i++;
    }
    paths[n][i]='\0';
    n++;
}
int calCommand(int index)
{
    int i;
    int d,t;
    d=calcDiff(-1,index);
    for(i=0;i<n;i++)
    {
        t=calcDiff(i,index);
        if(d>t)
            d=t;
    }
    addDirToPath(index);
    return d;

}
int main()
{
    int i,ti,t;
    int c;
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        c=0;//ans
        cin>>n>>m;
        for(i=0;i<n;i++)
        scanf("%s",paths[i]);
        for(i=0;i<m;i++)
        scanf("%s",dirs[i]);
        //inp finished

        for(i=0;i<m;i++)
        c=c+calCommand(i);

        printf("Case #%d: %d\n",ti,c);

   }

    return 0;
}
