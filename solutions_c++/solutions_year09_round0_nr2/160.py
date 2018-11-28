#include <iostream>
#include <map>
#include <vector>

using namespace std;

#define MAX 100 * 100 + 1

struct set{
	int p[MAX],rank[MAX], number[MAX];
	int size, sets;
 
	void init(int s){
		size = sets = s; // cada elemento é um conjunto
		for (int i = 0; i < size; i++) 
			{p[i]=i; rank[i]=0; number[i]=1;}
	}
 
	void link(int x, int y) {
		if(x == y) return; //andre.sp fix: ja tao ligados nao queremos contar o comprimento 2 vezes
		if (rank[x] <= rank[y]) {
		    p[x] = y;
                    --sets; //pedro.silva: se unimos dois conjuntos temos menos um
		    number[y] += number[x];
		    if (rank[x] == rank[y])
		      rank[y]++;
		} else link(y, x);
	}
 
	int find_set(int x) {
	  if (x != p[x]) p[x] = find_set(p[x]);
	  return p[x];
	}
	int find_length(int x) {
	  return number[ find_set(p[x]) ];
	}
	void union_set(int x,int y) {
	  link(find_set(x), find_set(y));
	}
};

void solve(int * mapi, int w, int h) {
	set s; s.init(w * h);

	for (int l = 0; l < h; l++) {
		for (int c = 0; c < w; c++) {
			int v = mapi[c + l*w];
			vector<char> n;

			int low = 0;

			if (l!=0 && v - mapi[c + (l - 1) * w] > low) low = v - mapi[c + (l - 1) * w];
			if (c!=0 && v - mapi[c - 1 + l * w] > low) low = v - mapi[c - 1 + l * w];  
			if (c!=w-1 && v - mapi[c + 1 + l * w] > low) low = v - mapi[c + 1 + l * w];   
			if (l!=h-1 && v - mapi[c + (l + 1) * w] > low) low = v - mapi[c + (l + 1) * w];  

			if (low == 0) continue;

			if (l!=0 && v - mapi[c + (l - 1) * w] == low) n.push_back('n');  
			if (c!=0 && v - mapi[c - 1 + l * w] == low) n.push_back('w');  
			if (c!=w-1 && v - mapi[c + 1 + l * w] == low) n.push_back('e');  
			if (l!=h-1 && v - mapi[c + (l + 1) * w] == low) n.push_back('s');  

			if (n[0] == 'n') s.union_set(c + l*w, c + (l - 1)*w);
			if (n[0] == 'w') s.union_set(c + l*w, c - 1 + l*w);
			if (n[0] == 'e') s.union_set(c + l*w, c + 1 + l*w);
			if (n[0] == 's') s.union_set(c + l*w, c + (l + 1)*w);
		}
	}

	char let; let = 'a';

	map<int, char> m;
	for (int l = 0; l < h; l++) {
		for (int c = 0; c < w; c++) {
			int le = s.find_set(c + l*w);
			if (m.find(le) == m.end()) m[le] = let++;
			char cc = m[le];
			cout << cc;
			if (c < w - 1) cout << ' ';
		}
		cout << endl;	
	}	
}

int main() {
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int w, h; cin >> h >> w;
		int mapi[MAX];
		for (int l = 0; l < h; l++)
			for (int c = 0; c < w; c++) {
				cin >> mapi[c + l*w];
			}
		cout << "Case #" << (i+1) << ":" << endl;
		solve(mapi, w , h);
	}
}
