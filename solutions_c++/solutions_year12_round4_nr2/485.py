#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

const int Max = 1000;

int x[Max], y[Max], n, W, L, r[Max];

int posx[Max*Max], posy[Max*Max];

void input() {
    scanf("%d%d%d", &n, &W, &L);
    for(int i = 0;i < n;i ++) scanf("%d", &r[i]);
}

void solve() {
    vector<pair<int,int> > vp;
    for(int i = 0;i < n;i ++) vp.push_back(make_pair(r[i], i));
    
    sort(vp.begin(), vp.end());
    
    int changed = 0;
    
    if(W < L) {
        int tmp = W;
        W = L;
        L = tmp;
        
        changed = 1;
    }
    
    int len = 2;
    posx[0] = 0; posy[0] = 0;
    posx[1] = W; posy[1] = 0;
    
    for(int i = (int)vp.size()-1;i >= 0;i --) {
        int id = vp[i].second;
        int rr = vp[i].first;
        
        for(int j = 1;j < len;j ++) {
            if(posy[j] == 0||posy[j] + rr <= L) {
                if(j == 1) x[id] = 0;
                else x[id] = posx[j-1] + rr;
				if(posy[j] == 0) y[id] = 0;
				else y[id] = posy[j] + rr;
                
                int nx = x[id] + rr;
                if(nx > W) nx = W;
                
                if(nx == posx[j]) posy[j] = y[id] + rr;
                else if(nx < posx[j]) {
                    ++ len;
                    for(int k = len-1;k > j;k --) {
                        posx[k] = posx[k-1];
                        posy[k] = posy[k-1];
                    }
                    posx[j] = nx;
                    posy[j] = y[id] + rr;
                }
                else {
                    int k = j;
                    while(k < len&&posx[k] <= nx) ++ k;
                    
                    posx[j] = nx;
                    posy[j] = y[id] + rr;
                    
                    while(k < len) {
                        ++ j;
                        posx[j] = posx[k];
                        posy[j] = posy[k];
                        ++ k;
                    }

					len = j+1;
                }
				break;
            }
            else posy[j] = L;
        }
	}

	if(changed) {
		for(int i = 0;i < n;i ++) {
			int tmp = x[i];
			x[i] = y[i];
			y[i] = tmp;
		}
		int tmp = W;
		W = L;
		L = tmp;
	}
	
	///*
	for(int i = 0;i < n;i ++) if(x[i] < 0 ||x[i] > W||y[i] < 0||y[i] > L) printf("WA1: %d %d %d %d\n", x[i], W, y[i], L);

	for(int i = 0;i < n;i ++) for(int j = i+1;j < n;j ++) {
		int va = x[i] - x[j];
		if(va < 0) va = -va;

		int va1 = y[i] - y[j];
		if(va1 < 0) va1 = -va1;
		if(va + va1 < r[i] + r[j]) printf("WA: %d %d %d %d %d %d\n", x[i], y[i], x[j], y[j], r[i], r[j]);
	}
	//printf("\n");
    //*/
        
        for(int i = 0;i < n;i ++) printf(" %d.0 %d.0", x[i], y[i]);
        printf("\n");
		
}

int main() {
    freopen("B-large.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d:", cas);
        solve();
    }
    
    return 0;
}
