#include <vector>
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
#include <vector>
#define FORN(i,n) FOR(i,0,(n))
#define FOR(i,a,n) for(int i=(a);i<(n);i++)
#define sz size()
#define PB push_back
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define PRESENT(container, element) (container.find(element) != container.end())
#define ALL(x) x.begin(), x.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define DIST(x1,y1,x2,y2) sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )


using namespace std;
typedef unsigned long long ull;


string base="QWERASDF"; 


void print (vector<char> S){
	cout<<"[";
	
	if (!S.empty())
		cout<<S[0];
	
	FOR(i,1,S.sz){
		cout<<", "<<S[i];
	}
	
	cout<<"]"<<endl;
}


void print1 (vector<string> S){
	cout<<"[";
	
	if (!S.empty())
		cout<<S[0];
	
	FOR(i,1,S.sz){
		cout<<", "<<S[i];
	}
	
	cout<<"]"<<endl;
}

int main(){
	int t;

	cin>>t;
	FORN(casos,t){

		int c,d;
		cin>>c;
		vector<string>comb;
		FORN(j,c){
			string st;
			cin>>st;
			comb.PB(st);
		}
	
		cin>>d;
		vector<string>opo;
		FORN(j,d){
			string st;
			cin>>st;
			opo.PB(st);
		}
		
		
	/*	cout<<"comb"<<endl;
		print1(comb);
		
		cout<<"opo"<<endl;
		print1(opo);
	*/	
		int N;
		cin>>N;
		string call,res="";
		cin>>call;
		
		
		//DO
		vector<char>elements;
		
		
		FORN(i,N){
			char actual=call[i];
	//		cout<<"Viendo " <<actual<<endl;
			if (elements.sz==0){
				elements.PB(actual);
				continue;
			}
			
			bool combined=false;
			FORN(i1,comb.sz){
				if ((comb[i1][0]==actual && elements[(elements.sz)-1]==comb[i1][1]) || 
				   (comb[i1][1]==actual && elements[(elements.sz)-1]==comb[i1][0])){
					elements[(elements.sz)-1]=comb[i1][2];
					combined=true;
		//			cout<<"Combinado!"<<endl;
					break;
				   }
			}
			
			bool oposite=false;
			
			if (!combined)
			FORN(i1,opo.sz){
				if (opo[i1][0]==actual){
					FORN(qq,elements.sz){
						if (elements[qq]==opo[i1][1]){
							elements.clear();
							oposite=true;
							break;
						//	cout<<"oposite!"<<endl;
						}
					}
				}
				if (opo[i1][1]==actual){
					FORN(qq,elements.sz){
						if (elements[qq]==opo[i1][0]){
							elements.clear();
						oposite=true;
// 						cout<<"oposite!"<<endl;
						break;}
					}
				}
			}
			
			
			if (!combined && !oposite)
				elements.PB(actual);
			
// 			print(elements);
			
		}
		
		
			
		cout<<"Case #"<<(casos+1)<<": ";
		print(elements);
	}
	

  return 0;
}
