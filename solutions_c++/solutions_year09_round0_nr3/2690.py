#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n ; i++)
#define FORK(i,a,b,k) for (int _n(b), i(a); i < _n ; i+=k)
#define FORD(i,a,b) for ( int i=(a),_b=(b); i>=_b; --i)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end(); ++it)
#define REP(i,n) FOR(i,0,n)
#define SZ(c) (c).size()
#define vs vector<string>
#define vi vector<int>
typedef pair<int, int> PII;

//bool comp (string i,string j) { return (i.compare(j) <0); }

int main(void){
	int N,L;
	int result=0;
	string a= "welcome to code jam";
	L = SZ(a);
	string s;	
	ifstream cin("input.txt");
	cin >>N;
	ofstream cout("output.txt");
	getline(cin,s);
	REP(i,N){
		result=0;
		getline(cin,s);
		size_t f ; 
		f = s.find("w");
		//s = s.substr(f);
		f = s.find_last_of("m");
		//s = s.substr(0,f+1);
		
		f = s.find_first_not_of("acdeljmotw ");
		while (f!=string::npos)
		{
			s.erase(f,1);
			f=s.find_first_not_of("acdeljmotw ");
		}
		if (SZ(s) >= L){
			int C[20][501];
			REP (i1,L){
				C[i1][0] = 0;
			}
			REP (i1, SZ(s)){
				C[0][i1] = 0;
			}

			FOR ( i1,1, L){
				FOR ( i2, 1, SZ(s)){
					if (a[i1] == s[i2])
						C[i1][i2] = C[i1-1][i2-1] +1;
					else
						C[i1][i2] = max(C[i1][i2-1], C[i1-1][i2]);
					
				}		
			}
			if ( C[L-1][SZ(s)-1] == L-1) {
				vector<PII> aa;
				vector<PII> bb;
				set<vector<PII>> ab,ac;
				PII tp;
				int kk = L-1;
				FORD ( i1, L-1, 0 ){
					FORD ( i2, SZ(s) -1 , 0){
						if( C[i1][i2] == kk && s[i2] == a[kk]){
							tp = make_pair( i1,i2);
							aa.push_back( tp);
							ab.insert(aa);
							aa.clear();
						}
					}
				}
				kk--;

				while(kk>=0){
					set<vector<PII>>::iterator it;
					for (it=ab.begin(); it!=ab.end(); it++)
					{
						vector<PII> aa = *it;
						FORD( i1, aa[SZ(aa)-1].first, 0){
							FORD( i2, aa[SZ(aa)-1].second, 0){
								if( C[i1][i2] == kk && s[i2] == a[kk] && kk==i1){
									tp = make_pair( i1,i2);
									aa.push_back(tp);
									ac.insert(aa);
									aa.pop_back();
								}
							}
						}
					}
					ab.clear();
					for (it=ac.begin(); it!=ac.end(); it++)
					{
						vector<PII> aa = *it;
						ab.insert(aa);
					}
					ac.clear();

					kk--;
				}
				set<vector<int>> rr;
				set<vector<PII>>::iterator it;
					
				for (it=ab.begin(); it!=ab.end(); it++)
				{
						vector<PII> aa = *it;
						vector<int> vint;
						REP(i,SZ(aa)){
							vint.push_back( aa[i].second);
						}
						rr.insert(vint);
				}
				result = SZ(rr);
				
			}
			
			
		}
		string rsss;
			stringstream out;
			out << result;
			rsss = out.str();
			while( rsss.length() <4 )
			{
				rsss = "0" + rsss;
			}
			cout << "Case #" << (i+1) << ": " << rsss << endl;
			result=0;
		
		
	}
	cout.close();

	cin.close();
	
	return 0;
}