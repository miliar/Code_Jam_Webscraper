#include <iostream>
using namespace std;
int T, H, W, A[100][100], S[100][100];
char name, table[100*100];
void find(int& alt, int h, int w, int& nh, int& nw)
{
    if (h < 0 || h >= H || w < 0 || w >= W) return;
    if (A[h][w] >= alt) return;
    alt = A[h][w];
    nh = h, nw = w;
}
int flow(int h, int w)
{
    if (S[h][w] >= 0) return S[h][w];
    int next = A[h][w], nh = h, nw = w;
    find(next, h-1, w, nh, nw);
    find(next, h, w-1, nh, nw);
    find(next, h, w+1, nh, nw);
    find(next, h+1, w, nh, nw);
    if (nh == h && nw == w) {
	S[h][w] = h*100+w;
	table[h*100+w] = name++;
	return h*100+w;
    }
    return S[h][w] = flow(nh, nw);
}
int main()
{
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> H >> W;
	for (int h=0; h<H; ++h)
	    for (int w=0; w<W; ++w) 
		cin >> A[h][w];
	fill(&S[0][0], &S[99][99]+1, -1);
	name = 'a';
	cout << "Case #" << t+1 << ":" << endl;
	for (int h=0; h<H; ++h) {
	    for (int w=0; w<W; ++w) {
		flow(h, w);
		if (w) cout << ' ';
		cout << table[S[h][w]];
	    }
	    cout << endl;
	}
    }    
}
