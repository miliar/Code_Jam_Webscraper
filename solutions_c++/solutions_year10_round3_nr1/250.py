#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <fstream>

#define ll long long
#define forn(i,n) for(int i=0;i!=n;i++)
#define forn1(i,n) for(int i=1;i<=n;i++)
#define ford(i,n) for(int i=n-1;i!=-1;i--)
#define ford1(i,n) for(int i=n;i!=0;i--)
#define pb(a) push_back(a)

using namespace std;
int mass[2][1000];
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	int t,n,kol;
	f>>t;
	forn1(j,t){
		f>>n;
		forn(i,n){
			f>>mass[0][i]>>mass[1][i];
		}
		kol=0;
		forn(i,n){
			forn(x,n){
				if (i!=x){
					if ((mass[0][i]-mass[0][x])*(mass[1][i]-mass[1][x])<0) kol++;
				}
			}
		}
		f2<<"Case #"<<j<<": "<<kol/2<<endl;
	}
	f.close();
	f2.close();
	return 0;
}