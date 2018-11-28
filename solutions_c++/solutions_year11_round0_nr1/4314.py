#include<iostream>
#include <cmath>
#define maxn 101
#define For(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
int n,test;
char name[maxn];
int button[maxn];


void solve()
{
    int u=1,v=1;
    bool chua[maxn];
    memset(chua,true,sizeof(chua));
    int dem=n,result=0;     
    while(dem)
        {
            dem--;
            For(i,1,n) if (chua[i])
                {
                    chua[i]=false;                    
                    int tam;
                    char robotname=name[i];
                    if (robotname == 'O' || robotname == 'o')
                        tam=abs(button[i]-u)+1;
                    else
                        tam=abs(button[i]-v)+1;                                                               
                    int j;
                    for(j=1;j<=n;j++)
                        if (chua[j] && name[j]!=name[i])
                            break;
                    if (robotname == 'O' || robotname == 'o')
                        u=button[i];
                    else
                        v=button[i];                    
                    result+=tam;
                    if (j<=n)
                        {
                            if (name[j]== 'O' || name[j]== 'o')
                                {
                                    int vovan=min(tam,abs(button[j]-u));
                                    if (button[j]<u) u-=vovan;else u+=vovan;
                                }
                            else
                                {
                                    int vovan=min(tam,abs(button[j]-v));
                                    if (button[j]<v) v-=vovan;else v+=vovan;
                                }                        
                        }//end if j<=n
                    break;
                }                    
        }
    cout<<result;
}

void enter()
{
    scanf("%d",&test);
//    test=1;
    For(ntest,1,test)
        {
            scanf("%d",&n);    
            char temp;        
            scanf("%c",&temp);
            For(i,1,n)
                {
                    scanf("%c %d",&name[i],&button[i]);
                    scanf("%c",&temp);                    
                }                 
            cout<<"Case #"<<ntest<<": ";                     
            solve();
            if (ntest<test) cout<<endl;
        }//end for ntest
}
int main()
{
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    enter();
    return 0;
}
