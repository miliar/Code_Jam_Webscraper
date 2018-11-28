#include<numeric>
#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

long long tab[1010];
int signs[1010];
int A[110];

int main(){
  ios::sync_with_stdio(false);
  int Q;
  cin >> Q;
  for(int q=1;q<=Q;q++){
    long long X,Y,Z;
    int m,n;
    cin >> n >> m >> X >> Y >> Z;
    for(int i=0;i<m;i++){
      cin >> A[i];
    }
    for(int i=0;i<n;i++){
      signs[i]=A[i%m];
      A[i%m]=(X* (long long)A[i%m] + Y*(long long)(i+1))%Z;
    }
    tab[n]=0;
    //    signs[n]=1000000000;
    for(int i=n-1;i>=0;i--){
      tab[i]=1;
      for(int j = i+1;j<n;j++){
	if(signs[i]<signs[j]){
	  tab[i]+=tab[j];
	  tab[i]%=1000000007;
	}
      }
    }
    long long sum = 0;
    for(int i=0;i<n;i++){sum+=tab[i];sum%=1000000007;}
    cout<<"Case #"<<q<<": "<<sum<<endl;
  }
}
