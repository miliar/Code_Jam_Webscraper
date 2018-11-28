#include <fstream>
using namespace std;

ifstream IN("B-large.in");
ofstream OUT("B-large.out");


template<class T> class matrix {
	T *underlying, H, W;
	public:
		matrix(int H, int W): H(H), W(W){
			underlying = new T[H*W];
		}
		matrix(int H, int W, T v): H(H), W(W){
			underlying = new T[H*W];
			for (int i = 0; i < H*W; i++) underlying[i] = v;
		}
		T& operator()(int i, int j){
			return underlying[i*W+j];
		}
		const T& operator()(int i, int j) const{
			return underlying[i*W+j];
		}
		~matrix(){
			delete[] underlying;
		}
};

struct point {
	int x, y;
	point(int x=0, int y=0): x(x), y(y) {}
};

int minimun(int a, int b, int c, int d){
	int min = a < b ? a : b;
	min = min < c ? min : c;
	return min < d ? min : d;
}

point flow_to(matrix<int> map, int i, int j){
	int min = minimun(map(i-1,j), map(i,j-1), map(i,j+1), map(i+1,j));
	if (map(i,j) <= min) return point(i,j);
	if (min == map(i-1,j)) return point(i-1,j);
	if (min == map(i,j-1)) return point(i,j-1);
	if (min == map(i,j+1)) return point(i,j+1);
	if (min == map(i+1,j)) return point(i+1,j);
}

void print(const matrix<char> &result, int H, int W){
	for (int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++){
			OUT << result(i,j);
			if (j < W) OUT << " ";
		}
		if (i < H) OUT << endl;
	}
}

int main(){
	int T, H, W;
	IN >> T;
	for (int t = 1; t <= T; t++){
		IN >> H >> W;
		matrix<int> map(H+2, W+2);
		for (int i=0; i< H+2; i++){
			for (int j = 0; j < W+2; j++){
				if (!i || !j || i>H || j>W) map(i, j) = 10001;
				else IN >> map(i, j);
			}
		}
		
		OUT << "Case #" << t << ":" << endl;
		char label = 'a';
		matrix<char> result(H+2, W+2, ' ');
		for (int i=1; i<= H; i++){
			for (int j = 1; j <= W; j++){
				if (result(i,j) != ' ') continue;
				point p(i,j), from;
				do {
					from = p;
					p = flow_to(map, from.x, from.y);
				} while (!(from.x == p.x && from.y == p.y) && result(p.x, p.y) == ' ');
				if (result(p.x, p.y) == ' ') result(p.x, p.y) = label++;
				char c = result(p.x, p.y);
				
				p = point(i,j);
				do {
					result(p.x, p.y) = c;
					from = p;
					p = flow_to(map, from.x, from.y);
				} while (!(from.x == p.x && from.y == p.y) && result(p.x, p.y) != ' ');
			}
		}
		print(result, H, W);
		if(t < T) OUT << endl;
	}
}
