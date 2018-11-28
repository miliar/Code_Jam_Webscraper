#include <vector>
#include <list>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

bool pos[30][11][2];


void doit(){
    int n, s, p, tc,ret=0;
	bool thr;
	vector <pair<int,bool> > vp;
	pair<bool,bool> pr;
    int scr[101];
	cin>>n>>s>>p;
    for(int i=0;i<n;i++){
        cin>>tc; 
		pr.first=pr.second=false;thr=false;
		for(int i=p;i<11;i++){
			if(pos[tc][i][0]==true)pr.first=true;
			if(pos[tc][i][1]==true)pr.second=true;
		}
		for(int i=0;i<11;i++)
		if(pos[tc][i][1])thr=true;
		//f, t = zero
		if(pr.first==false && pr.second==true)vp.push_back(make_pair(0,thr));
		//f, f = 1
		if(pr.first==false && pr.second==false)vp.push_back(make_pair(1,thr));
		//t, t = 2
		if(pr.first==true && pr.second==true)vp.push_back(make_pair(2,thr));
		//t, t = 3
		if(pr.first==true && pr.second==false)vp.push_back(make_pair(3,thr));
    }
	sort(vp.begin(),vp.end());
	for(int i=0;i<vp.size();i++){
		//f, t = zero
		if(vp[i].first==0){
			if(s){
				s--;
				ret++;
			}
		}
		else if(vp[i].first==1){
			if(s && vp[i].second){
				s--;
			}
		}
		else if(vp[i].first==2){
			if(s)s--;
			ret++;
		}
		else{
			if(s && vp[i].second)s--;
			else ret++;
		}
	}
	cout<<ret<<endl;
}
int main(){
    int tc;
    memset(pos,0,sizeof(pos));
    for(int i=0;i<11;i++)
    for(int j=i;j<11 && j<i+3;j++)
    for(int k=j;k<11 && k<i+3;k++){
        tc=i+j+k;
        if(k>i+1){
            pos[tc][i][1]=true;
            pos[tc][j][1]=true;
            pos[tc][k][1]=true;
        }
        else{
            pos[tc][i][0]=true;
            pos[tc][j][0]=true;
            pos[tc][k][0]=true;
        }
    }
	//for(int sum=0;sum<31;sum++)
	//for(int i=0;i<11;i++){
	//	cout<<sum<<" "<<i<<" "<<pos[sum][i][0]<<" "<<pos[sum][i][1]<<endl;
	//}
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}
