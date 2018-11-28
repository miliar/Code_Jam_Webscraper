#include<fstream>
using namespace std;
int main()
{
    long long sp[1000],so[1010],ar[1000],v=0,l,t,n,c,i,j,q,k,sum,lum,flag,temp,a,ti,r;
    ifstream fin("B-small-attempt2.in");
    ofstream fout("output2shravs.txt");
    fin>>r;
    while(r--)
    {
              v++;
              fin>>l>>t>>n>>c;
              for(i=0;i<c;i++)
              fin>>ar[i];
             
              k=0,sum=0,flag=0,lum=0;
              
              for(i=0;i<n;i++)
              {
                              sp[i]=ar[k];
                              so[i]=ar[k];
                              k++;
                              if(k==c)
                              k=0;
                              
                              
                              }
                              
                              
                              
                              
                              
              for(i=0;i<n;i++)
              {
                              sum=sum+sp[i];
                              
                              if((sum>=t/2)&&flag!=1)
                              {
                                                 flag=1;
                                        
                                 so[n]=sum-t/2;
                                 
                                 for(q=i+1;q<=n;q++)
                              {
                                              for(j=q+1;j<=n;j++)
                                              {
                                                                if(so[q]<so[j])
                                                                {
                                                                               temp=so[q];
                                                                               so[q]=so[j];
                                                                               so[j]=temp;
                                                                               }}}
                                                                               
                                                                               for(a=i+1;a<(l+i+1);a++)
                                                                               {
                                                                               lum=lum+so[a];
                                                                               
                                                                               }}
                                                                               }
                                                                               ti=2*sum-lum;
                                                                               
                                                                               fout<<"Case #"<<v<<": "<<ti<<endl;
                                                                               }
                                                                               return 0;
                                                                               }
                                                                               
                                                                                               
                                                                               
                                                              
                              
                              
                              
                              
                              
                              
                              
                              
