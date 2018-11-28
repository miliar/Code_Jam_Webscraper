#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char M[102][102];
double WPX[102],WPY[102],OWP[102],OOWP[102],WP[102];

int main(){
   int t,n;
   cin>>t;
   for(int k=0;k<t;++k){
       cin>>n;
       //cout<<n<<endl;
      for(int i=0;i<n;++i){
         for(int j=0;j<n;++j){
          cin>>M[i][j];
         }
       }
      //wp
      for(int i=0;i<n;++i){
         int ct=0,win=0;
            for(int j=0;j<n;++j){
               if(M[i][j]!='.')ct++;
               if(M[i][j]=='1')win++;
         }
         WPX[i]=win;
         WPY[i]=ct;
         WP[i]=(win*1.0)/ct;
        // cout<<"wp: "<<WPX[i]/WPY[i]<<endl;
      }
      //owp
      
      for(int j=0;j<n;++j){
         double acum=0.0;
         int ct=0;
         for(int i=0;i<n;++i){
            if(M[i][j]=='.')continue;
            ct++;
            int xu=M[i][j]-'0';
            double x=(WPX[i]-xu)/(WPY[i]-1);
            acum+=x;
         }
         OWP[j]=acum/ct;
        // cout<<"owp: "<<OWP[j]<<endl;
      }
      
      for(int j=0;j<n;++j){
         int ct=0;
         double acum=0.0;
         for(int i=0;i<n;++i){
            if(M[i][j]!='.'){
               ct++;
               acum+=OWP[i];
            }
         }
         OOWP[j]=acum/ct;
        // cout<<"oowp: "<<OOWP[j]<<endl;
      }
      
      printf("Case #%d:\n",k+1);
      for(int i=0;i<n;++i){
         double sol=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
         cout<<sol<<endl;
      }
      
      
 
   }
}
















