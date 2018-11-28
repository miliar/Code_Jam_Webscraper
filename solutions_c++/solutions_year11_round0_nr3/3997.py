#include <iostream>
#define maxn 1001
#define For(i,a,b) for(int i=a;i<=b;i++)
#define FOR(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
int test,n;
int c[maxn];
int mu[maxn];

void initialize()
{
    mu[0]=1;    
    For(i,1,21) mu[i]=mu[i-1]*2;            
}

char* phantich(int n)
{
    char* quynh=new char[22];
    FOR(i,21,0)
        if (n>=mu[i])
            {
                n-=mu[i];
                quynh[i]='1';
            }
        else
            quynh[i]='0';
    return quynh;
}

char* add(char* x,char* y)
{
    char* temp= new char[22];
    For(i,0,21)
        if (x[i]!=y[i]) temp[i]='1';
        else temp[i]='0';
    return temp;
}

bool equal(char* x,char* y)
{
    For(i,0,21) 
        if (x[i] != y[i]) return false;
    return true;
}

void solve()
{
    int sum=0,result=-1;    
    For(i,1,n) sum+=c[i];
    For(x,0,mu[n]-1)
        {
            int temp=0;
            char* quynh=phantich(x);
            For(i,0,n-1) if (quynh[i]== '1') temp+=c[i+1];                            
            if (temp>result && temp<sum)
                {            
                    char* ben1=new char[22];
                    char* ben2=new char[22];                    
                    For(i,0,21) {ben1[i]='0';ben2[i]='0';};
                    For(i,0,n-1)
                        if (quynh[i]=='1')
                            ben1=add(ben1,phantich(c[i+1]));
                        else
                            ben2=add(ben2,phantich(c[i+1]));
                    if (equal(ben1,ben2))
                        result=temp;
                }
        }
    if (result == -1) 
        cout<<"NO";
    else
        cout<<result;
}

void enter()
{
    initialize();
    scanf("%d",&test);
//    test=1;
    For(ntest,1,test)
        {
            scanf("%d",&n);
            For(i,1,n) scanf("%d",&c[i]);
            cout<<"Case #"<<ntest<<": ";
            solve();
            if (ntest<test) cout<<endl;
        }
}


int main()
{
    freopen("csmall2.in","r",stdin);
    freopen("csmall.out","w",stdout);
    enter();        
}
