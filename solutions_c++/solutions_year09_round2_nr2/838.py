#include "stdafx.h"
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

int main(){

	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);

	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{	
		string s,sn;
		cin>>s;
		sn="0"+s;
		next_permutation(sn.begin(),sn.end());
		while (sn[0]=='0')
			sn.erase(0,1);
		printf("Case #%d: ",i+1);
		cout<<sn<<endl;
	}
	
	return 0;
}