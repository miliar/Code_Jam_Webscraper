#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>

using namespace std;

int N,T;
vector<int> VP,VO,VB;
int main(){
	
	scanf("%d",&T);
	
	for (int Test=1;Test<=T;Test++){
		scanf("%d",&N);
		VO.clear();
		VB.clear();
		VP.clear();
		for (int i=0;i<N;i++){
			char c;
			int x;
			scanf("%*c%c%d",&c,&x);
			if (c=='O') VO.push_back(x);
			else VB.push_back(x);
			VP.push_back(c);
		}
		int posO=1,posB=1,cost=0;
		while (VP.size())
			if (VP[0]=='O'){
				int t = abs(VO[0] - posO) + 1;
				posO = VO[0];
				cost += t;
				if (!VB.empty())
					if (abs(VB[0]-posB)<t) posB = VB[0];
					else if (VB[0]<posB) posB -= t;
					 	 else posB += t;
				VO.erase(VO.begin());
				VP.erase(VP.begin());
			}
			else {
				int t = abs(VB[0] - posB) + 1;
				posB = VB[0];
				cost += t;
				if (!VO.empty())
					if (abs(VO[0]-posO)<t) posO = VO[0];
					else if (VO[0]<posO) posO -= t;
					 	 else posO += t;
				VB.erase(VB.begin());
				VP.erase(VP.begin());
			}
		printf("Case #%d: %d\n",Test,cost);
	}
	
	return 0;
}