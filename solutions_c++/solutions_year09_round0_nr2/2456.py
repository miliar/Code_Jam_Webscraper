#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <sstream>
using namespace std;

const int sz = 103;
const int inf = 100001;
bool used[sz][sz], back[sz][sz], F[sz * sz + 11][sz * sz + 11];
char out[sz][sz];
int G[sz][sz];
int Q[sz * sz + 11][2];
int dh[] = {-1, 0, 0, 1};
int dw[] = {0, -1, 1, 0};

//find the sink location, next find all node can come to this sink
void bfs(int h, int w, int H, int W, int& sh, int& sw)
{
    int j, head, tail, ch, cw, nh, nw, mh, mw, mp;
    head = 0, tail = 1;
    Q[head][0] = h, Q[head][1] = w;
    memcpy(back, used, sizeof(used));
    back[h][w] = true;
    while(head < tail){
	ch = Q[head][0];
	cw = Q[head++][1];
	for(j = 0, mh = -1, mw = -1, mp = G[ch][cw]; j < 4; j++){
	    nh = ch + dh[j];
	    nw = cw + dw[j];
	    if(nh < 0 || nh >= H || nw < 0 || nw >= W)continue;
	    if(back[nh][nw])continue;
	    if(G[nh][nw] >= G[ch][cw])continue;
	    if((mh == -1 && mw == -1) || G[nh][nw] < mp){
		mh = nh, mw = nw, mp = G[nh][nw];
	    }
	}
	if(mh == -1 && mw == -1)continue;
	Q[tail][0] = mh;
	Q[tail++][1] = mw;
	back[mh][mw] = true;
    }
    sh = ch, sw = cw;
}


void solve(int H, int W)
{
    int cnt, j, k, h, w, m, size;    
    size = H * W;
    memset(used, false, sizeof(used));
    for(j = 0, cnt = 0; j < H; j++){
	for(k = 0; k < W; k++){
	    if(!used[j][k]){
		bfs(j, k, H, W, h, w);
		//printf("(%d, %d) (%d, %d)\n", j, k, h, w);
		used[h][w] = true;
		out[h][w] = 'a' + cnt;
		for(m = 0; m < size; m++){		    		    
		    if(used[m / W][m % W])continue;
		    if(F[m][h * W + w]){
			used[m / W][m % W] = true;
			out[m / W][m % W] = 'a' + cnt;
		    }
		}
		cnt++;
	    }
	}
    }
}

int main()
{
    int T, H, W, j, k, l, t;
    scanf("%d", &T);
    for(t = 1; t <= T; t++){
	memset(G, -1, sizeof(G));
	memset(out, 0, sizeof(out));
	scanf("%d%d", &H, &W);
	memset(F, false, sizeof(F));
	for(j = 0; j < H; j++){
	    for(k = 0; k < W; k++){
		scanf("%d", &G[j][k]);
	    }
	}
	for(j = 0; j < H; j++){
	    for(k = 0; k < W; k++){
		int nh, nw, mh, mw, mp;		
		for(l = 0, mh = -1, mw = -1, mp = G[j][k];
			l < 4; l++){
		    nh = j + dh[l];
		    nw = k + dw[l];
		    if(nh < 0 || nh >= H || nw < 0 || nw >= W)continue;
		    if(G[nh][nw] >= G[j][k])continue;
		    if((mh == -1 && mw == -1) || (G[nh][nw] < mp)){
			mh = nh, mw = nw, mp = G[nh][nw];
		    }
		}
		if(mh == -1 && mw == -1)continue;
		//printf("(mh, mw) = (%d, %d) => (%d, %d)\n", j, k, mh, mw);
		F[j * W + k][mh * W + mw] = true;
	    }
	}
	int size = H * W;
	for(l = 0; l < size; l++){
	    for(j = 0; j < size; j++){
		for(k = 0; k < size; k++){
		    F[j][k] |= F[j][l] & F[l][k];
		}
	    }
	}
	//for(j = 0; j < size; j++){
	    //for(k = 0; k < size; k++){
		//cout<<F[j][k]<<" ";
	    //}
	    //cout<<endl;
	//}
	printf("Case #%d:\n", t);
	solve(H, W);	
	for(j = 0; j < H; j++){
	    for(k = 0; k < W; k++){
		if(k != W - 1){
		    printf("%c ", out[j][k]);
		}
		else{
		    printf("%c\n", out[j][k]);
		}
	    }
	}
    }
    return 0;
}
