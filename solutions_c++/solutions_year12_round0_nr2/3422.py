#include<iostream>
#include<fstream>
using namespace std;
int comp(const void *a, const void *b)
{
     return (*(int*)b - *(int*)a);
}
int main()
{
    ifstream fil;
    ofstream dd;
    int t,a[101],p,n,s,i,j,count,x;
    fil.open("E:\\google\\q2\\B-large.in");
    dd.open("E:\\google\\q2\\abcl.out");
    fil>>t;
    
    for (i=0;i<t;i++)
      { count=0;
                     fil>>n>>s>>p;
                     for (j=0;j<n;j++)
                         fil>>a[j];
                     
                     qsort(a,n,sizeof(a[0]),comp);
                     
                     for(j=0;j<n;j++)
                       {   x=a[j]/3;  
                               if( a[j]%3==2)
                                   {
                                         if ((x+1)<=10 && (x+1) >=0 && (x+1)>=p)
                                            count++;
                                         else if ((x+2)<=10 && (x) >=0 && (x+2)>=p && s>0)       
                                            {  count++;
                                               s--;
                                            }
                                            else
                                                    break;
                                            
                                   }
                                else if (a[j]%3==0)
                                    {
                                              if ((x)<=10 && (x) >=0 && (x)>=p)
                                            count++;
                                         else if ((x+1)<=10 && (x-1) >=0 && (x+1)>=p && s>0)       
                                            {  count++;
                                               s--;
                                            }
                                            else
                                                    break;
                                    }
                                else
                                    { 
                                       if ((x+1)<=10 && (x) >=0 && (x+1)>=p)
                                            count++;
                                       else
                                        break;     
                                    } 
                       }         
        dd<<"Case #"<<i+1<<": "<<count<<endl;  
    }                                    
    
    fil.close();
    dd.close();
    return 0;
    
}
    
