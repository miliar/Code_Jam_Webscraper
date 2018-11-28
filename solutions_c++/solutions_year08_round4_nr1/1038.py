#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;
ll N, M, V, G, C;
ll ans, now;

struct node{
	ll G, C;
};

vector<node> tree;

ll value(ll pos)
{
	if (pos >= (M-1)/2) return tree[pos].G;
	if (tree[pos].G == 1){
		if ( value(2*(pos+1)-1) == 1 && value(2*(pos+1)) == 1) return 1; else return 0;
	} else {
		if ( value(2*(pos+1)-1) == 1 || value(2*(pos+1)) == 1) return 1; else return 0;
	}
}

void Solve(int step)
{
	if (step == (M-1)/2){
		ll val = value(0);
		if (val == V && now<ans) ans = now;
		return;
	}
	
	if (tree[step].C == 1){
			Solve(step+1);
			now++;
			tree[step].G = 1-tree[step].G;
			Solve(step+1);
			tree[step].G = 1-tree[step].G;
			now--;
	} else Solve(step+1);
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	in >> N;
	node tmp;
	for (int i=0; i<N; i++){
		ans = 1000000;
		tree.clear();
		in >> M >> V;
		for (int j=0; j<(M-1)/2; j++){
			in >> tmp.G >> tmp.C;
			tree.push_back(tmp);
		}

		for (int j=0; j<(M+1)/2; j++){
			in >> tmp.G;
			tree.push_back(tmp);
		}

		Solve(0);
		
		out << "Case #" << i+1 << ": ";
		if (ans != 1000000) out << ans << endl; else out << "IMPOSSIBLE" << endl;
			
	}

	out.close();
	in.close();
	return 0;
}