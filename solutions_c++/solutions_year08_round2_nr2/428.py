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


bool isPrime(ll x){
    for(ll i=x-1;i>=sqrt((double)x);i--){
        if((x%i)==0)
            return false;
    }
    return true;
}

int main(){

	ifstream in("B-small-attempt2.in");
	ofstream out("output.out");

	ll N;
	in>>N;
 
	
	REP(i,N){
        ll A,B,P;
        in>>A;
        in>>B;
        in>>P;

        int table[3001];

        for(int j=0;j<3000;j++){
            table[j]=j;
        }
        
    
        for(int k=P;k<B;k++){
            if(isPrime(k)){
                //cout<<k<<endl;
                for(int j=A;j<=B;j++){
                    if((j%k)==0){
                        int base=j;
                        while(j<=B){
                            j+=k;
                            if(table[j]!=j){
                                int go=table[j];
                                for(int z=A;z<=B;z++){
                                    if(table[z]==go){
                                        table[z]=base;
                                    }
                                }
                            }else{
                                table[j]=base;
                            }
                        }
                    }
                
                }
               
            }
            // cout<<k<<endl;
        }

        int count=0;
        for(int j=A;j<=B;j++){
            if(table[j]==j){
                count++;
               // cout<<j<<endl;
            }
        }
        
		out<<"Case #"<<(i+1)<<": "<<count<<endl;
        //cout<<"Case #"<<(i+1)<<": "<<count<<endl;
	
	}
	
	//int a;
    //cin>>a;

	return 0;


}
