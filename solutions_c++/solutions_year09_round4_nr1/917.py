#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <set>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>


using namespace std; 

typedef pair<int,int> intpair;
const int maxsize = 100 ;

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
template<class T> inline void showMatrix(int n,T A[][maxsize])
{for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}
template<class T> inline void showTable(int n, T A[]) 
{for (int i=0;i<n;i++) cout << A[i] <<" " ; cout << endl;  } 
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}

const int movex[]= {-1,0,1,0 }, movey[] = {0,1,0,-1} ; 
bool validMove(int r, int c, int rmax, int cmax) {
    return (r>=0 && r<rmax && c>=0 && c<cmax) ; 
}

// Global variables

int numCases, table[100]; 


// Main code lines !

int sort(int n ) {
	int idx = 0, cnt=0,i,j; 
	for(i=0;i<n;i++) {
		for(j=i;j<n;j++) {
			if (table[j]<=i ) {
				idx = j; break; 
			}
		}
		if (idx!=i ) {
			int temp = table[idx] ; 
			for(j=idx;j>=i+1;j--) {
				table[j] = table[j-1] ; 
			}
			table[i] = temp ; 
			cnt += (idx-i); 
		}
	}
	return cnt ; 
}

void process() {
	int l ; 
	scanf("%d\n",&l);
	for(int i=0;i<l;i++) {
		string temp ; 
		cin >> temp ; 
		temp = temp+"0"; 
		;


		//cout << temp << "--" << temp.find_last_of('1') << "--" << endl; 
		table[i] = temp.find_last_of('1') ; 
	} //cout << endl; 

	cout << sort(l) << endl ; 


	return; 
}

// Main code ends !


int main() {
	freopen("A-large.in","r",stdin);freopen("test.out","w",stdout);
	scanf("%d",&numCases);
	for(int i=1;i<=numCases;i++) {
		printf("Case #%d: ",i);
		process();
	}
	cout.flush;
	return 0 ;
}