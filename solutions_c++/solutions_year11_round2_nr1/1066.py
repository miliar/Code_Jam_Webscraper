#include <iostream>
//#include <float.h>
#include <string>

using namespace std;

int main()
{
   int t;
   cin>>t;
   for(int it=0;it<t;it++){
      string result[103];
      float wp[103]={0};
      float owp[103]={0};
      float oowp[103]={0};
      float win[103]={0};
      float total[103]={0};
      int n;
      cin>>n;
      for(int i=0;i<n;i++)
         cin>>result[i];
      for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            if(result[i][j]!='.')
               total[i]++;
            if(result[i][j]=='1')
               win[i]++;
         }
      }
      
      for(int i=0;i<n;i++)
         wp[i]=win[i]/total[i];
      
      for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            if(result[i][j]=='.')
               continue;
            if(result[i][j]=='1'){
               owp[i]+=win[j]/(total[j]-1);
            }else{
               owp[i]+=(win[j]-1)/(total[j]-1);
            }
         }
         owp[i]/=total[i];
      }
      
      for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            if(result[i][j]=='.')
               continue;
            oowp[i]+=owp[j];
         }
         oowp[i]/=total[i];
      }
      
      cout<<"Case #"<<(it+1)<<":"<<endl;
      for(int i=0;i<n;i++){
         cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
         //cout<<win[i]<<" "<<total[i]<<" "<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" "<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
      }
      
   }
   return 0;
}


