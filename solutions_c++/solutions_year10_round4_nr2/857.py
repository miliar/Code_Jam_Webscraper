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
int p, noofteams;
bool bought[3000];
int miss[3000];
int getroot(int val){
	while(val>1 && !bought[val/2])
		val/=2;
	return val;
}
void reducemiss(int node){
	if(node>=noofteams){
		node-=noofteams;
		miss[node]++;
		return;
	}
	reducemiss(node*2);
	reducemiss(node*2+1);
}
void doit(){
	int ticketnode,result=0,price,noofmatch;
	memset(bought,0,sizeof(bought));
	cin>>p;
	noofteams=1;
	for(int i=0;i<p;i++)noofteams=noofteams<<1;
	for(int i=0;i<noofteams;i++)cin>>miss[i];
	noofmatch=noofteams;
	for(int i=0;i<noofteams;i++){
		noofmatch=noofmatch>>1;
		for(int j=0;j<noofmatch;j++)cin>>price;
	}
	for(int i=0;i<noofteams;i++)
	{
		while(miss[i]<p){
			ticketnode=getroot(noofteams+i);
			bought[ticketnode]=true;
			reducemiss(ticketnode);
			result++;
		}
	}
	cout<<result<<endl;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

