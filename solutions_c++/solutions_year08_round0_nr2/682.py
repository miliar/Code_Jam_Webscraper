#include<stdio.h>
#include<vector>
#include<algorithm>


using namespace std;

struct Hora{
  int hi;
  int mi;
  int hf;
  int mf;
  int sta;
  int usd;
       
};

bool operator<(const Hora &a, const Hora &b)
{
     if(a.hi==b.hi && a.mi==b.mi){ 
                   if(a.hf==b.hf) return a.mf<b.mf;
                   return a.hf<b.hf;
     }
     else if(a.hi==b.hi)
          return a.mi<b.mi;
     return a.hi<b.hi;
     
}

int main(){
    
    int n,z;
    scanf("%d", &n);
    for(z=0;z<n;z++){
                     vector<Hora> deps;
                     int t,na,nb; 
                     scanf("%d%d%d", &t,&na,&nb);
                     for(int i=0;i<na;i++){
                             int hi,mi,hf,mf; char t;
                             scanf("%d:%d %d:%d",&hi,&mi,&hf,&mf);
                             Hora tt={hi,mi,hf,mf,1,0};
                             deps.push_back(tt);
                     }
                     for(int i=0;i<nb;i++){
                             int hi,mi,hf,mf; char t;
                             scanf("%d:%d %d:%d",&hi,&mi,&hf,&mf);
                             Hora tt={hi,mi,hf,mf,2,0};
                             deps.push_back(tt);
                     }
                     sort(deps.begin(),deps.end());
                     
                     int ca=0,cb=0;
                     for(int i=0;i<deps.size();i++){
                            if(deps[i].usd==0){
                                  if(deps[i].sta==1) ca++; else cb++;
                                  deps[i].usd=1;                                                             
                                  int hact,mact,staact;
                                  hact=deps[i].hf+((t+deps[i].mf)/60);
                                  mact=(deps[i].mf+t)%60;
                                  staact=deps[i].sta;
  //                                printf("%d %d %d - %d %d\n", i, hact, mact, ca, cb);
                                  
                                  for(int j=i+1;j<deps.size();j++)
                                     if(deps[j].usd==0 && deps[j].sta!=staact && (deps[j].hi>hact || (deps[j].hi==hact && deps[j].mi>=mact)) ){
                                          
                                          deps[j].usd=1;
                                          //if(deps[j].sta==1) ca++; else cb++;                        
                                          hact=deps[j].hf+((t+deps[j].mf)/60);
                                          mact=(deps[j].mf+t)%60;
                                          staact=deps[j].sta;                                                      
//                                          printf("->%d %d %d\n", j, hact, mact);
                                     }
                                  
                                  
                                                     
                                               
                            }        
                             
                             
                     }
                     
                     printf("Case #%d: %d %d\n", z+1,ca,cb);
        }
    
    
    system("pause");
    return 0;
    
}
