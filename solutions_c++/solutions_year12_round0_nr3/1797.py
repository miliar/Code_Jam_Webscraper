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
set <pair<int,int> > st;
set <pair<int,int> >::iterator it;

void doit(){
	int a,b,ret=0;
	cin>>a>>b;
	for(it=st.begin();it!=st.end();it++)
	if((*it).first>=a && (*it).first<=b && (*it).second>=a && (*it).second<=b){
		ret++;
	}
	ret/=2;
	cout<<ret<<endl;
}
int main(){
    int tc,tm,md;
    pair<int,int> pr;
    string str;
    for(int i=11;i<2000001;i++){
        if(i>999999)tc=1000000;else if(i>99999)tc=100000;else if(i>9999)tc=10000;else if(i>999)tc=1000;else if(i>99)tc=100;else tc=10;
        md=i%10;
        tm=i/10 + md*tc;
        while(tm!=i){
            if(md){
                pr.first=i;pr.second=tm;
                st.insert(pr);
            }
            md=tm%10;
            tm=tm/10 + md*tc;
        }
    }
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

