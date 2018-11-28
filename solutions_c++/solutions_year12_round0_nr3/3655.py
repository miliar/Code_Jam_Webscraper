#include<iostream>
#include<cstring>
using namespace std;

int bit(int x)
{
    int i=1;
    while (1) 
    {
          x/=10;
          if (x==0) break;
          i++;
    }
    return i;
}

int mov(int a, int b)
{
    int j;
    while (a%10==0) a/=10;
    j=a%10;
    while(--b) j*=10;
    a/=10;
    j+=a;
    return j;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
    int i,T;
    bool b[2000000];
    
    cin>>T;
    for (i=1;i<=T;i++)
    {
        int A,B,s,t=0;
        int j,k,l,m,n;
        
        memset(b,0,sizeof(b));
        cin>>A>>B;
        for(j=A;j<=B;j++)
        {
                               if (b[j]==1) continue;
                               b[j]=1;
                               s=1;m=j;
                               while(1)
                               {
                                         k=mov(m, bit(m));
                                         if (k>=A && k<=B && b[k]==0) s++;
                                         m=k;
                                         b[m]=1;
                                         if (m==j) break;
                               }
                               t+=(s*(s-1)/2);
        }     
        cout<<"Case #"<<i<<": "<<t<<endl;
        //for (n=0;n<2000000;n++) if(b[n]==1) cout<<n<<" ";
    }
	return 0;
}

