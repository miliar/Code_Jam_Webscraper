#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

#define FOR(i,a) for (int (i)=0;(i)<(a);++(i))
#define FORR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define sz(a) int((a).size()) 
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end() 

string L;
map<string,int> out;

string star(string in){
	string out="";
	FOR(i,sz(in)){
		out+="*";
	}
	return out;
}

void rek(vector<pair<string,string> > a,int pos,int tips){
	bool change=false;
	if (pos>-1){
		FOR(i,sz(a)){
			FOR(j,sz(a[i].first)){
				if (a[i].second[j]==L[pos]){		
					a[i].first[j]=L[pos];
					change=true;
				}
			}
		}
	}
	sort(all(a));
	//rozdel podla prveho
	string last=a[0].first;
	vector<pair<string,string> > pom(1,a[0]);
	FORR(i,1,sz(a)){
		if (a[i].first==last){
			pom.pb(a[i]);
		}
		else{
			//testni ci obsahuje to co sme tipovali, ak ano tak si uloz dakde +1
			//zisti ci je len jedno, ak je len jedno, tak ho uloz do pola s tips map<string,tips+zvysok>
			//inak rekurzivne zavolaj toto pre pom,pos+1,tips
			int add=1;
			if (pos==-1 || change==false) add=0;
			else{
				FOR(j,sz(last)){
					if (last[j]==L[pos]) add=0;
				}
			}
			if (sz(pom)==1) out[a[i-1].second]=tips+add;
			else{
				rek(pom,pos+1,tips+add);
			}
			
			pom.clear();
			pom.pb(a[i]);
		}
		last=a[i].first;
	}
	//copy paste zhora
	int add=1;
	if (pos==-1 || change==false) add=0;
	else{
		FOR(j,sz(last)){
			if (last[j]==L[pos]) add=0;
		}
	}
	if (sz(pom)==1) out[a[sz(a)-1].second]=tips+add;
	else{
		rek(pom,pos+1,tips+add);
	}
	
	
}

//predpokladam, ze to neobsahuje duplikaty, ak hej, tak to treba osetrit

main(){
	ofstream fout ("B-small-0.out");
	ifstream fin ("B-small-0.in");
	int T;
	fin>>T;
	FOR(num,T){
		int N,M;
		fin>>N;
		fin>>M;
		vector<pair<string,string> > words;

		FOR(i,N){
			string pom_string;
			fin>>pom_string;
			words.pb(mp(star(pom_string),pom_string));
		}

		fout<<"Case #"<<num+1<<":";
		FOR(i,M){
			out.clear();
			fin>>L;
			rek(words,-1,0);
			int opt=-1;
			string vypis;
			FOR(j,sz(words)){
		//		cout<<words[j].second<<" "<<out[words[j].second]<<endl;
				if(out[words[j].second]>opt){
					opt=out[words[j].second];
					vypis=words[j].second;
				}
			}
	//		cout<<"-----------------------------------";
			fout<<" "<<vypis;
		}
		fout<<endl;
	}
	fout.close();
}
