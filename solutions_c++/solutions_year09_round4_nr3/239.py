#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

struct node {
    int inweight[204];
    int outweight[204];
};

int T;

fstream in, out;

int N, K, M;

int prices[100][25];

node graph[204];

int SOUR, SINK;
int start;
int end;
int flow;

bool isless(int x, int y) {
	for (int i = 0; i < K; i++) {
		if (prices[x][i] >= prices[y][i]) {
			return false;
		}
	}
	return true;
}

int pathLen;
int path[204];
int pathSize;

int INF = 10000000;
bool visited[204];
bool newVisited[204];
int dist[204];
int prev[204];
int numVisited;

void modifyPath(int size) {
    for (int i = 0; i < pathLen-1; i++) {
        graph[path[i]].outweight[path[i+1]] -= size;
        graph[path[i]].inweight[path[i+1]] += size;
        graph[path[i+1]].inweight[path[i]] -= size;
        graph[path[i+1]].outweight[path[i]] += size;
    }
}

int pathMax() {
    int ret = graph[path[0]].outweight[path[1]];
    for (int i = 0; i < pathLen - 1; i++) {
        if (graph[path[i]].outweight[path[i+1]] < ret) {
            ret = graph[path[i]].outweight[path[i+1]];
        }
    }
    return ret;
}

bool findPath() {
	numVisited = 0;
    for (int iii = 0; iii < M; iii++) {
        newVisited[iii] = false;
        visited[iii] = false;
        dist[iii] = 0;
    }
    visited[start] = true;
    dist[start] = INF;
    numVisited++;
    while (numVisited > 0) {
        numVisited = 0;
        for (int i = 0; i < M; i++) {
            if (visited[i]) {
                for (int j = 0; j < M; j++) {
                    if (graph[i].outweight[j] > 0) {
                        if (!visited[j]) {
                            numVisited++;
                        }
                        newVisited[j] = true;
                        int test = dist[i];
                        if (graph[i].outweight[j] < test) {
                            test = graph[i].outweight[j];
                        }
                        if (test > dist[j]) {
                            dist[j] = test;
                            prev[j] = i;
                        }
                    }
                }
            }
        }
        for (int ii = 0; ii < M; ii++) {
            if (newVisited[ii]) {
                visited[ii] = true;
            }
            newVisited[ii] = false;
        }  
    }
    if (!visited[end]) {
        return false;
    } else {
        pathLen = 1;
        int curr = end;
        int index = pathLen - 1;
        while (curr != start) {
            pathLen++;
            curr = prev[curr];
            index--;
        }    
        curr = end;
        index = pathLen - 1;
        while (index >= 0) {
            path[index] = curr;
            curr = prev[curr];
            index--;
        }      
        return true;
    }
}


int maxflow() {
	flow = 0;
	while (findPath()) {
        int pathSize = pathMax();
        flow += pathSize;
        modifyPath(pathSize);
    }
	return flow;
}

int val(int a, int b) {
	return a + b *(N + 2);
}

void add(int a, int b, int c, int d) {
	graph[val(a, b)].outweight[val(c,d)] = 1;
	graph[val(c, d)].inweight[val(a,b)] = 1;
}

int main() {
	in.open("prob3.in", fstream::in);
	out.open("prob3.out", fstream::out);
	in >> T;

    for (int i = 0; i < T; i++) {
		in >> N >> K;
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < K; k++) {
				in >> prices[j][k];
			}
		}
		SOUR = N;
		SINK = N+1;

		start = val(SOUR, 1);
		end = val(SINK, 0);

		for (int iii = 0; iii < N+2; iii++) {
			for (int jjj = 0; jjj < 2*(N+2); jjj++) {
				graph[val(iii, 0)].inweight[jjj] = 0;
				graph[val(iii, 1)].inweight[jjj] = 0;
				graph[val(iii, 0)].outweight[jjj] = 0;
				graph[val(iii, 1)].outweight[jjj] = 0;
			}
		}

		for (int ii = 0; ii < N; ii++) {
			for (int jj = 0; jj < N; jj++) {
				if (isless(ii, jj)) {
					add(ii, 0, jj, 1);
				}
			}			
		}
		for (int xx = 0; xx < N; xx++) {
			add(xx, 1, SINK, 0);
			add(SOUR, 1, xx, 0);
		}

		M = 2*(N+2);
		int ans = N - maxflow();

		out << "Case #" << i + 1 << ": " << ans << endl;
    }
    
	in.close();
	out.close();

	return 0;
}
