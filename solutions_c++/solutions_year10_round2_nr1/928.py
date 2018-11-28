//BISMILLAHIRRAHMANIRRAHIM


#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

/*
map < string , vector < string > > g;

int creat(string r,string s) {
	string tm="";
	int i=1,j=s.size(),k,l;
	while(i<j && s[i]!='/') {
		tm+=s[i];
		i++;
	}
	for(k=0,l=g[r].size();k<l;k++) {
		if(g[r][k]==tm) {
			if(i==j) return 0;
			else return creat(
*/

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-practice-L.out","w",stdout);
	int T,I,i,j,k,n,m,q;
	cin>>T;
	set < string > s;
	set < string > :: iterator it;
	string l;
	for(I=1;I<=T;I++) {
		cin>>n>>m;
		s.clear();
		q=0;
		while(n--) {
			cin>>l;
			j=l.size();
			for(i=1;i<j;i++) if(l[i]=='/') {
				s.insert(string(l.begin(),l.begin()+i));
			}
			s.insert(l);
		}
		while(m--) {
			cin>>l;
			if(l=="/") continue;
			j=l.size();
			for(i=1;i<j;i++) if(l[i]=='/') {
				it=s.find(string(l.begin(),l.begin()+i));
				if(it==s.end()) {
					q++;
					s.insert(string(l.begin(),l.begin()+i));
				}
			}
			it=s.find(l);
			if(it==s.end()) {
				q++;
				s.insert(l);
			}
		}
		printf("Case #%d: %d\n",I,q);
			
	}
	return 0;
}
