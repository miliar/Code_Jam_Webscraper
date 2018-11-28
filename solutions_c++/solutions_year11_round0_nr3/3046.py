#include<fstream>
using namespace std;
int main()
{
    long long t,n,z,i,j,k,s,q,w,g,max,ar[1000],count=0,flag;
    ifstream fin("C-large.in");
    ofstream fout("outputshravsluvme.txt"); 
    fin>>t;
    while(t--)
    { max=0;
    count++;
              fin>>n;
              for(i=0;i<n;i++)
              fin>>ar[i];
              for(z=0;z<n-1;z++)
              {
                        //  cout<<"1"<<endl;    
              for(i=0;i<n-1;i++)
              {   //cout<<endl<<"i   "<<i<<endl;
                  s=q=w=g=0;
              //cout<<endl<<"j= ";
                                for(j=z;j<=i;j++)
                                { flag=1;
                                                 //cout<<j;
                                                 q=q^ar[j];
                                                 s=s+ar[j];
                                                 }
                                                 //cout<<endl<<"k= ";
                                                 if(flag==1)
                                                 for(k=i+1;k!=z;k++)
                                                 {//cout<<k;
                                                                   w=w^ar[k];
                                                                   g=g+ar[k];
                                                                   if(k==(n-1))
                                                                    k=-1;
                                                                   }
                                                                   flag=0;
                                                        if(q==w)
                                                       {
                                                         if((g>=s)&&(g>=max))
                                                         max=g;
                                                         if((s>=g)&&(s>=max))
                                                         max=s;
                                                         }
                                                        
                                                         }}
                                                         if(max==0)
                                                         fout<<"Case #"<<count<<": "<<"NO"<<endl;
                                                         else
                                                         fout<<"Case #"<<count<<": "<<max<<endl;           
                                                         }
                                                         return 0;
                                                         fout<< flush;
                                                        fout.close();
                                                         }
