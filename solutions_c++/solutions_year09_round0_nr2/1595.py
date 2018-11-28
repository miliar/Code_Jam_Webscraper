#include <iostream>
#include <vector>

using namespace std;

struct Cell;

struct Cell{
	int a;
	char c;
	Cell *l;
	Cell(int x):a(x),c('_'),l(NULL) {};
};

int H, W;
int getId(int x, int y) {
	if(x<0 || x>= W) return -1;
	if(y<0 || y>= H) return -1;
	return x+y*W;
};

main(){
	int N;
	cin >> N;
	for(int n=0; n<N; ++n){
		cin >> H >> W;
		vector<Cell> map;
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++){
				int a;
				cin >> a;
				map.push_back(Cell(a));
			}
		}
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++){
				int me=getId(w, h);
				Cell *to= NULL;
				int a=	map[me].a;
				int nei = getId(w,h+1);
				if(nei >=0 && map[nei].a <= a) {
					to=&map[nei];
					a = map[nei].a;
				}
				nei = getId(w+1, h);
				if(nei >=0 && map[nei].a <= a) {
					to=&map[nei];
					a = map[nei].a;
				}
				nei = getId(w-1, h);
				if(nei >=0 && map[nei].a <= a) {
					to=&map[nei];
					a = map[nei].a;
				}
				nei = getId(w, h-1);
				if(nei >=0 && map[nei].a <= a) {
					to=&map[nei];
					a = map[nei].a;
				}
				if(map[me].a > a) {
					map[me].l = to;
			 	}	
			}
		}
		char c='a';
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++){
				char thisc=c;
				int me=getId(w,h);
				Cell *next=&map[me];
				while(next->c == '_' && next->l != NULL) 
					next=next->l;
				if (next->c != '_') thisc=next->c;
				else c++;
				next=&map[me];
				while(next->c == '_' && next->l != NULL) {
					next->c = thisc;
					next=next->l;
				}
				next->c = thisc;
			}
		}
		cout << "Case #" << n+1 <<":" << endl;
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++){
				int me=getId(w,h);
				cout << map[me].c << " ";
//				if(map[me].l) cout << " ";
//				else cout << "X";
			}
			cout << endl;
		}
	}	
}

					
		
			
				
	

