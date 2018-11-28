#include"iostream"
#include"cstdlib"
using namespace std;
__int64 rec[1001][3];
__int64 peo[1001];
__int64 peo2[2002];
__int64 T,R,k,N,nsum,kt;
__int64 cycle(__int64 t){
    kt=k;
   // rec[t][1]=kt/nsum;
   // kt%=nsum;
    for(int i=t;i<2*N;i++){
      // if(kt<peo2[i]){rec[t][0]=kt;rec[t][2]=i%N;return i%N;}
       if(kt<peo2[i] || i==t+N){rec[t][0]=kt;rec[t][2]=i%N;return i%N;}
       else kt-=peo2[i];
    }
    return -1;
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("Clarge.txt","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++){
       cin>>R>>k>>N;
       memset(rec,0xff,sizeof(rec));
       nsum=0;
       for(int j=0;j<N;j++){
          cin>>peo[j];
          nsum+=peo[j];
          peo2[j]=peo[j];
       }
       for(int j=N;j<N*2;j++){
          peo2[j]=peo2[j-N];
       }
       //rec
       __int64 now=0,now2=0;
      while(1){
         now=cycle(now);
         if(rec[now][0]!=-1)break;
      }
  //    cout<<"now="<<now<<endl;
      
      __int64 sum0=0,sum1=0,cy1=0,cy2=0;
      while(1){
         if(now2==now)break;
         sum0+=k-rec[now2][0];
         now2=rec[now2][2];
         cy1++;
      }
      while(1){
         cy2++;
         sum1+=k-rec[now2][0];
         now2=rec[now2][2];
         if(now2==now)break;
      }
  //    for(int j=0;j<N;j++)cout<<j<<":rec[0]="<<rec[j][0]<<",rec[1]="<<rec[j][1]<<",rec[2]="<<rec[j][2]<<endl;
  //    cout<<"cy1="<<cy1<<",cy2="<<cy2<<endl;
  //    cout<<"sum0="<<sum0<<",sum1="<<sum1<<endl;
      __int64 res=0;
      if(cy1>R){
         __int64 now3=0,tr=R;
         while(tr--){
            res+=k-rec[now3][0];
            now3=rec[now3][2];
         }
      }
      else{
          __int64 tr=R;
          tr-=cy1;
          res+=(sum0+tr/cy2*sum1);
          tr%=cy2;
          int now3=now;
          while(tr--){
            res+=k-rec[now3][0];
            now3=rec[now3][2];
         }
      }
      printf("Case #%d: %I64d\n",i,res);
    }
   // system("pause");
    return 0;
}

