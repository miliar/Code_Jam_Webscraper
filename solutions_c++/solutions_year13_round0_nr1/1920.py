//This is the painkiller...
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<queue>
#include<math.h>
#include<stdlib.h>
#include<stack>
#include<string.h>
#include<string>
#include<map>
#include<algorithm>
#include<time.h>
#include<set>
#include<vector>
using namespace std;
#define fin(a) freopen(a,"r",stdin)
#define fout(a) freopen(a,"w",stdout)
#define abv(a) ((a)>0?(a):-(a))
#define sqr(a) ((a)*(a))
#define fs(i,s) for(int i=0;s[i];i++)
#define fg(e,u) for(int e=L[u];e!=-1;e=pre[e])
#define f0(i,n) for(int i=0;i<(n);i++)
#define f1(i,a,n) for(int i=(a);i<(n);i++)
#define f2(i,a,n,b) for(int i=(a);i<(n);i+=(b))
#define rf0(i,n) for(int i=(n);i>=0;i--)
#define rf1(i,a,n) for(int i=(a);i>(n);i--)
#define rf2(i,a,n,b) for(int i=(a);i>(n);i-=(b))
#define mem(a,v) memset(a,v,sizeof(a))
#define pq priority_queue
#define pb push_back
#define pq priority_queue
#define sz size
#define vint vector<int>
#define vvint vector<vector<int> >
#define vstr vector<string>
#define emt empty
#define clr clear
#define bn begin
#define en end
#define all(a) a.bn(),a.en()
#define dlt(v,a) v.erase(v.bn()+a)
#define dlst(v) v.erase(v.bn()+((int)v.size()-1))
#define nset(S,v) S.erase(find(v))
#define scn(a,b,n) f1(j,b,n+b)cin>>a[j]
#define scm(a,b,c,m,n) f1(i,b,m+b)scn(a[i],c,n)
#define prn(a,b,n) f1(j,b,n+b){if(j>b)cout<<' ';cout<<a[j];}
#define prm(a,b,c,m,n) f1(i,b,m+b){prn(a[i],c,n);cout<<endl;}
#define greater(a,b) ((a)>(b)+eps)
#define zero(a) (fabs(a)<eps)
#define Int __int64
#define Long long long
const double Pi=acos(-1.0);
Long mod=1000000007;
#define inf (1<<30)
#define eps 1e-9
#define MAX 1005
//struct pii{int x,y;pii(int a=0,int b=0){x=a,y=b;}};
//bool operator<(pii a,pii b){return a.x<b.x||(a.x==b.x&&a.y<b.y);}
//int L[],pre[],to[],C[],ne;
//inline void addEdge(int u,int v,int c=1){to[ne]=v,pre[ne]=L[u],C[ne]=c;L[u]=ne++;}

char str[4][5];

int check()
{
    char tmp[5];
    f0(i,4)
    {
        strcpy(tmp,str[i]);
        sort(tmp,tmp+4);
        if(strcmp(tmp,"TXXX")==0||strcmp(tmp,"XXXX")==0)return 0;
        if(strcmp(tmp,"OOOT")==0||strcmp(tmp,"OOOO")==0)return 1;
    }
    f0(j,4)
    {
        f0(i,4)tmp[i]=str[i][j];tmp[4]=0;
        sort(tmp,tmp+4);
        if(strcmp(tmp,"TXXX")==0||strcmp(tmp,"XXXX")==0)return 0;
        if(strcmp(tmp,"OOOT")==0||strcmp(tmp,"OOOO")==0)return 1;
    }

    f0(i,4)tmp[i]=str[i][i];tmp[4]=0;
    sort(tmp,tmp+4);
    if(strcmp(tmp,"TXXX")==0||strcmp(tmp,"XXXX")==0)return 0;
    if(strcmp(tmp,"OOOT")==0||strcmp(tmp,"OOOO")==0)return 1;

    f0(i,4)tmp[i]=str[3-i][i];tmp[4]=0;
    sort(tmp,tmp+4);
    if(strcmp(tmp,"TXXX")==0||strcmp(tmp,"XXXX")==0)return 0;
    if(strcmp(tmp,"OOOT")==0||strcmp(tmp,"OOOO")==0)return 1;

    f0(i,4)f0(j,4)if(str[i][j]=='.')return 2;

    return 3;
}
int main()
{
    ios_base::sync_with_stdio(false);
    //fin("in.txt");
    //fout("out.txt");
    int tst,cas=0;cin>>tst;
    while(tst--)
    {
        f0(i,4)cin>>str[i];
        int f=check();
        cout<<"Case #"<<++cas<<": ";
        if(f==0)cout<<"X won";
        if(f==3)cout<<"Draw";
        if(f==1)cout<<"O won";
        if(f==2)cout<<"Game has not completed";
        cout<<endl;
    }
	return 0;
}
