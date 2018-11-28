#include<iostream> 
#include<vector>
#include<algorithm>
#include<math.h> 
using namespace std;
int techo(double n){
    int t;
    t=int(ceil(n));
    return t;

}
int main(){   
   freopen("B-large.in","r",stdin);
   freopen("b.out","w",stdout);
   int i,r,t,n,s,p,max;
   double g[100];
   int j=1;
   cin>>t;
   while(t-->0){
      cin>>n>>s>>p;
      r=0;
      for(i=0;i<n;i++){
         cin>>g[i];
      }
      sort(g,g+n);
      max=0;
      double comp,cm3;
      int c,num;
      for(i=0;i<n;i++){
         cm3=g[i]/3;
         num=int(g[i]);
         c=techo(cm3);
         if(num==0){if(c>=p)max++;continue;}
         if(num%3==0){
            if(c>=p)max++;
            else{if(s>0){c++;if(c>=p){max++;s--;}}}
            continue;               
         }
         if(num%3==1){if(c>=p)max++;continue;}
         if(num%3==2){
            if(c>=p)max++;
            else{if(s>0){c++;if(c>=p){max++;s--;}}}
            continue;
         }
         //cout<<num<<" "<<c<<endl;
      }
      cout<<"Case #"<<j<<": "<<max<<endl;
      j++;
   }
} 
