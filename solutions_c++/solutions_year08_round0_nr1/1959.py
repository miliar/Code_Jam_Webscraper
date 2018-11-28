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
#define loop(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define vi vector<int>
#define vvi vector<vector<int> > vvi
#define vs vector<string>

using namespace std;

int qs[1001];
const int Max = 100000;
int MS;
int MQ;

set<int> sset;
void fillset(){
	for(int i=1;i<=MS;i++){
			sset.insert(i);
		}
}
int doit(){

	fillset();
	int count=0;
	for(int i=0;i<MQ;i++){
		sset.erase(qs[i]);
		if(sset.empty()){
			fillset();
			count++;
			i--;
		}
	}
	return count;
}

int main() {

    int i,j,k;
    int t;
    char st[1000];

    cin>>t;
    cin.getline(st,1000);
    for(i=0;i<t;i++){
    	int s,q;
		memset(qs,0,sizeof qs);
		map<string,int > se;
    	string str;
    	cin>>s;
    	cin.getline(st,1000);
    	MS=s;
    	for(j=0;j<s;j++){
    		cin.getline(st,1000);
    		str=st;
    		se.insert(mp(str,j+1));
    	}
    	cin>>q;
    	cin.getline(st,1000);
    	MQ=q;
    	for(k=0;k<q;k++){
    		cin.getline(st,1000);
    		str=st;
    		int m=se[str];
    		qs[k]=m;
    	}
    	if(q==0){
    		cout<<"Case #"<<i+1<<": "<<0<<endl;
    	}
    	else if(q==1){
    		cout<<"Case #"<<i+1<<": "<<0<<endl;
    	}
    	else{
    		sset.clear();
    		cout<<"Case #"<<i+1<<": "<<doit()<<endl;
    	}

    }


    return 0;
}
