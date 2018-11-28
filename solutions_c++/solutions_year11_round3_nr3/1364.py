#include <iostream>
#include <set>
using namespace std;
typedef long long int lint;
int t,n;
lint l,h;
set<lint> f;

void tcalc(){
  for(set<lint>::iterator i=f.begin();i!=f.end();i++){
    if(*i<l)continue;
    for(set<lint>::iterator j=(++i)--;j!=f.end();){
      if(*j%*i==0){
        
        f.erase(j++);
      }else{
        j++;
      }
    }
  }
  for(set<lint>::iterator i=f.begin();i!=f.end();i++){
    cout<<*i<<" ";
  }
}
void calc(){
  int d;
  bool isNG=false;
  for(d=l;d<=h;d++){
    isNG=false;
    set<lint>::iterator i;
    for(i=f.begin();i!=f.end()&&*i<=d;i++){
      if(d%*i){isNG=true;break;}
    }
    if(isNG){continue;}
    for(;i!=f.end();i++){
      if(*i%d){isNG=true;break;}
    }
    if(!isNG){cout<<d<<endl;return;}
  }
  cout<<"NO"<<endl;
}

int main(){
  cin>>t;
  lint temp;
  for(int tcase=1;tcase<=t;tcase++){
    cin>>n>>l>>h;
    f.clear();
    for(int i=0;i<n;i++){
      cin>>temp;
      f.insert(temp);
    }
    
    cout<<"Case #"<<tcase<<": ";
    calc();
  }
}