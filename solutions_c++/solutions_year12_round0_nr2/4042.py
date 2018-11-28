#include<iostream>
using namespace std;
int main()
{
    
    //freopen("idl.txt","r",stdin);
    //freopen("odl.txt","w",stdout);
    int i,j,k,n,s,p,m,c,t;
    while(cin>>t)
    {
                 int a[9];
                 m=1;
                 while(m<=t)
                 {
                            cin>>n>>s>>p;
                            //cout<<n<<" "<<s<<" "<<p<<" ";
                            int b[n];
                            c=0;
                            for(i=0;i<n;++i)
                            cin>>b[i];
                            //for(i=0;i<n;++i)
                            //cout<<b[i]<<" ";
                            //cout<<endl;
                            if(p!=1)
                            {
                                            a[0]=3*p-4;
                                            a[1]=3*p-3;
                                            a[2]=3*p-2;
                                            a[3]=3*p-1;
                                            a[4]=3*p;
                                            a[5]=3*p+1;
                                            a[6]=3*p+2;
                                            a[7]=3*p+3;
                                            a[8]=3*p+4;
                            }               
                            else
                            {
                                         a[0]=-1;
                                         a[1]=-1;
                                         a[2]=3*p-2;
                                         a[3]=3*p-1;
                                         a[4]=3*p;
                                         a[5]=3*p+1;
                                         a[6]=3*p+2;
                                         a[7]=3*p+3;
                                         a[8]=3*p+4;
                            }                        
                            cout<<"Case #"<<m<<": ";
                            ++m;
                            for(j=0;j<n;++j)
                            {
                                            if(b[j]>a[8])
                                            ++c;
                                            else if(b[j]<a[0])
                                            continue;
                                            else
                                            {
                                                for(k=8;k>=0;--k)
                                                {
                                                                 if(b[j]==a[k])
                                                                 {
                                                                               if((k<2)&&(s>0))
                                                                               {
                                                                                               --s;
                                                                                               ++c;
                                                                               }
                                                                               if(k>1)
                                                                               ++c;
                                                                 }
                                                }
                                            }
                            }
                            cout<<c<<endl;
                 }
    }
    return 0;
}
                            
                                                                                                                           
