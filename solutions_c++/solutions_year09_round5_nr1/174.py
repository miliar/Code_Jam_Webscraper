#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;

typedef vector<int> IV;
typedef pair<int,int> PI;
typedef vector<pair<int,int> > IVP;
#define MP(a, b) make_pair((a), (b))

const int MOD = 178127;
struct Node{
	Node *next;
	int id, s, f;
	Node(){}
	Node(Node* _next, int _id, int _s, int _f):next(_next), id(_id), s(_s), f(_f){}
}buff[MOD*10], *head[MOD];

IVP ivp[MOD*10];
int R, C, ID, pt;
char mp1[16][16],mp2[16][16],mp3[16][16],mp4[16][16], mp[16][16];
void init(){
	pt = 0;
	memset(head, 0, sizeof(head));
}
int hash(IVP &tiv){
	int t = 1, res = 0;
	for(int i = 0; i < tiv.size(); ++i){
		res += (tiv[i].first*C+tiv[i].second)*t;
		t *= 10;
	}
	return res%MOD;
}
int Find(int h, IVP &tiv){
	for(Node *p = head[h]; p; p = p->next)
		if(tiv == ivp[p->id])return 1;
	return 0;
}
int Insert(int h, IVP &tiv, int s, int f){
	buff[pt] = Node(head[h], ID, s, f);
	head[h] = &buff[pt++];
	ivp[ID++] = tiv;
}
int valid(int r, int c){
	return (r>=0 && r<R && c>=0 && c < C && mp[r][c] != '#');
}
int in_iv(PI pi, IVP &tiv){
	for(int i = 0; i < tiv.size(); ++i)if(pi == tiv[i])return 1;
	return 0;
}
int dir[4][2] = {{0,1}, {-1,0},{0,-1},{1,0}};
//int q[MOD*10];
IVP siv, eiv;
int judge(IVP &tiv){
	int vis[16];
	memset(vis, 0, sizeof(vis));
	vis[0] = 1;
	for(int i = 0; i < tiv.size(); ++i){
		if(vis[i]){
			for(int j = 0; j < tiv.size(); ++j)
				if((tiv[i].first == tiv[j].first && abs(tiv[i].second-tiv[j].second) == 1) 
					|| (tiv[i].second == tiv[j].second && abs(tiv[i].first-tiv[j].first) == 1) )
					vis[j] = 1;
		}
	}
	for(int i = 0; i < tiv.size(); ++i)if(!vis[i])return 0;
	return 1;
}
int bfs(){
	if(siv == eiv)return 0;
	int qs, qe, nr1, nc1, nr2, nc2, d, k, h,f;
	int r, c, s;
	qs = 0, qe = 1;
	init();	ID = 0;
	h = hash(siv);	Insert(h, siv, 0, 1);//buff[0] = Node(head[h], 0, 0, 1);
	//ivp[0] = siv;
	while(qs < qe){
		IVP iv1, iv2;
		iv1 = ivp[qs];
	//	cout<<"qs qe "<<qs<<' '<<qe<<endl;
	//	for(int i = 0; i < iv1.size(); ++i)cout<<iv1[i].first<<' '<<iv1[i].second<<endl;
	//	cout<<endl;
		if(iv1 == eiv)return buff[qs].s;
		for(int i = 0; i < iv1.size(); ++i){
			r = iv1[i].first, c = iv1[i].second;
			for(int j = 0; j < 2; ++j){
				nr1 = r+dir[j][0], nc1 = c + dir[j][1];
				nr2 = r+dir[j+2][0], nc2 = c + dir[j+2][1];
				if(!valid(nr1, nc1) || !valid(nr2, nc2))continue;
			//	if(mp[nr1][nc1] == '#' || mp[nr2][nc2] == '#')continue;
				if(in_iv(make_pair(nr1, nc1), iv1) || in_iv(make_pair(nr2, nc2), iv1))continue;
				
				iv2 = iv1;
				iv2[i] = make_pair(nr1, nc1); sort(iv2.begin(), iv2.end());
				h = hash(iv2);
				f = judge(iv2);
				if(buff[qs].f+f > 0 && !Find(h, iv2)){
					Insert(h, iv2, buff[qs].s+1, f);	++qe;
				}					
				iv2 = iv1;
				iv2[i] = make_pair(nr2, nc2); sort(iv2.begin(), iv2.end());
				h = hash(iv2);
				f = judge(iv2);
				if(buff[qs].f+f > 0 && !Find(h, iv2)){
					Insert(h, iv2, buff[qs].s+1, f);	++qe;
				}
			}
		}
		++qs;
	}
	return -1;
}			
				
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T, N, i, j, k;
	cin>>T;
	for(int t = 1; t <= T; ++t){
		cin>>R>>C;
		siv.clear();	eiv.clear();
		for(int i = 0; i < R; ++i){
			cin>>mp[i];
			for(int j = 0; j < C; ++j){
				if(mp[i][j] == 'o')
					siv.push_back(make_pair(i, j));
				else if(mp[i][j] == 'x')
					eiv.push_back(make_pair(i, j));
				else if(mp[i][j] == 'w'){
					eiv.push_back(make_pair(i, j));
					siv.push_back(make_pair(i, j));
				}
			}
		}
		sort(siv.begin(), siv.end());	sort(eiv.begin(), eiv.end());
		cout<<"Case #"<<t<<": "<<bfs()<<endl;
	}
	return 0;
}
