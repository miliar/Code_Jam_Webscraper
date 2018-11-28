#include <iostream>
using namespace std;
long long tab[102][102];
int wyp[102];

long long mi(long long a, long long b){
return (a<b)?a:b;
}

int main(){
int i,j,k,n,m,min,P,Q;
cin>>n;
for(i=1;i<=n;i++){
 cin>>P;
 cin>>Q;
 for(j=0;j<Q;j++)
   for(k=0;k<Q;k++)
     tab[j][k]=0;
  for(j=1;j<=Q;j++)
    cin>>wyp[j];
  wyp[0]=0;
  wyp[Q+1]=P+1;
  for(k=1;k<=Q;k++){
    tab[0][k]=wyp[k]-1;
    tab[k][Q+1]=P-wyp[k];
  }
  for(k=1;k<=Q;k++){
    tab[k][k]=wyp[k+1]-wyp[k-1]-2;
    //cout<<"a "<<k<<" "<<k<<" "<<tab[k][k]<<endl;
  }
  for(k=1;k<Q;k++){
    tab[k][k+1]=mi(2*tab[k+1][k+1]+wyp[k]-wyp[k-1],2*tab[k][k]+wyp[k+2]-wyp[k+1]);
    //cout<<"b "<<k<<" "<<k+1<<" "<<tab[k][k+1]<<endl;
  }
  for(k=2;k<=Q-1;k++)
    for(j=1;j<=Q-k;j++){
      min=mi(wyp[j+k+1]-wyp[j-1]-2+tab[j+1][j+k],wyp[j+k+1]-wyp[j-1]-2+tab[j][j+k-1]);
      for(m=j+1;m<j+k;m++){
        min=mi(min,wyp[j+k+1]-wyp[j-1]-2+tab[j][m-1]+tab[m+1][j+k]);
      }
      tab[j][j+k]=min;
      //cout<<"c "<<j<<" "<<j+k<<" "<<tab[j][j+k]<<endl;
    }
  cout<<"Case #"<<i<<": "<<tab[1][Q]<<endl;
}
}