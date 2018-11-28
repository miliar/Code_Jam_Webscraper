#include<iostream>
#include<fstream>
#include<string> 
#include<vector>
using namespace std;
int main()
{
    ofstream of("a.out");
    int l,d,n,i,p,m,k,j,count;
    cin>>l>>d>>n;
    vector<string> a(d);
    vector<int> v(d,0);
    for(i=0;i<d;i++)
    cin>>a[i];
    vector<string> b(n);
    for(i=0;i<n;i++)
    cin>>b[i];
    for(i=0;i<n;i++)
    {
                    count=0;
                    for(j=0,m=0;m<l;m++)
                    {
                                        if(b[i][j]=='(')
                                               {
                                               j++;
                                               for(k=0;k<d;k++)
                                               {
                                                               if(v[k]==m)
                                                               {
                                                           for(p=j;b[i][p]!=')';p++)
                                                           {
                                                           if(a[k][m]==b[i][p])
                                                           {
                                                                     v[k]++;
                                                                     break;
                                                                     }
                                                                     }
                                                                     }
                                                                     }
                                                                     for(;b[i][p]!=')';p++);
                                                                     j=p+1;
                                                                     }
                                             else                                                                                                       
                                                {
                                                    for(k=0;k<d;k++)
                                                          if(v[k]==m && a[k][m]==b[i][j])
                                                                  v[k]++;
                                                                   j++;
                                                                               }
                                                                               }
for(k=0;k<d;k++)    
{
if(v[k]==l)
count++;
v[k]=0;
}
of<<"Case #"<<(i+1)<<": "<<count<<endl;                                                                           
} 
}
