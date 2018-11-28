#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <utility>
#include <map>
#include <climits>
#include <algorithm>

#define vi vector<int>
#define vii vi::iterator
#define pii pair<int,int>
#define vpi vector< pii >
#define vpii vpi::iterator

#define FOR(i,n) for (ll i=0;i<n;i++)
#define FORIT(it,t,n) for (t::iterator it=n.begin();it!=n.end();it++)

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)<0?-(a):(a))
#define DIFF(a,b) MAX((a)-(b),(b)-(a))
#define BETWEEN(x,a,b) ((x)>=(a) && (x)<=(b))

#define DEBUG(a) cout << #a << ": " << a << "\n"

typedef long long ll;

using namespace std;

int main(int argc,char **argv)
{   
    if (argc!=3)
    {
      printf("usage: program-name inputfile outputfile\n");
      exit(1);
    }
    
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T,Case;
    
    fin >> T;
    
    for (Case=1;Case<=T;Case++)
    {
		ll l,t,n,c;
		fin >> l >> t >> n >> c;
		vector<ll> a(c);
		ll sum=0;
		FOR(i,c) {
			fin >> a[i];
			sum+=a[i];
		}
		ll waittill=t/(2*sum)*c, sum2=0;
		ll time=0;
		
		ll onetimeboost=0;
		if (2*sum*(waittill/c)<t){
			FOR(i,c){
				sum2+=a[i];
				if (2*sum*(waittill/c)+2*sum2>=t) {
					onetimeboost=(2*sum*(waittill/c)+2*sum2)-t;
					time=t;
					waittill+=i+1;
					break;
				}
			}
		}
//		DEBUG(time);
//		DEBUG(waittill);
		map<ll, ll> number;
		FORIT(it,vector<ll>,a){
			number[*it]+=((n+c-1)/c-(waittill+c-1)/c);
		}
		for (ll i=n;i%c!=0;i++) number[a[i%c]]--;
		for (ll i=waittill;i%c!=0;i++) number[a[i%c]]++;
		number[onetimeboost/2]++;
		
		for (map<ll,ll>::reverse_iterator it=number.rbegin();it!=number.rend();it++){
			if (l>0){
				if (l>(*it).second){
					l-=(*it).second;
					time+=(*it).first*(*it).second;
				}else{
					time+=(*it).first*l+2*(*it).first*((*it).second-l);
					l=0;
				}
			}else{
				time+=2*(*it).first*(*it).second;
			}
//			DEBUG(time);
		}
		
        fout << "Case #" << Case << ": ";
		
		fout << time;
		
		fout << "\n";
    }
	fin.close();
    fout.close();
}
