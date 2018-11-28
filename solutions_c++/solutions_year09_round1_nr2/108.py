#include <iostream>
#include <queue>
using namespace std;

struct node {
	int row;
	int col;
	int topBottom;
	int leftRight;
	long long t;
};

bool operator<(node a, node b) {
	return a.t > b.t;
}

int C;
int N, M;
int upDownLength[25][25], leftRightLength[25][25], cycleShift[25][25];
long long tim[25][25][2][2]; // third and fourth indices are top vs bottom and left vs right

int main() {
	cin >> C;
	for (int z = 0; z < C; z++) {
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++) {
				cin >> upDownLength[i][j] >> leftRightLength[i][j] >> cycleShift[i][j];
				cycleShift[i][j] = upDownLength[i][j]+leftRightLength[i][j]-cycleShift[i][j]%(upDownLength[i][j]+leftRightLength[i][j]);
				tim[i][j][0][0] = tim[i][j][0][1] = tim[i][j][1][0] = tim[i][j][1][1] = -1;
			}
		tim[N-1][0][1][0] = 0;
		node start = { N-1, 0, 1, 0, 0 };
		priority_queue<node> pq;
		pq.push(start);
		while (!pq.empty()) {
			node c = pq.top();
			pq.pop();
			if (tim[c.row][c.col][c.topBottom][c.leftRight] != c.t) continue;
			
			int cycleStage = c.t+cycleShift[c.row][c.col];
			int nextUpDown = (cycleStage%(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) < upDownLength[c.row][c.col] ? c.t : (cycleStage/(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) + 1)*(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) - cycleShift[c.row][c.col]);
			int cycleShift2 = cycleShift[c.row][c.col]+leftRightLength[c.row][c.col];
			int cycleStage2 = c.t+cycleShift2;
			int nextLeftRight = (cycleStage2%(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) < leftRightLength[c.row][c.col] ? c.t : (cycleStage2/(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) + 1)*(upDownLength[c.row][c.col]+leftRightLength[c.row][c.col]) - cycleShift2);
			
			if (tim[c.row][c.col][!c.topBottom][c.leftRight] == -1 || nextUpDown+1 < tim[c.row][c.col][!c.topBottom][c.leftRight]) {
				tim[c.row][c.col][!c.topBottom][c.leftRight] = nextUpDown+1;
				node n = { c.row, c.col, !c.topBottom, c.leftRight, nextUpDown+1 };
				pq.push(n);
			}
			
			if (tim[c.row][c.col][c.topBottom][!c.leftRight] == -1 || nextLeftRight+1 < tim[c.row][c.col][c.topBottom][!c.leftRight]) {
				tim[c.row][c.col][c.topBottom][!c.leftRight] = nextLeftRight+1;
				node n = { c.row, c.col, c.topBottom, !c.leftRight, nextLeftRight+1 };
				pq.push(n);
			}
			
			if (c.row > 0 && c.topBottom == 0 && (tim[c.row-1][c.col][1][c.leftRight] == -1 || c.t+2 < tim[c.row-1][c.col][1][c.leftRight])) {
				tim[c.row-1][c.col][1][c.leftRight] = c.t+2;
				node n = { c.row-1, c.col, 1, c.leftRight, c.t+2 };
				pq.push(n);
			}
			
			if (c.row < N-1 && c.topBottom == 1 && (tim[c.row+1][c.col][0][c.leftRight] == -1 || c.t+2 < tim[c.row+1][c.col][0][c.leftRight])) {
				tim[c.row+1][c.col][0][c.leftRight] = c.t+2;
				node n = { c.row+1, c.col, 0, c.leftRight, c.t+2 };
				pq.push(n);
			}
			
			if (c.col > 0 && c.leftRight == 0 && (tim[c.row][c.col-1][c.topBottom][1] == -1 || c.t+2 < tim[c.row][c.col-1][c.topBottom][1])) {
				tim[c.row][c.col-1][c.topBottom][1] = c.t+2;
				node n = { c.row, c.col-1, c.topBottom, 1, c.t+2 };
				pq.push(n);
			}
			
			if (c.col < M-1 && c.leftRight == 1 && (tim[c.row][c.col+1][c.topBottom][0] == -1 || c.t+2 < tim[c.row][c.col+1][c.topBottom][0])) {
				tim[c.row][c.col+1][c.topBottom][0] = c.t+2;
				node n = { c.row, c.col+1, c.topBottom, 0, c.t+2 };
				pq.push(n);
			}
		}
		
		cout << "Case #" << (z+1) << ": " << tim[0][M-1][0][1] << endl;
	}
	return 0;
}
