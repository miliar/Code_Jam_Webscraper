#include <iostream>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cstdio>
using namespace std;
ifstream fcin("C-large.in");
ofstream fcout("C-large-result.out");
int f[1005];
int main()
{
    int t,n,tt=1;
    fcin>>t;
    while(t--)
    {
        fcin>>n;
        int sum=0,ans=0;
        for(int i=0;i<n;i++){
             fcin>>f[i];
             sum ^= f[i];
             ans+=f[i];
        }
        fcout<<"Case #"<<tt++<<": ";
        if(sum != 0) fcout<<"NO"<<endl;
        else
        {
            sort(f,f+n);
            fcout<<ans-f[0]<<endl;
        }
    }
    return 0;
}
/*
int vis[50][50],map[50][50],f[105];
char ans[105];
int main()
{
    int t,a,b,c,tt=1;
    char ss,s[50];
    fcin>>t;
    while(t--)
    {
        memset(vis,-1,sizeof(vis));
        memset(map,0,sizeof(map));
        fcin>>a;
        for(int j=0;j<a;j++)
        {
            fcin>>s;
            vis[s[0]-'A'][s[1]-'A']=vis[s[1]-'A'][s[0]-'A']=s[2]-'A';
            //cout<<s[2]-'A'<<endl;
        }
        fcin>>b;
        for(int j=0;j<b;j++)
        {
            fcin>>s;
            map[s[0]-'A'][s[1]-'A']=map[s[1]-'A'][s[0]-'A']=1;
        }
        fcin>>c;
        for(int j=0;j<c;j++)
        {
            fcin>>ss;
            f[j]=ss-'A';
            //cout<<f[j]<<' ';
        }
        //cout<<endl;
    //}
    int flag,n;
    for(int i=1;i<c;i++)
    {
        flag = 0,n=0;
        for(int j=i-1;j>=0;j--)
        {
            if(f[j]!=-1) n++;
            if(n==1 && f[j]!=-1 && vis[f[i]][f[j]]!=-1)
            {
                //cout<<"hello,world"<<vis[f[i]][f[j]]<<endl;
                f[i]=vis[f[i]][f[j]];
                f[j]=-1;
                flag = 1;
            }
            else if(map[f[i]][f[j]]==1)
            {
                for(int k=j;k<=i;k++)
                {
                    f[k]=-1;
                }
                flag = 1;
            }
            if(flag) break;
        }
        //printf("%d %c ",f[i],f[i]+'A');
    }
    int kk=0;
    for(int i=0;i<c;i++)
    {
        if(f[i]!=-1)
        ans[kk++]=f[i]+'A';
    }
    fcout<<"Case #"<<tt++<<": ";
    if(kk == 0) { fcout<<"[]"<<endl;continue;}
    fcout<<"[";
    for(int i=0;i<kk-1;i++)
    fcout<<ans[i]<<", ";
    fcout<<ans[kk-1]<<"]"<<endl;
}
    return 0;
}
/*
ifstream fin("A-large.in");
ofstream fout("A-large-result.out");
struct node
{
    int num;
    int flag;
};
node x[205],y[205];
int main()
{

    int t,n,b,c,d,tt=1;
    char a;
    fin>>t;
    while(t--)
    {
        fin>>n;
        c = d = 0;
        for(int i=0;i<n;i++)
        {
            fin>>a>>b;
            if(a=='O')
            {
                x[c].num=b;
                x[c++].flag=i;
            }
            else if(a=='B')
            {
                y[d].num=b;
                y[d++].flag=i;
            }
        }
        int anss = 0;
        int cc=0,dd=0;
        int nn=1,mm=1;
        for(int i=0;i<n;i++)
        {
            if(cc<c && x[cc].flag==i)
            {
                int tem = x[cc].num;
                int ans = abs(tem - nn) + 1;
                anss += ans;
                nn = tem;
                if(dd<d){
                if(abs(y[dd].num-mm)<=ans)
                {
                    mm=y[dd].num;
                }
                else
                {
                    //y[dd].num = mm - ans;
                    if(mm > y[dd].num)
                    {
                        mm -= ans;
                    }
                    else
                    {
                        mm += ans;
                    }
                }
                }
                cc++;
            }
            else if(dd<d && y[dd].flag==i)
            {
                int tem = y[dd].num;
                int ans = abs(tem - mm) + 1;
                anss += ans;
                mm = tem;
                if(cc<c){
                if(abs(x[cc].num-nn)<=ans)
                {
                    nn=x[cc].num;
                }
                else
                {
                    //y[dd].num = mm - ans;
                    if(nn > x[cc].num)
                    {
                        nn -= ans;
                    }
                    else
                    {
                        nn += ans;
                    }
                }
                }
                dd++;
            }
            //dd++;
        }
        fout <<"Case #"<<tt++<<": ";
        fout << anss << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
*/
