#include <iostream>
#include <string>
#include <set>
#include <vector>
using namespace std;

typedef set<int>::iterator si;

int **in_data, h, w, pos, size, next=1;
char **out_data, cur='a', c='a';
set<int> path;

void func(int y, int x){
	if(out_data[y][x] == cur) return;
	if(out_data[y][x] != '*'){
		cur = out_data[y][x];
		next = 0;
		for(si it = path.begin(); it != path.end(); it++){
			out_data[*it/w][*it%w] = cur;
		}
	}
	path.insert(y*w+x);
	out_data[y][x] = cur;
	int min = in_data[y][x];
	
	if(x-1 >= 0)
		if(in_data[y][x-1] < min) min = in_data[y][x-1];
	if(x+1 < w)
		if(in_data[y][x+1] < min) min = in_data[y][x+1];
	if(y-1 >= 0)
		if(in_data[y-1][x] < min) min = in_data[y-1][x];
	if(y+1 < h)
		if(in_data[y+1][x] < min) min = in_data[y+1][x];
		
	if(min != in_data[y][x]){
		if(y-1 >= 0){
			if(min == in_data[y-1][x]){
				func(y-1, x);
				return;
			}
		}
		if(x-1 >= 0){
			if(min == in_data[y][x-1]){
				func(y, x-1);
				return;
			}
		}
		if(x+1 < w){
			if(min == in_data[y][x+1]){
				func(y, x+1);
				return;
			}
		}
		if(y+1 < h){
			if(min == in_data[y+1][x]){
				func(y+1, x);
				return;
			}
		}
	}
}

int main(){
	int n, f=0;
	cin >> n;
	for(int i = 1; i <= n; i++){
		cur = c = 'a';
		path.clear();
		cin >> h >> w;
		in_data = new int*[h];
		out_data = new char*[h];
		for(int j = 0; j < h; j++){
			in_data[j] = new int[w];
			out_data[j] = new char[w];
			for(int k = 0; k < w; k++){
				cin >> in_data[j][k];
				out_data[j][k] = '*';
			}
		}
		for(int j = 0; j < h; j++){
			for(int k = 0; k < w; k++){
				path.clear();
				next = 1;
				cur = c;
				func(j,k);
				if(next) c++;
				path.clear();
			}
		}
		cout << "Case #" << i << ":" << endl;
		for(int j = 0; j < h; j++){
			for(int k = 0; k < w; k++){
				cout << out_data[j][k];
				if(k != w-1) cout << " ";
			}
			cout << endl;
		}
	}
}

