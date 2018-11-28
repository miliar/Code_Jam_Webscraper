#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<cmath>

#define PB push_back
#define MP make_pair


using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 


int n;
double x[100+15], y[100+15], r[100+15];


double dis(double x1, double y1, double x2, double y2)
{
     return sqrt( (x1-x2)*(x1-x2) +  (y1-y2)*(y1-y2)  );
}

void solve()
{
     cin>>n;
     int i,j,k;
     
     for (i=0; i<n; i++)
         cin>>x[i]>>y[i]>>r[i];
     
     
     for (i=0; i<n; i++)
       for (j=i+1; j<n; j++)
         if (r[j]>r[i])
         {
             swap(r[i],r[j]);
             swap(x[i],x[j]);
             swap(y[i],y[j]);
         }
     
     
     if (n==1) { cout<<r[0]<<endl; return; }
     if (n==2) 
     { 
          cout<<max(r[0],r[1])<<endl;
          return;
     }
     
     if (n==3)
     {
         if ( 2.0*r[0] >= dis(x[1],y[1], x[2],y[2]) + r[1] + r[2] )
         {
             cout<<r[0]<<endl;
             return; 
         }
         
         
         double res = 1e10;
         for (i=0; i<n; i++)
           for (j=i+1; j<n; j++)
           {
              double z;
              for (k=0; k<n; k++)
                if (k!=i && k!=j) z = r[k];
                
              res <?= max(z , (dis(x[i],y[i],x[j],y[j]) + r[i] + r[j])/2.0  );
           }
         printf("%.6lf\n",res);
     }
     
     
     
}


#include<conio.h>
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num,z;
    cin>>num;
    for (z=1; z<=num; z++)
    {
       cout<<"Case #"<<z<<": "; 
       solve();
    }
     
    
    fclose(stdin);
    fclose(stdout);    
    getch();
    
    return 0;
}
