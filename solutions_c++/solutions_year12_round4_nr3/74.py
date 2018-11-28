#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

int h[4000];
int f[4000];
int n;
int last[4000];
int start[4000];

int get_hight(int x,int a,int b)
{
    int H=h[a],L=0;
    if (b<a)
    {
        int tmp=b;b=a;a=tmp;
    }
    

    while (H>L)
    {
        int mid=(H+L)/2+1;
        double x1=b-a,x2=x-a,y1=h[b]-h[a],y2=mid-h[a];
    
        double cross=y1*x2-y2*x1;
    
        if (cross>0) L=mid;else H=mid-1;
    }
    
//    cout << x << ' ' << a << ' ' << b << ' ' << H << endl;
    return H;
}


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("cc.out","w",stdout);
    int NT,CT=0;
    cin >> NT;
    while (NT)
    {
        NT--;CT++;
        
        cin >> n;
        for (int i=0;i<n-1;i++) cin >> f[i];
        int flag=1;
        for (int i=0;i<n-1;i++) if (f[i]<=i+1) flag=0;
        if (flag==0)
        {
            printf("Case #%d: Impossible\n",CT);
            continue;
        }
        
        
        
        for (int i=0;i<n;i++) h[i]=-1;
        
        memset(start,0,sizeof(start));
        memset(last,0,sizeof last);
        h[n-1]=1000000000;
        h[n]=999999999;
        start[n-1]=0;
        last[n-1]=n;
        
        for (int i=n-1;i>0;i--)
        {
            for (int j=start[i];j<i;j++) if (f[j]>i+1) 
            {
                flag=0;
                         //   cout << i << ' ' << start[i] << endl << flush;
                        }
            if (flag==0) break;
            
            int ll=last[i];
            for (int j=start[i];j<i;j++) if (f[j]==i+1)
            {
                if (ll!=last[i]) start[j]=ll+1;else start[j]=start[i];
                    h[j]=get_hight(j,i,ll);//cout << j << ' ' <<h[j] << endl;
                    ll=j;
                last[j]=i;
            }
            
        }
//        for (int i=0;i<n;i++) cout << start[i] << ' ';cout << endl << flush;
        for (int i=0;i<n;i++) if (h[i]<0) flag=0;
        if (flag==0)
        {
            printf("Case #%d: Impossible\n",CT);
            continue;
        }
        
        printf("Case #%d:",CT);
        for (int i=0;i<n;i++) printf(" %d",h[i]);printf("\n");
    }
}
            
        
        
    
    
