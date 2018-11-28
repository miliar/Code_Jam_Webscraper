#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <queue>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main() {
	int t,c,d,n,tes=1;
	char magic[105],gabung[40][3],hancur[40][3],x;
	
	scanf("%d",&t);
	while (t--) {
		scanf("%d",&c);
		for (int i=0;i<c;i++) {
			scanf("%s",&gabung[i]);	
		}	
		scanf("%d",&d);
		for (int i=0;i<d;i++) {
			scanf("%s",&hancur[i]);	
		}
		scanf("%d",&n); getchar();
		vector <int> vec;
		for (int i=0;i<n;i++) {
			scanf("%c",&x);	
			bool lagi=true;
			if (vec.empty()) vec.push_back(x); else {
				for (int j=0;j<c;j++)  {
				if (c>=1 && ((vec.back()==gabung[j][0] && x==gabung[j][1]) || (vec.back()==gabung[j][1] && x==gabung[j][0])) ) {
					vec.pop_back();
					vec.push_back(gabung[j][2]);	
					lagi=false;
					break;
				} 
				}
				if (lagi) {
					int pos=-1;
					for (int i=0;i<vec.size();i++) {
						for (int j=0;j<d;j++) {
						if ((vec[i]==hancur[j][0] && x==hancur[j][1]) ||	(vec[i]==hancur[j][1] && x==hancur[j][0])) {pos=i; break;}
						}
						if (pos!=-1) break;
					}
					if (pos!=-1) {
					vec.clear();
					}
					else vec.push_back(x);	
				}	
			}
		}
		printf("Case #%d: [",tes++);
		for (int i=0;i<vec.size();i++) if (i==0) printf("%c",vec[i]);else printf(", %c",vec[i]);
		printf("]\n");
		}
	return 0;
}
