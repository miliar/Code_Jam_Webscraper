#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); i++)
#define FOR(i,a,b) for (int i=(a); i<=(b); i++) 
#define ALL(c) (c).begin(),(c).end()
typedef long long ll;


int main(){

	ifstream in("A-large.in");
	ofstream out("output.out");

	ll N;
	in>>N;
 
	int S,Q;
	REP(i,N){
        
		in>>S;
		set <string> names;
		string name;
        getline(in,name);
		REP(j,S){
            getline(in,name);
            names.insert(name);
            
		}

        in>>Q;
        int count=0;
        getline(in,name);
        set <string> temp(names);
      
		REP(j,Q){
			getline(in,name);
            temp.erase(name);
            if(temp.empty()){
                count++;
                temp=names;
                temp.erase(name);
            }
           
            //cout<<name<<endl;
            //cout<<temp.size()<<endl;
		}
        //cout<<names.size()<<endl;
       
	  //  cout<<endl;
		out<<"Case #"<<i+1<<": "<<count<<endl;
        
	
	}
	
	//int a;
    //cin>>a;

	return 0;


}
