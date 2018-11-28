#include <stdio.h>
#include <string.h>
#include <set>
using namespace std;


struct PP{
  int y, x;
  PP(int y, int x){
	  this->y = y;
	  this->x = x;
  }
  PP(){x = y = 0;}
  bool operator < (const PP& pp) const{
	  if (this->y != pp.y) return this->y < pp.y;
	  else return this->x < pp.x;
  }

};

set<PP> a[2];




int main(){
	int T;
	scanf("%d", &T);
	for (int ttt =1 ; ttt <=T; ttt++){
		a[0].clear();
		int R;
		scanf("%d", &R);
		for (int r = 0; r < R; r++){
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int y = y1; y<=y2; y++){
				for (int x = x1; x <=x2; x++){
					a[0].insert(PP(y, x));
				}
			}
		}
		int swt;
		swt = 0;
		int res = 0;
		while (!a[swt].empty()){
			a[!swt].clear();
			set<PP>::iterator it = a[swt].begin();
			set<PP>::iterator itend = a[swt].end();
			for (;it!=itend;++it){
				if( (a[swt].find(PP(it->y-1, it->x)) != itend) || (a[swt].find(PP(it->y, it->x-1)) != itend))
						a[!swt].insert(*it);
				if (a[swt].find(PP(it->y+1, it->x-1))!=itend)
					a[!swt].insert(PP(it->y+1, it->x));
			}
			
			res++;
			swt=!swt;
		}
		printf("Case #%d: %d\n", ttt, res);
	}
	return 0;
}