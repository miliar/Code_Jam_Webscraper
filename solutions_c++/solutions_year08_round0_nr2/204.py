#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int puppa(string a) {
	int A=0;
	bool f=true;
	for (int i=0; i<a.size(); i++) {
		if (a[i]==':') f=false;
		else {
			if (f) A*=10;
			else A*=6;
			f=true;
			A+=a[i]-'0';
			}
		}
	return A;	
	}

int miao(vector <pair<int, bool> > a) {
	int t=0;
	int q=0;
	for (int i=0; i<a.size(); i++) {
		if (a[i].second==true) {
			q--;
			if (q<0) {t=t-q; q=0;}
			}
		else q++;	
		}
	return t;
	}

int main (void) {
    ofstream OUT;
    OUT.open ("OU.txt");
    ifstream FILE("IN.txt");
    int Num;
    FILE>>Num;
	for (int z=1; z<=Num; z++) {
		cout<<z<<"\n";
		int NA,NB,T;
		FILE>>T>>NA>>NB;
		vector <pair<int,bool> > a;
		vector <pair<int,bool> > b;
		string k1,k2;
		cout<<NA<<"\n";
		for (int i=0; i<NA; i++) {
			k1="";
			FILE>>k1;
			k2="";
			FILE>>k2;
			a.push_back(pair<int,bool> (puppa(k1)*2+1, true) );
			b.push_back(pair<int,bool> (puppa(k2)*2+T*2, false) );
			}
		cout<<NB<<"\n";
		for (int i=0; i<NB; i++) {
			k1="";
			FILE>>k1;
			k2="";
			FILE>>k2;
			b.push_back(pair<int,bool> (puppa(k1)*2+1, true) );
			a.push_back(pair<int,bool> (puppa(k2)*2+T*2, false) );
			}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		
//		cout<<"DARIO PUPPA "<<miao(a)<<" "<<miao(b)<<"\n\n";
		
		
		
		
//		for (int i=0; i<a.size(); i++) cout<<a[i].first<<" "<<a[i].second<<"\n";
		OUT<<"Case #"<<z<<": "<<miao(a)<<" "<<miao(b)<<"\n";
        	}
    FILE.close();
    OUT.close();
    system("PAUSE");
    return 0;
    }
