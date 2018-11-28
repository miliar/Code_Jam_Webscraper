#include<iostream.h>
#include<fstream.h>

struct node
{      
       int g;
       node *ptr;
}*top,*group;

int main()
{   
    int t,i,j,l;
    long R,k,N,z,f;
    long *sum;
    ifstream fin;
    fin.open("inputfile.txt");
    fin>>t;
    sum=new long[t];
    for(i=0;i<t;i++)
    {               
                    sum[i]=0;
                    fin>>R;
                    fin>>k;
                    fin>>N;
                    top=new node;
                    fin>>top->g;
                    group=top;
                    for(j=1;j<N;j++)
                    {               
                                    group->ptr=new node;
                                    group=group->ptr;
                                    fin>>group->g;
                    }
                    group->ptr=top;
                    group=top;
                    
                    for(l=0;l<R;l++)
                    {               
                                    z=0;
                                    f=1;
                                    while((z+group->g<=k)&&(f<=N))
                                    {
                                                        z+=group->g;
                                                        sum[i]+=group->g;
                                                        group=group->ptr;
                                                        f++;
                                    }
                    }
                    for(l=0;l<N;l++)
                    {               
                                    top=group;
                                    delete group;
                                    group=top->ptr;
                    }
                                    
    }  
    fin.close(); 
    ofstream fout("outfile.txt");      
    for(i=0;i<t;i++)
    fout<<"Case #"<<i+1<<": "<<sum[i]<<"\n";
    fout.close();
    delete []sum;
    return 0;
}                       
                                    
                                       
                                    
                    
                                                            
                                                  
                                    
                                    
                    
                                                     
                                    
                    
