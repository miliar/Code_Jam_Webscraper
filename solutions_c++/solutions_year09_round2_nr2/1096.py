#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<math.h>
#include<queue>
using namespace std;

string buff,t2;
char solWorst[30];
int digits[30];
int cnt[10] , cntc[10];
int sol[30];

int main(){
   int T,t,d;
   freopen("Ulaz.txt","r",stdin);
  freopen("Izlaz.txt","w",stdout);
   scanf("%d",&T);
   for( int t = 1 ; t<=T; t++){
      memset(sol,0,sizeof(sol));
      memset(cnt,0,sizeof(cnt));
      memset(cntc,0,sizeof(cntc));
      memset(digits,0,sizeof(digits));
      memset(solWorst,0,sizeof(solWorst));
      cin>>buff;
      t2 = buff;
      for(int i=0;i<buff.size();i++)cnt[ buff[i]-'0' ]++ , digits[i] = buff[i]-'0';
      sort(buff.begin(),buff.end() );
      solWorst[0] = buff[0];
      solWorst[1] = '0';
      int di;
      for(int i=0;i<buff.size();i++){
         if( buff[i]!='0' ){ di = i;break;}
      }
      d=2;
      solWorst[0] = buff[di];
      solWorst[1] = '0';
      for(int i=0;i<buff.size();i++){
         if( i==di )continue;
         solWorst[d] = buff[i];d++;
      }                
      vector<string>V;
      string num;
      
      bool ok = false;
      bool solExist = false;
      for(int i=buff.size()-1; i>=0;i--){
           num = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz";
         for( int j=digits[i]+1;j<10;j++){
            for( int k=0;k<10;k++) cntc[k] = cnt[k];
            cntc[j]--;sol[i] = j;
            num[i] = '0'+j;
            if( cntc[j]<0 )continue;
            bool getG = false;
            solExist = true;
            for( int l=0;l<buff.size() && solExist;l++){
               if( l==i ){getG=true;continue;}
               
               int m;
               if( getG==false)m=digits[l];
               else m = 0;
               for( ;m<10;m++){
                  if( cntc[m]==0 )continue;
                  cntc[m]--;
                  if( m>digits[l] )getG = true;
                  num[l] = '0'+m;
                  sol[l] = m;
                  break;
               }
               if( m==10 )solExist = false;
            }
            if( solExist ){
               V.push_back(num);
               ok  = true;
            }
         }
      }
      if( ok ){
         printf("Case #%d: ",t);
         sort(V.begin(),V.end());
         for(int i=0;i<buff.size();i++)
            cout<<V[0][i];cout<<endl;
      }else{
         printf("Case #%d: ",t);
         printf("%s\n",solWorst); 
      }
        
      
   }
   return 0;
}
