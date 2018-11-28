#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

#define pb push_back
#define MOD 1000000007
int main(){

  int N;
  cin>>N;
  for(int no=1;no<=N;no++){
    
    long long n,m,X,Y,Z;
    cin>>n>>m>>X>>Y>>Z;
    //cout<<n<<" "<<m<<" "<<X<<" "<<Y<<" "<<Z<<endl;
    vector<long long> limits;
    limits.clear();
    
    vector<int> generator;
    generator.clear();
    int temp;
    for(int i=0;i<m;i++){
      cin>>temp;
      //cout<<temp<<endl;
      generator.pb(temp);
    }
    //cout<<"limits"<<endl;
    for(int i=0;i<n;i++){
      temp=generator[i%m];
      limits.pb(temp);
      //cout<<temp<<endl;
      generator[i%m]=(((X%Z)*(generator[i%m]%Z))%Z+((Y%Z)*((i+1)%Z)))%Z;
    }

    vector<int> count(n,1);

    for(int i=0;i<n;i++){
      int sum=0;
      for(int j=i-1;j>=0;j--){
	if(limits[j]<limits[i]){
	  sum+=count[j];
	  sum%=MOD;
	}
      }
      count[i]+=sum;
      count[i]%=MOD;
    }
    int ans=0;
    for(int i=0;i<n;i++){
      ans+=count[i];
      ans%=MOD;
    }
    cout<<"Case #"<<no<<": "<<ans<<endl;
  }

}
