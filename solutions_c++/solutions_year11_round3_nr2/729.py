#include<iostream>
#define lolo long long;

using namespace std;

long long tot,l,n,c,t,ans,o[2000],s[2000];

void work0(){
      ans=s[n]*2;
}

long long go(long long i,long long j){
      return (s[j]-s[i])*2;
}
void work1(){
      ans=2000000*2000000;
      for (long long p=0;p<=n;p++){
            long long time=0,pos=0;
            if (go(pos,p)>=t){
                  time+=s[p]+s[p+1];
            } else
            if (go(pos,p+1)>=t){
                  time+=s[p+1]+t/2;
            } else{
                  time+=s[p+1]*2;
            }
            pos=p+1;
            time+=go(pos,n+1);
            if (time<ans) ans=time;
      }
}

void work2(){
      ans=2000000*2000000;
      for (long long p=0;p<=n;p++)
      for (long long q=p+1;q<=n;q++){
            long long time=0,pos=0;
            if (go(pos,p)>=t){
                  time+=s[p]+s[p+1];
            } else
            if (go(pos,p+1)>=t){
                  time+=s[p+1]+t/2;
            } else{
                  time+=s[p+1]*2;
            }
            pos=p+1;
            time+=go(pos,q);
            if (time>=t){
                  time+=s[q+1]-s[q];
            } else
            if (time+go(q,q+1)>=t){
                  time=s[q+1]+t/2;
            } else{
                  time+=go(q,q+1);
            }
            pos=q+1;
            time+=go(pos,n+1);
            if (time<ans) ans=time;
      }
}
          
int main(){
      freopen("D:\\B-small-attempt0.in","r",stdin);
      freopen("D:\\out.txt","w",stdout);
      cin>>tot;
      for (long long ca=1;ca<=tot;ca++){
            memset(s,0,sizeof(s));
            cin>>l>>t>>n>>c;
            for (long long i=1;i<=c;i++) cin>>o[i];
            for (long long i=1;i<=n;i++) s[i]=s[i-1]+o[(i-1)%c+1];
            s[n+1]=s[n];
            if (l==0) work0(); else
            if (l==1) work1(); else 
            if (l==2) work2();
            cout<<"Case #"<<ca<<": "<<ans<<endl;
      }
      //system("pause");
}
            
      
