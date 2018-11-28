
//CODER: Adolfo Ccanto Ad...
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<stack>
#include<math.h>
#include<string>

#define F(i,a,b) for(int i=a;i<b;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define pii pair<int,int>

#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)


using namespace std;

int main(){
int ad,N;
cin>>ad;
long long K;
F(sub,1,ad+1){
cin>>N>>K;
long long periodo=1LL;
F(j,0,N)periodo*=2;

long long lesli=K+1;
if(lesli%periodo==0)cout<<"Case #"<<sub<<": "<<"ON"<<endl;
else cout<<"Case #"<<sub<<": "<<"OFF"<<endl;           
}
}
