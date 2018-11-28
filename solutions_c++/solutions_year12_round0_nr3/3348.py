#include <iostream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

map<int,int> M1;
map<int,int> M2;

string tostr(int a)
{
	string s;
	stringstream buf;
	buf<<a;
	s=buf.str();
	return s;
}

int toint(string s)
{
	stringstream buf;
	int a;
	buf<<s;
	buf>>a;
	return a;
}

void countfreq(int n,int m)
{
	M1.clear();
	M2.clear();
	int r;
	while(n){
		r=n%10;
		M1[r]++;
		n=n/10;
	}
	while(m){
		r=m%10;
		M2[r]++;
		m=m/10;
	}
}		

bool valid()
{
	for(int i=0;i<10;i++){
		if(M1[i]!=M2[i]) return false;
	}
	return true;
}

int main()
{
	int t,i,j,A,B,n,m,tc,cnt,l;
	string s1,s2;
	cin>>t;
	tc = 1;
	while(tc <= t) {
		cin>>A>>B;
		cnt=0;
		for(i=A;i<B;i++){
			for(j=i+1;j<=B;j++){
				countfreq(i,j);
				if(valid()){
					s1 = tostr(i);
					s2 = tostr(j);
					l = s1.size();
					for( int k = 0; k < l; k++ ) {
						string tmp = "";
						tmp += s1.substr(k,l-k);
						tmp += s1.substr(0,k);
						if(tmp == s2){
							cnt++;
							break;
						}
					}
				}
			}
		}
		cout<<"Case #"<<tc<<": "<<cnt<<"\n";
		tc++;
	}
	return 0;
}
		
					
					
		
