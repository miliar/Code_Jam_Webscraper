/*
name:pABotTrust
By Tony
2011-5-7 ÉÏÎç09:54:06
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <string>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("pABotTrust","r",stdin);
    freopen("pABotTrust.out","w",stdout);
#endif
    int icas=0;
    int cas;
    int otime,btime;
    int opos,bpos;
    char group[3];
    int pos;
    int n;

    char prepush;

    cin>>cas;
    while(cas--){
    	++icas;
    	opos=bpos=1;
    	otime=btime=0;
    	cin>>n;
    	n--;
		scanf("%s",group);
		scanf("%d",&pos);
		if(group[0]=='O')
			otime+=(abs(opos-pos)+1),opos=pos,prepush='O';
		else
			btime+=(abs(bpos-pos)+1),bpos=pos,prepush='B';

    	while(n--){
    		int dt;
    		scanf("%s",group);
    		scanf("%d",&pos);
    		if(group[0]=='O'){
    			dt=abs(opos-pos)+1;
    			if(prepush=='O')
    				otime+=dt;
    			else
    				otime=max(otime+dt,btime+1);
    			opos=pos;
    			prepush='O';
    		}
    		else{
    			dt=abs(bpos-pos)+1;
    			if(prepush=='B')
    				btime+=dt;
    			else
    				btime=max(btime+dt,otime+1);
    			bpos=pos;
    			prepush='b';
    		}
    	}
    	printf("Case #%d: %d\n",icas,max(otime,btime));

    }



	return 0;
}
