using namespace std;

/*
author : ravi shukla 
*/


# include<iostream>
# include<cstdio>
# include<cstring>
# include<cstdlib>
# include<cmath>
# include<cassert>
# include<cctype>
# include<algorithm>

# include<vector>
# include<limits>
# include<list>
# include<stack>
# include<queue>
# include<set>
# include<map>
# include<bitset>
# include<sstream>
# include<deque>
# include<fstream>


int main(){
  int cnum=0,tcases,n,s,p,count,marks,res,imx,imn;
  freopen("q2linp.in","r+",stdin);
  freopen("q2lout.txt","w+",stdout);
  cin>>tcases;
  int f1=0,f2;
  while(tcases--){
    cnum++;
    cin>>n>>s>>p;
    count=0;
    for(int i=0;i<n;i++){
      cin>>marks;
      f1=0;f2=0;
      for(int j=0;j<=10;j++){
        for(int k=0;k<=10;k++){
          for(int l=0;l<=10;l++){
            if(j+k+l==marks){
              imx=max(j,max(k,l));
              if(imx>=p){
              imn=min(j,min(k,l));
              res=imx-imn;
              if(res<=1)
                f1=1;
              else if(res==2)
                f2=1;
              }}
            }
          }
        }
        if(f1==1){
          count++;
        }else if(s>0 && f2==1){
          s--;
          count++;
        }
        
      }
      cout<<"Case #"<<cnum<<": "<<count<<endl;
    }
    return 0;
    
  }
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
