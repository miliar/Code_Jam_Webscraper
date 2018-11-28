#include <iostream>
#include <vector>
#define pb push_back
using namespace std;

struct times {
  int hour;
  int min;
  bool taken;
  times(){
    taken=false;
  }
};
bool cmp2(times a,times b) {
  if(a.hour<b.hour)
    return true;
  else if(a.hour>b.hour)
    return false;
  else 
    return a.min<=b.min;
}

bool cmp(times a,times b) {
  if(a.hour<b.hour)
    return true;
  else if(a.hour>b.hour)
    return false;
  else 
    return a.min<b.min;
}
int main() {

  
  int n;
  cin>>n;
  //cout<<"here"<<endl;
  for(int cas=1;cas<=n;cas++) {
    int add;
    cin>>add;
    int na,nb;
    cin>>na>>nb;
    
    vector<times> A_dep;
    vector<times> B_arr;
    vector<times> B_dep;
    vector<times> A_arr;
    //cout<<"here 2"<<endl;
    for(int i=0;i<na;i++){
      times t;
      char c;
      cin>>t.hour>>c>>t.min;
      //cout<<t.hour<<":"<<t.min<<" ";
      A_dep.pb(t);
      cin>>t.hour>>c>>t.min;
      //cout<<t.hour<<":"<<t.min<<endl;
      t.min+=add;
      t.hour+=(t.min/60);
      t.min%=60;
      B_arr.pb(t);
    }

    for(int i=0;i<nb;i++){
      times t;
      char c;
      cin>>t.hour>>c>>t.min;
      B_dep.pb(t);
      cin>>t.hour>>c>>t.min;
      t.min+=add;
      t.hour+=(t.min/60);
      t.min%=60;

      A_arr.pb(t);
    }
    //cout<<"here"<<endl;
    sort(A_dep.begin(),A_dep.end(),cmp);
    sort(B_dep.begin(),B_dep.end(),cmp);
    int countA=0,countB=0;    
    for(int i=0;i<na;i++) {
      int j;
      for(j=0;j<nb;j++) {
	if(A_arr[j].taken==false && cmp2(A_arr[j],A_dep[i])) {
	  A_arr[j].taken=true;
	  break;
	}


      }
      if(j==nb)
	countA++;
    }
    
    for(int i=0;i<nb;i++) {
      int j;
      for(j=0;j<na;j++) {
	if(B_arr[j].taken==false && cmp2(B_arr[j],B_dep[i])) {
	  B_arr[j].taken=true;
	  break;
	}
	
      }
      if(j==na)
	  countB++;
    }
    cout<<"Case #"<<cas<<": "<<countA<<" "<<countB<<endl;
    /*    for(int i=0;i<na;i++)
      cout<<A_dep[i].hour<<":"<<A_dep[i].min<<" "<<B_arr[i].hour<<":"<<B_arr[i].min<<endl<<endl;
    for(int i=0;i<nb;i++)
      cout<<B_dep[i].hour<<":"<<B_dep[i].min<<" "<<A_arr[i].hour<<":"<<A_arr[i].min<<endl<<endl;
    */
  }

  return 0;
}
