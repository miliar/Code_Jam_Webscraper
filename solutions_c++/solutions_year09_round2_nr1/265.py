#include <iostream>
#include <set>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

typedef double D;

char buf [100],cc,naw;

set<string> S;
struct node
{
    node *L;
    node *R;
    D w;
    string name;
    node() {
        L=NULL;
        R=NULL;
        w=0.0;
        name="";
    }
    D licz()
    {
        if(L==NULL) return w;
//        printf("%.6lf\n",w);
        if(S.find(name)==S.end()) return w*(R->licz());
        else return w*(L->licz());
    }
    void read()
    {
        scanf(" %c%lf",&naw,&w);
        while(1)
        {
            scanf("%c",&cc);
            if(cc=='\n') break;
            if(cc!=' ') name.insert(name.end(),cc);
            if(cc==')') break;
        }

            if(name[name.size()-1]==')')
            {
                name="";
                return;
            }
  //      printf("dla %.2lf name = %s\n\n",w,name.c_str());
        L=new node(); L->read(); 
        R=new node(); R->read();
        scanf("%c",&naw);
//        printf("haeelo %c\n",naw);
        if(naw!=')') 
        {
            scanf(" %c",&naw);
    ///        printf("czy to awaias = = %c\n",naw);
        }
    }
    void out()
    {
        printf("%.2lf %s\n",w,name.c_str());
        if(L) L->out();
        if(R) R->out();
    }
};

node *T;

void solve()
{
    int del;
    scanf("%d",&del);
    T=new node();
    T->read();
//    T->out();
    int q;
    scanf(" %d",&q);
  //  printf("q =%d\n",q);
 //   return;
    fru(i,q)
    {
        S.clear();
        int n;
        scanf("%s %d",buf,&n);
        fru(j,n)
        {
            scanf("%s ",buf);
            S.insert((string) buf);
        }
        printf("%.07lf\n",T->licz());
    }
}

int main()
{
    int t;
    scanf("%d",&t);
    fru(i,t) 
    {
        printf("Case #%d:\n",i+1);
        solve();
    }
#ifdef __WIN32
 //  system ("pause");
#endif
return 0;
}
