#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<map>

#define rep(i,n) for(int i=0;i<n;++i)

using namespace std;

int main()
{
 long long N,M,Q=0;
    
    char junk[1000];
    fstream in("input3.in",ios::in);
    fstream out("output3.out",ios::out);

	in>>N;                     
                
    rep(n,N)
    {
    
            
            in>>M;
            
           
            
          char s[100][1000];
          char junk[1000];
          in.getline(junk,2000,'\n');        

            
            rep(i,M)in.getline((char *)s[i],2000,'\n');                   
            
    
    
            
            in>>Q;
         
            in.getline(junk,2000,'\n');
    
            
           
           
            char q[1000][1000];    

            rep(i,Q)in.getline((char *)q[i],2000,'\n');                              
            
            map<string,long long> m;
            long long flag[1000];

            long long j=0,count=0,ct=0;
            
            rep(i,M)
            {
             m[s[i]]=i;
             flag[i]=1;
            }

                                           
            while(j<Q)
            {
                      long long prev=flag[m[q[j]]];  
                      flag[m[q[j]]]=0;
                      
                      if(prev == 1 && flag[m[q[j]]]==0)
                      ct++;                     
                                            
                      if(ct==M)
                      {
                              ct=0;                            
                              count++;
                              rep(i,M)flag[i]=1;
                              j--;
                      }

                      j++;
            }
           out<<"Case #"<<n+1<<": "<<count<<endl;
                      
            

    }

    in.close();
    out.close();
  system("pause");
return 0;
}
