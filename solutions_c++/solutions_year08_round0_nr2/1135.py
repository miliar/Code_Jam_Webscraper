#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <string>

using namespace std;

#define ALL(container) (container).begin(),(container).end()
#define REP(i,N) for (int i=0; i<(N); ++i)
#define FOR(i,i_begin,i_end) for (int i=(i_begin); i<=(i_end); ++i)
#define FORD(i,i_begin,i_end) for (int i=(i_begin); i>=(i_end); --i)
#define FOREACH(it, container) for(__typeof((container).begin()) it = (container).begin(); it != (container).end(); ++it)
#define clearStream(_stream_, _str_) getline((_stream_),(_str_))

int main(){

	ifstream inf("B-small.in");
	ofstream outf("B-small.out");
	string clear_str="";
	
	int NumberOfCase = 0;
	inf >> NumberOfCase;
	
	REP(i, NumberOfCase){
		vector<int> a1, a2, b1, b2;
		int na, nb, tt;
		inf >> tt;
		inf >> na >> nb;
		string tmpa, tmpb;
		REP(j, na){
			inf >> tmpa >> tmpb;
			int itmpa=0, itmpb=0;
			
			itmpa = (tmpa[0]-'0')*10 + (tmpa[1]-'0');
			itmpa *= 60;
			itmpa += ((tmpa[3]-'0')*10 + (tmpa[4]-'0'));

			itmpb = (tmpb[0]-'0')*10 + (tmpb[1]-'0');
			itmpb *= 60;
			itmpb += ((tmpb[3]-'0')*10 + (tmpb[4]-'0'));

			a1.push_back(itmpa);
			b2.push_back(itmpb+tt);
		}
		REP(j, nb){
			inf >> tmpa >> tmpb;
			int itmpa=0, itmpb=0;
			
			itmpa = (tmpa[0]-'0')*10 + (tmpa[1]-'0');
			itmpa *= 60;
			itmpa += ((tmpa[3]-'0')*10 + (tmpa[4]-'0'));

			itmpb = (tmpb[0]-'0')*10 + (tmpb[1]-'0');
			itmpb *= 60;
			itmpb += ((tmpb[3]-'0')*10 + (tmpb[4]-'0'));

			b1.push_back(itmpa);
			a2.push_back(itmpb+tt);
		}
		sort(ALL(a1));
		
		sort(ALL(a2));
		sort(ALL(b1));
		sort(ALL(b2));
		int availa=0, resulta=0, availb=0, resultb=0;
		
		int k=0;
		REP(j, na){
			int traina = a1[j];
			if(k < nb){
				while( traina >= a2[k]){
					availa++;
					k++;
					if(k >= nb)
						break;
				}
			}
			if(availa <= 0){
				resulta++;
			}
			else{
				availa--;
			}

		}
		k=0;
		REP(j, nb){
			int trainb = b1[j];
			if(k < na){
				while( trainb >= b2[k]){
					availb++;
					k++;
					if(k >= na)
						break;
				}
			}
			if(availb <= 0){
				resultb++;
			}
			else{
				availb--;
			}

		}

		


		

		outf << "Case #" << i+1 << ": " << resulta << " " << resultb << endl;
	}
	
	outf.close();
	inf.close();
	return 0;
}