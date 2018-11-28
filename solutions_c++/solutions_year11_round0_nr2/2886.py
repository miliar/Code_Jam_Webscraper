#include<fstream>
using namespace std;
int main()
{
    int t,q,c,j,d,n=0,m=0,p,k,i,z=0;
    char a[3],b[2],g[10],r[10];
    
    ifstream fin("B-small-attempt4.in");
    ofstream fout("outputCSfinal1.txt");
    fin>>t;
    while(t--)
    {z++;
              q=-1;
              fin>>c;
            if(c!=0)
               for(i=0;i<3;i++)
               fin>>a[i];
                  fin>>d;
                   if(d!=0)  
                   for(i=0;i<2;i++)
                     fin>>b[i];
                    fin>>n;
                    for(i=0;i<n;i++)       
                    fin>>g[i];     
                  
                          for(i=0;i<n;i++)
                              {q++;
                                                r[q]=g[i];
                                                                                              
                                                    if(q>0)                          
                                                     if((r[q]==a[0]&&r[q-1]==a[1])||(r[q]==a[1]&&r[q-1]==a[0]))
                                                     {   
                                                        q--;
                                                       r[q]=a[2];
                                                        continue;
                                                         }
                                              for(j=0;j<=q;j++)
                                              {
                                                          
                                                              if(r[j]==b[0])
                                                              m=1;
                                                              if(r[j]==b[1])
                                                              p=1;
                                                              }
                                                              
                                                              if(m==1&&p==1)
                                                                q=-1;
                                                              
                                                              

                                                              
                                                              m=0;p=0;
                                                              
                                                              }
                                                              
                                                              
                                                              
                                                              if(q!=-1)
                                                              {
                                                                      fout<<"Case #"<<z<<": [";
                                                              for(i=0;i<q;i++)
                                                              fout<<r[i]<<", ";
                                                                   
                                                              fout<<r[q]<<"]"<<"\n";              
                                                              }
                                                              else
                                                              fout<<"Case #"<<z<<": []"<<"\n";         
                                                                            }
                                                                                            
             
                                                        fout<< flush;
                                                        fout.close();
    return 0;
    }
