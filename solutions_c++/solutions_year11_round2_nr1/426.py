#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iostream>
#include <queue>
#include <cstring>
#include <stack>
#include <bitset>
using namespace std;

int n;
char ma[101][101];

double wp[101];
double owp[101];
double oowp[101];

void WP()
{
    for(int i=0;i<n;i++)
    {
        double win=0;
        double tot=0;
        for(int k=0;k<n;k++)
        {
            if(ma[i][k]=='1')
                win++;
            if(ma[i][k]!='.')
                tot++;
        }
        wp[i]=win/tot;
    }
}

void OWP()
{
    for(int i=0;i<n;i++)
    {
        double res=0;
        double tot2=0;
        for(int k=0;k<n;k++)
        {
            double win=0;
            double tot=0;
            if(i==k)continue;
            if(ma[k][i]=='.')continue;
            tot2++;
            for(int j=0;j<n;j++)
            {
                if(j==i)continue;
                if(ma[k][j]=='1')
                    win++;
                if(ma[k][j]!='.')
                    tot++;
            }
            res+=win/tot;
        }
        res/=tot2;
        owp[i]=res;
    }
}

void OOWP2()
{
    for(int i=0;i<n;i++)
    {
        double res=0;
        double tot=0;
        for(int k=0;k<n;k++)
        {
            if(i==k)continue;
            if(ma[k][i]=='.')continue;
            tot++;
            res+=owp[k];
        }
        res/=tot;
        oowp[i]=res;
    }
}

void OOWP()
{
    for(int i=0;i<n;i++)
    {
        double res=0;
        double tot2=0;
        for(int k=0;k<n;k++)
        {
            double win=0;
            double tot=0;
            if(i==k)continue;
            if(ma[k][i]=='.')continue;
            tot2++;
            for(int j=0;j<n;j++)
            {
                double w=0;
                double t=0;
                if(j==i || j==k)continue;
                if(ma[j][k]=='.')continue;
                tot++;
                for(int r=0;r<n;r++)
                {
                    if(r==i || r==k)continue;
                    if(ma[j][r]=='1')
                        w++;
                    if(ma[j][r]!='.')
                        t++;
                }
                if(t>0)
                    win+=w/t;
            }
            if(tot>0)
                win/=tot;
            res+=win;
        }
        if(tot2>0)
            res/=tot2;
        oowp[i]=res;
    }
}


int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",ma[i]);

        WP();
        OWP();
        OOWP2();

        printf("Case #%d:\n",I+1);
        for(int i=0;i<n;i++)
        {
            printf("%lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }

    }
}

/*
int n,m;
string D[10001];
char L[30];
string guess;
int cont;
bitset<10001> b;
int maxi;
string res;

bool check(string &s,string &ss,char c)
{
    for(int i=0;i<s.size();i++)
    {
        if(s[i]==c && ss[i]!=c)
            return false;
    }
    return true;
}

void solve()
{
    maxi=0;
    res=D[0];
    for(int i=0;i<n;i++)
    {
        guess=D[i];
        cont=n;
        int temp=0;
        b=0;
        for(int k=0;k<n;k++)
        {
            if(D[k].size()!=guess.size())
            {
                b[k]=1;
                cont--;
            }
        }

        //printf("%s %d\n",guess.c_str(),cont);

        for(int k=0;k<26;k++)
        {
            if(cont==1)
            {
                break;
            }
            bool ok=false;
            for(int j=0;j<n;j++)
            {
                if(!b[j])
                {
                    if(D[j].find(L[k])!=string::npos)
                    {
                        ok=true;
                        break;
                    }
                }
            }
            if(!ok) continue;
            
           // printf(">%c\n",L[k]);

            bool si=false;
            if(guess.find(L[k])!=string::npos)
                si=true;

            if(!si) temp++;
            for(int j=0;j<n;j++)
            {
                if(!b[j])
                {
                    if(!si)
                    {
                        if(D[j].find(L[k])!=string::npos)
                        {
                            b[j]=1;
                            cont--;
                        }
                    }else
                    {
                        if(!check(guess,D[j],L[k]))
                        {
                            b[j]=1;
                            cont--;
                        }
                    }
                }
            }
        }

        if(temp>maxi)
        {
            maxi=temp;
            res=guess;
        }
    }

    printf("%s",res.c_str());
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int I=0;I<T;I++)
    {
        char temp[20];
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%s",temp);
            D[i]=temp;
        }
        printf("Case #%d: ",I+1);
        for(int i=0;i<m;i++)
        {
            scanf("%s",L);
            solve();
            if(i<m-1)
                printf(" ");
        }
        printf("\n");
    }
}

/*
#define dos pair<int,int> 
#define cost first
#define state second

int n,m;
char ma[30][30];

dos dp[262145][21];
int pre[262145];

inline int set(int &p,int pos,int val)
{
    return (p|(3<<(pos*2)))&(val<<(pos*2));
}

inline int get(int &p,int pos)
{
    return (p>>(pos*2))&3;
}

inline bool check(int &a,int &b)
{
    bool cero=true;
    bool tres=false;
    for(int i=0;i<m;i++)
    {
        if(i>0 && (get(b,i-1)*get(b,i)==1 || get(b,i-1)*get(b,i)==2 || get(b,i-1)*get(b,i)==4 ))
            return false;

        if(get(b,i)==1 && (get(a,i)==0 || get(a,i)==2))
            return false;
        if(get(b,i)==3 && (get(a,i)==1 || get(a,i)==3))
            return false;
        if(get(b,i)==2 && (get(a,i)==1 || get(a,i)==3))
            return false;

        if(get(a,i)==1 && (get(b,i)==0 || get(b,i)==2))
            return false;
        if(get(a,i)==2 && (get(b,i)==1 || get(b,i)==0))
            return false;
        if(get(a,i)==3 && (get(b,i)==2 || get(b,i)==3))
            return false;

        if(get(b,i)==2 && i>0 && i<m-1 && get(b,i-1)==0 && get(b,i+1)==0 && get(a,i)==0)
            return false;

        if(get(b,i)==3 && cero)
        {
            tres=true;
        }else
            if(get(b,i)==0 && tres)
            {
                return false;
            }
        if(get(b,i)==0)
            cero=true;
        else
            if(get(b,i)==1 || get(b,i)==2)
            {
                cero=false;
            }

        if(get(b,i)!=3)
            tres=false;
    }
    if(cero && tres)
        return false;

    if(m>1 && get(b,0)==2 && get(b,1)==0 && get(a,0)==0)
        return false;

    if(m>1 && get(b,m-1)==2 && get(b,m-2)==0 && get(a,m-1)==0)
        return false;


    return true;
}

inline bool checkF(int &b)
{
    if(get(b,0)!=1)
        return false;

    bool cero=true;
    bool tres=false;
    for(int i=0;i<m;i++)
    {
        if(i>0 && (get(b,i-1)*get(b,i)==1 || get(b,i-1)*get(b,i)==2 || get(b,i-1)*get(b,i)==4 ))
            return false;

        if(get(b,i)==1 && i<m-1)
            return false;

        if(get(b,i)==2 && i>0 && i<m-1 && get(b,i-1)==0 && get(b,i+1)==0)
            return false;

        if(get(b,i)==3 && cero)
        {
            tres=true;
        }else
            if(get(b,i)==0 && tres)
            {
                return false;
            }
        if(get(b,i)==0)
            cero=true;
        else
            if(get(b,i)==1 || get(b,i)==2)
            {
                cero=false;
            }

        if(get(b,i)!=3)
            tres=false;
    }
    if(cero && tres)
        return false;

    if(m>1 && get(b,0)==2 && get(b,1)==0)
        return false;


    return true;
}

void print(int a)
{
    for(int i=0;i<m;i++)
    {
        printf("%d ",get(a,i));
    }
}

string convert(int a)
{
    string res="";
    for(int i=0;i<m;i++)
    {
        if(get(a,i)!=0)
            res+='C';
        else
            res+='.';
    }
    reverse(res.begin(),res.end());
    return res;
}

int cc;

dos memo(int s,int lvl)
{
    if(dp[s][lvl].cost!=-1)
        return dp[s][lvl];

    print(s);
    printf("%*d %s\n",lvl,lvl,convert(s).c_str());

    if(lvl==n)
    {
        int cont=0;
        for(int i=0;i<m;i++)
            if(get(s,i)>0)
                cont++;
        int cccccc=0;
        int t=set(cccccc,m-1,2);
        if(check(s,t))//get(s,m-1)==1)
        {
            printf(".");
            return dp[s][lvl]=make_pair(cont,-1);
        }
        else
            return dp[s][lvl]=make_pair(0,-1);
    }

    int maxi=-1;
    int f=-1;
    for(int i=0;i<cc;i++)
    {
        if(check(s,i))
        {
            if(lvl==0 && 0)
            {
                print(i);
                printf("%s\n",convert(i).c_str());
            }
            if(memo(i,lvl+1).cost>maxi)
            {
                maxi=memo(i,lvl+1).cost;
                f=i;
            }
        }
    }

    //print(f);
    //printf("%*d %s\n",lvl,lvl,convert(f).c_str());

    return dp[s][lvl]=make_pair(maxi,f);
}


void makePre(int p,int pos)
{
    if(pos<m)
    {
        for(int i=0;i<4;i++)
            makePre(set(p,pos,i),pos+1);
    }else
    {
        pre[cc]=p;
        cc++;
    }
}




int main()
{
    scanf("%d%d",&n,&m);
    while(n!=0)
    {
        for(int i=0;i<n;i++)
        {
            scanf("%s",ma[i+1]);
            reverse(ma[i+1],ma[i+1]+m);
        }
        for(int i=0;i<m;i++)
        {
            ma[0][i]='.';
            ma[n+1][i]='.';
        }
        
        memset(dp,-1,sizeof(dp));
        cc=0;
        
        makePre(0,0);
        
        dos res=memo(2,0);
        printf("%d %d\n",cc,res.cost);

        int lvl=0;
        while(lvl<n && res.state!=-1)
        {
            printf("%s\n",convert(res.state).c_str());
            res=dp[res.state][lvl+1];
            lvl++;
        }
        
        scanf("%d%d",&n,&m);
    }
}


/*
int n,x;
int ma[101];
int DP[51][101][101];

int dp(int cua,int ini,int fin)
{
    if(DP[cua][ini][fin]!=-1)
        return DP[cua][ini][fin];
    
    if(ini==fin) return (cua==0?0:x-cua);

    int col=ma[ini];
    int p=ini;
    for(;p<fin;p++)
    {
        if(ma[p]!=col)
        {
            break;
        }
    }
    
    int cuantos=cua+p-ini;
    if(cuantos>x)
        cuantos=x;
    
    //op1: sumarle
    DP[cuantos][ini][fin]=x-cuantos + dp(0,p,fin);
    
    //op2: unir
    int pp=p;
    for(;pp<fin;pp++)
        if(ma[pp]==col)
            break;
    if(pp!=p)
        DP[cuantos][ini][fin]=min(DP[cuantos][ini][fin],dp(0,p,pp)+dp(cuantos,pp,fin));

    printf("%d %d %d %d\n",cua,ini,fin,DP[cuantos][ini][fin]);
    return DP[cuantos][ini][fin];
}

int main()
{
    scanf("%d%d",&n,&x);
    for(int i=0;i<n;i++)
        scanf("%d",&ma[i]);
   
    memset(DP,-1,sizeof(DP));

    printf("%d\n",dp(0,0,n));

}
*/

/*
int dp[101][101];

int DP(int b,int c)
{
    if(dp[b][c]!=-1)
        return dp[b][c];

    if(b==0 && c==1)
        return 0;

    int maxi=0;
 //   if(b==1)
  //      maxi=1;
   // if(c==b+2)
    //    maxi=1;
    for(int i=0;i<b;i++)
        maxi=max(maxi,DP(i,b));
    for(int i=b+1;i<c;i++)
    {
        maxi=max(maxi,DP(i-b,c-b));
    }
    return dp[b][c]=1+maxi;
}

int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    b-=a;
    c-=a;

    memset(dp,-1,sizeof(dp));

    //printf("%d",DP(b,c));
    printf("%d\n",max(b,c-b)-1);
}
*/

/*
char s[12];
string res[2015];
int pos=0;
//CAGBIHEFJDK
int check()
{
    char c[12];
    for(int i=0;i<11;i++)
        c[i]=s[i];
    int cont=0;
    for(int i=0;i<11;i++)
    {
        if(c[i]=='A'+i)continue;
        if(c[10]=='A'+i)
        {
            reverse(c+i,c+11);
            cont++;
        }else
        {
            int p=0;
            for(int k=0;k<11;k++)
                if(c[k]=='A'+i)
                {
                    p=k;
                    break;
                }
            reverse(c+p,c+11);
            cont++;
            reverse(c+i,c+11);
            cont++;
        }
    }
    return cont;
}

int main()
{
    for(int i=0;i<11;i++)
    {
        s[i]='A'+i;
    }


    int maxi=1;
    int temp;
    int cont=0;
    do
    {
        cont++;
        if(cont%1000000==0)
        {
            printf("%d %d %d\n",maxi,cont,pos);
        }
        temp=check();
        //printf("%s %d\n",s,temp);
        if(temp==maxi)
        {
            if(pos<2015)
                res[pos]=s;
            pos++;
        }else
            if(temp>maxi)
            {
                maxi=temp;
                pos=0;
            }
    }while(next_permutation(s,s+11));

    printf("hola\n");
    sort(res,res+2015);

    printf("%s\n",res[2009].c_str());
    printf("%s\n",res[2010].c_str());
    printf("%s\n",res[2011].c_str());
    printf("%s\n",res[2012].c_str());
    printf("%s\n",res[2013].c_str());

}

 */
