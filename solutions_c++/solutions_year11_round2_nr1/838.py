#include<iostream>
#include<string>

using namespace std;

int tot,n;
string s[200];
double wp[200],owp[200],oowp[200];
int main(){
      freopen("D:\\A-large.in","r",stdin);
      freopen("D:\\out.txt","w",stdout);
	cout.setf(ios::showpoint);
	cout.precision(9); 
	cout.setf(ios::fixed);

      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            memset(wp,0,sizeof(wp));
            memset(owp,0,sizeof(owp));
            memset(oowp,0,sizeof(oowp));
            cin>>n;
            for (int i=1;i<=n;i++) cin>>s[i];
            for (int i=1;i<=n;i++){
                  int p=0,q=0;
                  for (int j=1;j<=n;j++){
                        if (s[i][j-1]=='1'){
                              p++;
                              q++;
                        } else
                        if (s[i][j-1]=='0') q++;
                  }
                  wp[i]=double(p)/double(q);
            }
            for (int i=1;i<=n;i++){
                  double sum=0;
                  int pp=0;
                  for (int j=1;j<=n;j++) if (s[i][j-1]!='.'){
                        int p=0,q=0;
                        pp++;
                        for (int k=1;k<=n;k++) if (k!=i){
                              if (s[j][k-1]=='1'){
                                    p++;q++;
                              } else
                              if (s[j][k-1]=='0'){
                                    q++;
                              }
                        }
                  sum+=double(p)/double(q);
                  }
                  owp[i]=sum/double(pp);
            }
            for (int i=1;i<=n;i++){
                  double sum=0;
                  int p=0;
                  for (int j=1;j<=n;j++) if (s[i][j-1]!='.'){
                        p++;
                        sum+=owp[j];
                  }
                  oowp[i]=sum/double(p);
            }
            cout<<"Case #"<<ca<<":"<<endl;
            for (int i=1;i<=n;i++) cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
      }      
}                 
                  
                  
      
