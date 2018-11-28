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
ll l,p,c,kol,fact,t;
int main(){
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>t;
	forn1(j,t){
		f>>l>>p>>c;
		kol=l;
		fact=0;
		kol*=c;
		while(kol<p) {
			kol*=c;
			fact++;
		}
		kol=0;
		while(fact!=0){
			fact/=2;
			kol++;
		}
		cout<<j<<endl;
		f2<<"Case #"<<j<<": "<<kol<<endl;
	}
	f.close();
	f2.close();
	return 0;
}