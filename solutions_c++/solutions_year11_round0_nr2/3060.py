#include<iostream>
using namespace std;

#define N 100

int main()
{
    char string[N];
    int t,c,d,n;
    char base[3];
    char opp1,opp2;
    char opp;
    bool opp_found=false;
    bool combine=false;
    int count=0;
    char found;
    cin>>t;
    int len=0;
    int q=1;
    
    while(t-->=1)
    {
                 len=0;
                 opp_found=false;
                 cin>>c;
                 if(c==1)
                     cin>>base;
                 cin>>d;
                 if(d==1)
                      cin>>opp1>>opp2;
                 
                 cin>>n;
                 int i=0;
                 count=0;
                 while(i<n)
                 {
                           combine=false;
                           
                           cin>>string[len];
                            // For combining 
                           if(c==1)
                           {
                                   if(len>=1)
                                   {
                                             if((string[len]==base[0] && string[len-1]==base[1]) || (string[len]==base[1] && string[len-1]==base[0]))
                                             {
                                                                   if(string[len-1]==found )
                                                                    {
                                                                                            if(count==1)
                                                                                            {
                                                                                            opp_found=false;
                                                                                            count=0;
                                                                                            }
                                                                                            else 
                                                                                            count--;
                                                                    }
                                                                    len--;
                                                                    string[len]=base[2];
                                                                    combine=true;
                                                                    
                                                                    
                                             }
                                   }
                           }
                           // For Opposite base elements
                           if(d==1 )
                           {
                                   if(opp_found==true && string[len]==opp)
                                   {
                                                      len=-1;
                                                      opp_found=false;
                                   }
                                   else if(string[len]==opp1 || string[len]==opp2)
                                   {
                                                      opp_found=true;
                                                      found=string[len];
                                                      count++;
                                                      opp=(string[len]==opp1?opp2:opp1);
                                   }
                           }
                                           
                           len++;
                           i++;
                 }
                 cout<<"Case #"<<q<<": [";
                 for(int j=0;j<len;j++)
                 {
                           if(j!=len-1)
                           cout<<string[j]<<", ";
                           else
                           cout<<string[j];
                 }
                 
                 cout<<"]"<<endl;
                 q++;
    }
    
   
    return 0;
}           
                          
                           
                           
                                   
                           
                           
                           
                 
                 
                 
                 
