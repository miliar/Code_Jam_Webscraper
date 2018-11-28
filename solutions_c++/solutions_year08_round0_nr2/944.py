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

	ifstream in("B-large.in");
	ofstream out("output.out");

	ll N;
	in>>N;
 
    int turn;
	int NA,NB;
	REP(i,N){
        
		in>>turn;
        in>>NA;
        in>>NB;

	    multiset <pair <int,int> > fromA;
        multiset <pair <int,int> > fromB;
        
		REP(j,NA){
            int dep=0,arr=0;
            char ch;
            in>>ch;
            dep+=(ch-'0')*600;
            in>>ch;
            dep+=(ch-'0')*60;
            in>>ch;//:
            in>>ch;
            dep+=(ch-'0')*10;
            in>>ch;
            dep+=(ch-'0')*1;
            
           // in>>ch;// bosluk
            in>>ch;
            arr+=(ch-'0')*600;
            in>>ch;
            arr+=(ch-'0')*60;
            in>>ch;//:
            in>>ch;
            arr+=(ch-'0')*10;
            in>>ch;
            arr+=(ch-'0')*1;

            fromA.insert(make_pair(dep,arr+turn));
            //cout<<dep<<" "<<arr<<endl;
		}

        REP(j,NB){
            int dep=0,arr=0;
            char ch;
            in>>ch;
            dep+=(ch-'0')*600;
            in>>ch;
            dep+=(ch-'0')*60;
            in>>ch;//:
            in>>ch;
            dep+=(ch-'0')*10;
            in>>ch;
            dep+=(ch-'0')*1;
            
           // in>>ch;// bosluk
            in>>ch;
            arr+=(ch-'0')*600;
            in>>ch;
            arr+=(ch-'0')*60;
            in>>ch;//:
            in>>ch;
            arr+=(ch-'0')*10;
            in>>ch;
            arr+=(ch-'0')*1;

            fromB.insert(make_pair(dep,arr+turn));
            //cout<<dep<<" "<<arr<<endl;

		}

        int needA[2000]={0};
        int needB[2000]={0};

        
        int addA[2000]={0};
        int addB[2000]={0};

        for( multiset <pair <int,int> >::iterator it=fromA.begin();it!=fromA.end();it++){
            needA[it->first]++;
            addB[it->second]++;
        }

        for( multiset <pair <int,int> >::iterator it=fromB.begin();it!=fromB.end();it++){
            needB[it->first]++;
            addA[it->second]++;
        }

        int A=0,B=0,readyA=0,readyB=0;
        for(int j=0;j<1440;j++){
            readyA+=addA[j];
            if(readyA<needA[j]){
                A+=needA[j]-readyA;
                readyA=0;
            }else{
                readyA-=needA[j];
            }

            readyB+=addB[j];
            if(readyB<needB[j]){
                B+=needB[j]-readyB;
                readyB=0;
            }else{
                readyB-=needB[j];
            }

        }
        out<<"Case #"<<i+1<<": "<<A<<" "<<B<<endl;
	
	}
	
	//int a;
    //cin>>a;

	return 0;


}
