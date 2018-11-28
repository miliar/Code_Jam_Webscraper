// Coder: Ad
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<sstream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<deque>
#include<queue>
#include<numeric>
#define F(i,a,b) for(int i=a;i<b;++i)
#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)

#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;

int main(){
 int W;
 cin>>W;
 
 F(t,1,W+1)
 {string ini,s;
   cin>>s;
  string speedy=s;
  int ok=0;
  set<string>lesli;
  while(!ok){
   long long r=10000000;
  lesli.clear();
  sort(all(speedy));
 do{
  if(speedy[0]!='0'&&((speedy.size()>s.size())||(speedy.size()==s.size()&&speedy>s)))
   {lesli.insert(speedy);
   }
  }while(next_permutation(all(speedy)));
 
  if(lesli.size()==0)
  speedy="0"+speedy;
  else ok=1;
  }
  set<string>:: iterator ad;
  ad=lesli.begin();
  cout<<"Case #"<<t<<": "<<*ad<<endl;
 }
}
