#include<iostream>
#include<set>
using namespace std;
const int maxn=100000;
char ch;
set<string> hash;
int lc[maxn],rc[maxn],tot,tt,cases;
double p[maxn];
string q[maxn];
void read1(char ch1)
{
     while (1)
     {
           scanf("%c",&ch);
           if (ch==ch1) return;
     }
}

int readtree()
{
     tot++;
     int tmp;
     tmp=tot;
     scanf("%lf",&p[tot]);
     q[tot]="";
     while (1)
     {
           scanf("%c",&ch);
           if ((ch>='a')&&(ch<='z')) break;
           if (ch==')')
           {
              lc[tot]=-1;
              rc[tot]=-1;
              return tmp;
           }
     }
     while (1)
     {
           q[tot]+=ch;
           scanf("%c",&ch);
           if ((ch>='a')&&(ch<='z')) continue;
           break;
     }
     read1('(');
     lc[tmp]=readtree();
     read1('(');
     rc[tmp]=readtree();
     read1(')');
     return tmp;
}

void init()
{
     read1('(');
     tot=0;
     readtree();     
     printf("Case #%d:\n",tt+1);
}

void work()
{
     int x,y;
     double ans;
     string ss;
     for (scanf("%d",&x);x;x--)
     {
         cin >> ss;
         hash.clear();
         for (scanf("%d",&y);y;y--)
         {
             cin >> ss;
             hash.insert(ss);
         }
         y=1;
         ans=1;
         while (y!=-1)
         {
               ans*=p[y];
               if (hash.count(q[y])) y=lc[y];
               else y=rc[y];
         }
         printf("%.7lf\n",ans);
     }     
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
    }
    return 0;       
}
