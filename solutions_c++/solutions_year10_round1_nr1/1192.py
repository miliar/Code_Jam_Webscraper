//Marcin Baran

#include<iostream>
#include<sstream>
#include<vector>
#include<cmath>
#include<list>
#include<algorithm>

using namespace std;
typedef long long int lli;
lli kolumny,wiersze;

lli z,n,k;

vector<string> rotuj(vector<string>& v){
	vector<string> res(v.size(),string());
	for(lli i=v.size()-1;i>=0;--i){
		for(lli j=0;j<(lli)v.size();++j){
			res[j] += v[i][j];
		}
	}
	return res;
}

vector<string> opadaj(vector<string>& v){
	vector<string> res(v.begin(),v.end());
	for(lli i=res.size()-1;i>=0;--i){
		for(lli j=0;j<(lli)res.size();++j){
			if(res[i][j] == '.') continue;
			lli pozycja = i+1;
			while(pozycja < (lli)v.size() && res[pozycja][j] == '.'){
				res[pozycja][j] = res[pozycja-1][j];
				res[pozycja-1][j] = '.';
				++pozycja;
			}
		}
	}
	return res;
}

bool sprawdz(vector<string>& v,char znak,lli k){
	for(lli i=0;i<(lli)v.size();++i){
		for(lli j=0;j<(lli)v.size();++j){
			bool znalazlem = true;
			for(lli l=j;l<j+k;++l){
				if(l == (lli)v.size() || v[i][l] != znak) {znalazlem = 0; break;}
			}
			if(znalazlem) return true;
			znalazlem = 1;
			for(lli l=i;l<i+k;++l){
				if(l == (lli)v.size() || v[l][j] != znak) {znalazlem = 0; break;}
			}
			if(znalazlem) return true;
			znalazlem = true;
			
			for(lli l=0;l<k;++l){
				if(i+l == (lli)v.size() || j+l == (lli)v.size() || v[i+l][j+l] != znak){ znalazlem = 0; break;}
			}
			if(znalazlem) return true;
			znalazlem = true;
			for(lli l=0;l<k;++l){
				if(i-l < 0 || j-l < 0 || v[i-l][j-l] != znak){ znalazlem = 0; break;}
			}
			if(znalazlem) return true;
		}
	}
	return false;
}

string s;
int main(){
	cin>>z;
	for(lli ii=0;ii<z;++ii){
		vector<string> v;
		cin>>n>>k;
		for(lli i=0;i<n;++i){
			cin>>s;
			v.push_back(s);
		}
		vector<string> r = rotuj(v);
//		for(int i=0;i<v.size();++i) cout<<v[i]<<endl;cout<<endl;
//		for(int i=0;i<r.size();++i) cout<<r[i]<<endl;cout<<endl;
		vector<string> rr = opadaj(r);
//		for(int i=0;i<rr.size();++i) cout<<rr[i]<<endl;
		cout<<"Case #"<<ii+1<<": ";
		bool B = sprawdz(rr,'B',k);
		bool R = sprawdz(rr,'R',k);
		if(B & R) cout<<"Both"<<endl;
			else if(B) cout<<"Blue"<<endl;
				else if(R) cout<<"Red"<<endl;
					else cout<<"Neither"<<endl;
	}
	return 0;
}
