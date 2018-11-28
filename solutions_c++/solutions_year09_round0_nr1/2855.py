//AlienLanguage.cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,n) for(LET(i,a); i!=n; i++)
#define REP(i,n) FOR(i,0,n)
#define pb(x) push_back(x)
#define sz size()
#define PRINT(x) { REP(_,x.sz) cout<<x[_]<<" "; cout<<endl;}

int main(){
  int L,D,N;
  cin >> L >> D >> N; string temp;
  vector<string> d;
  REP(i,D) { cin>>temp; d.pb(temp); }

  REP(testCase,N) { 
    string test; cin >> test;
    vector< vector<int> > input(L,vector<int>(26,0));
    int count = 0; 
    
    REP(i,test.sz) {	
	 
	 if(test[i]!='(' && test[i]!=')') input[count][test[i]-'a']=1;
	 else if(test[i]=='(') {

	   do{
		i++;
		if(test[i]!=')') input[count][test[i]-'a']=1;
	   }while(i<test.sz && test[i]!=')');
	 }
	 count++; 
    }
    
    
    int ans=0;
    
    REP(word,d.sz){ 
	 bool flag = true;
	 REP(l,d[word].sz) 
	   if(input[l][d[word][l]-'a'] != 1) { flag=false; break; }
	 if(flag)   ans++; 
    }
    cout <<"Case #" << testCase+1 << ": " << ans << endl;
  }
  return 0;
}

