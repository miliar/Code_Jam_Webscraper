#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

struct event {
    int where;//1-A, 2-B
    int time;
    int what;//1-start, 2-end+ready to go
    bool operator<(const event &e) const {
	if (time!=e.time)  
    	    return time<e.time;
	if (what!=e.what)    
    	    return what>e.what;//najpierw przyjazdy
	return where>e.where;	
    }
};

/*
struct  cmp
{
  bool operator()(event a, event b) const {
    if (a.time!=b.time)  
        return a.time>b.time;
    return a.what<b.what;//najpierw przyjazdy
  }
};
*/	  

event tab[500];

int N;
int T;
int NA,NB;
string tmp1,tmp2;
int main() {
    cin >> N;
    int casee(0);	
    while (N--) {
	casee++;
	cin >> T;	
	cin >> NA;
	cin >> NB;
	int i(0);
	for (i=0;i<NA;i++) {
	    cin>>tmp1>>tmp2;
	    //cout<<tmp1<<" "<<tmp2<<endl;
	    int m=(tmp1[0]-'0')*10+(tmp1[1]-'0');
	    m*=60;
	    m+=(tmp1[3]-'0')*10+tmp1[4]-'0';
	    //cout<<"from "<<m<<endl;
	    tab[2*i].where=1;//A
	    tab[2*i].time=m;
	    tab[2*i].what=1;
	    
	    m= (tmp2[0]-'0')*10+tmp2[1]-'0';
	    m*=60;
	    m+=(tmp2[3]-'0')*10+tmp2[4]-'0';
	    //cout<<"  to"<<m<<endl;
	    
	    tab[2*i+1].where=2;//B
	    tab[2*i+1].time=m+T;
	    tab[2*i+1].what=2;
	    
	}
        //cout<<"NB    <<<<"<<endl;
	for (;i<NB+NA;i++) {
	    cin>>tmp1>>tmp2;
    	    //cout<<tmp1<<" "<<tmp2<<endl;

	    int m=(tmp1[0]-'0')*10+(tmp1[1]-'0');
	    m*=60;
	    m+=(tmp1[3]-'0')*10+tmp1[4]-'0';
	    //cout<<"from  "<<m<<endl;
	    tab[2*i].where=2;//B
	    tab[2*i].time=m;
	    tab[2*i].what=1;
	    
	    m= (tmp2[0]-'0')*10+tmp2[1]-'0';
	    m*=60;
	    m+=(tmp2[3]-'0')*10+tmp2[4]-'0';
	    //cout<<"  to  " <<m<<endl;
	    
	    tab[2*i+1].where=1;//A
	    tab[2*i+1].time=m+T;
	    tab[2*i+1].what=2;
	    
	}
	
	sort(tab,tab+(NA+NB)*2);	
/*	
	for (i=0;i<(NA+NB)*2;i++){	
	    cout<<tab[i].time<<" "<<tab[i].where<<" "<<tab[i].what<<endl;	    
	}
*/	
	
	//algorithm 
	int trainsA(0),trainsB(0),trainsSA(0),trainsSB(0);
	
	for (int i=0;i<(NA+NB)*2;i++) {
	    if (tab[i].what == 2) {
		if (tab[i].where == 1)
		    trainsA++;
		else
		    trainsB++;	
	    } else {
		if (tab[i].where==1) {
		    if (trainsA>0)
			trainsA--;
		    else
			trainsSA++;	    
		} else {
		    if (trainsB>0)
			trainsB--;
		    else
			trainsSB++;	    
		}
	    }
	}
	cout << "Case #"<<casee<<": "<<trainsSA<<" "<<trainsSB<<endl;
    }
}

