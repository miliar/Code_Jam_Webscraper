#include <vector>
#include <list>
#include <ctime>
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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll unsigned long long
#define pb push_back
#define mp make_pair
#define size(v) (int)(v.size())
#define all(v) v.begin(), v.end()


using namespace std;

int toTime(string str){
	int start=0;
	for(int i=0;i<size(str);i++){
		if(str[i]==':')
			continue;
		start+=str[i]-'0';
		start*=10;
	}
	start/=10;

	return start;
}

int cmpS(pair<int,int> p1, pair<int,int>p2){
	return p1.first<p2.first;
}

int cmpE(pair<int,int> p1, pair<int,int>p2){
	return p1.second<p2.second;
}
int xfind(int n,vector<pair<int,int> >& ve){
	for(int i=0;i<size(ve);i++){
		if(ve[i].second<=n) return i;
	}
	return -1;
}

int xcount(vector<pair<int,int> >& vecs , vector<pair<int,int> >& vecb){
	int cnt=0;
	for(int i=0;i<size(vecs)&&vecb.empty()==false;i++){
		int j=xfind(vecs[i].first,vecb);
		if(j!=-1){
			vecb.erase(vecb.begin()+j);
			cnt++;
		}

	}

	return cnt;

}

int main() {

    int i,j,k;
    int t,T;
    //char st[1000];

    cin>>t;
    //cin.getline(st,1000);
    for(i=0;i<t;i++){
    	int na,nb;
    	vector<pair<int,int> > vsa,vsb;

    	string start,end;
    	cin>>T;
    	//cin.getline(st,1000);
		cin>>na>>nb;
    	//cin.getline(st,1000);
    	for(j=0;j<na;j++){
    		cin>>start;
    		cin>>end;
    		int stt=toTime(start);
    		int ett=toTime(end)+T;
    		vsa.pb(mp(stt,ett));
    	}
    	for(j=0;j<nb;j++){
    		cin>>start;
    		cin>>end;
    		int stt=toTime(start);
    		int ett=toTime(end)+T;
    		vsb.pb(mp(stt,ett));
    	}

    	vector<pair<int,int> > vea(vsa),veb(vsb);
    	sort(all(vsa),cmpS);
    	sort(all(vsb),cmpS);
    	sort(all(vea),cmpE);
    	sort(all(veb),cmpE);


//    	for(i=0;i<size(vsa);i++){
//    		cout<<vsa[i].first<<" "<<vea[i].second<<endl;
//    	}
//    	for(i=0;i<size(vsb);i++){
//    	    cout<<vsb[i].first<<" "<<veb[i].second<<endl;
//    	}

    	int c1=xcount(vsa,veb);
    	int c2=xcount(vsb,vea);

    	//cout<<c1<<" "<<c2<<endl;
    	cout<<"Case #"<<i+1<<": "<<size(vsa)-c1<<" "<<size(vsb)-c2<<endl;

    }


    return 0;
}
