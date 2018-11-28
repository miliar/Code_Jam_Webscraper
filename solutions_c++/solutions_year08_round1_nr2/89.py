#include <iostream>
#include <queue>
using namespace std;

// First is customer, second is flavor.
bool likesMalted[2000][2000]; 
bool likesUnmalted[2000][2000];
bool malted[2000];
int numLiked[2000];
queue<int> toProcess;

int main() {
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) {
		int N, M;
		cin >> N >> M;
		for (int j = 0; j < N; j++) malted[j] = false;
		for (int j = 0; j < M; j++) {
			cin >> numLiked[j];
			for (int k = 0; k < N; k++) likesMalted[j][k] = likesUnmalted[j][k] = false;
			for (int k = 0; k < numLiked[j]; k++) {
				int f;
				cin >> f;
				int malted;
				cin >> malted;
				if (malted) likesMalted[j][f-1] = true;
				else likesUnmalted[j][f-1] = true;
			}
			if (numLiked[j] == 1) toProcess.push(j);
		}
		bool possible = true;
		
		while (!toProcess.empty()) {
			int j = toProcess.front();
			toProcess.pop();
			int liked = -1;
			for (int k = 0; k < N; k++) if (likesMalted[j][k]) liked = k;
			if (liked < 0) continue;
			malted[liked] = true;
			for (int k = 0; k < M; k++) if (likesUnmalted[k][liked]) {
				likesUnmalted[k][liked] = false;
				numLiked[k]--;
				if (numLiked[k] == 1) toProcess.push(k);
				if (numLiked[k] == 0) possible = false;
			}
		}
		
		cout << "Case #" << i+1 << ": ";
		if (!possible) cout << "IMPOSSIBLE\n";
		else for (int j = 0; j < N; j++) {
			if (malted[j]) cout << 1;
			else cout << 0;
			cout << (j == N-1 ? '\n' : ' ');
		}
	}
}
