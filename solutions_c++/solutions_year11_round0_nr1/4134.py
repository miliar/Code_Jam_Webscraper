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
#include <ctime>
#include <queue>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
#define pr(x) cout<<#x<<" : "<<x<<endl<<flush; 
typedef vector<int> VI;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int,int> pII;
typedef pair<string,int> pSI;
typedef map<int,int> mII;
typedef map<string,int> mSI;
typedef vector<string> VS;

string toStr (int n)
{
  ostringstream oss;
  oss << n;
  string ret = oss.str();
  int i;
  for (i = 0 ; i < ret.sz && ret[i] == '0' ; i ++);
  return ret.substr (i);
}


int toInt (string s)
{
  istringstream iss (s);
  int ret;
  iss >> ret;
  return ret;
}


int main ()
{
	int T = GI;
	
	FORZ (t, T) {
		int n;
		cin >> n;
		
		VS seq;
		VI ora, blue;
		
		FORZ (i, n) {
			char r; int b;
			cin >> r >> b;
			if (r == 'O') ora.PB(b);
			else blue.PB(b);
			string s;
			s += r;
			s += toStr(b);
			seq.PB (s);
		}
		
	
		int oc = 1, bc = 1, sec = 0, bgoto = 0, ogoto = 0;
		
		FORZ (i, seq.sz) {
		
			if (ogoto >= ora.sz && bgoto >= blue.sz)
				break;
		
			string s = seq[i];
			char r = s[0];
			int b = toInt(s.substr(1));
			
			int bnxt = -1, onxt = -1;
			
			if (bgoto < blue.sz) bnxt = blue[bgoto];
			if (ogoto < ora.sz) onxt = ora[ogoto];
						
			if (r == 'O') {				
				while (oc < b) {
					oc ++;
					sec ++;
					if (bnxt != -1) {
						if (bc < bnxt) bc ++;
						else if (bc > bnxt) bc --;
					}	
				}
				while (oc > b) {
					oc --;
					sec ++;
					if (bnxt != -1) {
						if (bc < bnxt) bc ++;
						else if (bc > bnxt) bc --;
					}	
				}
				
				ogoto ++;
				sec ++;
				if (bnxt != -1) {
						if (bc < bnxt) bc ++;
						else if (bc > bnxt) bc --;
				}
			}

			else {
				while (bc < b) {
					bc ++;
					sec ++;
					if (onxt != -1) {
						if (oc < onxt) oc ++;
						else if (oc > onxt) oc --;
					}	
				}
				while (bc > b) {
					bc --;
					sec ++;
					if (onxt != -1) {
						if (oc < onxt) oc ++;
						else if (oc > onxt) oc --;
					}	
				}
				
				bgoto ++;
				sec ++;
				if (onxt != -1) {
						if (oc < onxt) oc ++;
						else if (oc > onxt) oc --;
				}
			}
		}
		
		cout << "Case #" << t + 1 << ": " << sec << "\n";
	}
	
	return 0;
}



















