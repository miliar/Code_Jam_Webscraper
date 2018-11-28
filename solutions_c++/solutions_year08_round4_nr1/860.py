#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <utility> 

// container 
#include <vector> 
#include <string> 
#include <set> 
#include <map> 
#include <stack>
#include <queue>

// C-style 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <climits>
#include <cfloat>
#include <cassert>

using namespace std;

#define FOR(_I,_A,_B) for(int _I=(_A);(_I)<(_B);_I++)
#define FORE(_I,_A,_B) for(int _I=(_A);(_I)<=(_B);_I++) 
#define REP(_I,_B) for(int _I=(0);(_I)<(_B);_I++) 

typedef long long ll;
typedef long double ld;

int d[10000+1][2][2];
int t[10000+1];
int c[10000+1];
int v[10000+1];
int N, M, V;

int get(int node, int value, int type) {
	// ��� ���� ������
	if(node>M) return -1;
	// ���� �ִ� ���̸�
	if(d[node][value][type]!=-2) 
		return d[node][value][type];
	// �ٲ� �� ������
	if(!c[node] && type != t[node]) 
		return d[node][value][type]=-1;	
	// �ϴ� original�� ��� �� �� ������
	if(value == v[node]) 
		return d[node][value][type]=0;
	
	// original�� ��� ���� �Ф�
	// �׷��� �ؿ� �ֵ��� �ٲ㼭 ��� �����Ѱ�?
	// �׷��� ���� �����ָ� 
	int res=-1;
	if(type==1) {  // and 
		if(value==1) { // value = 1
			// �Ѵ� 1
			REP(i, 2) REP(j, 2) {
				int l = get(2*node, 1, i);
				int r = get(2*node+1, 1, j);
				if(l!=-1 && r!=-1) {
					if(res!=-1) {
						res = min(res, l+r);
					}
					else res = l+r;
				}
			}
		}
		else { // value = 0 
			// ���� �ϳ��� 0;
			REP(i, 2) {
				int l = get(2*node, 0, i);
				if(l!=-1) {
					if(res!=-1) res = min(res, l);
					else res = l;
				}
			}

			REP(i, 2) {
				int l = get(2*node+1, 0, i);
				if(l!=-1) {
					if(res!=-1) res = min(res, l);
					else res = l;
				}
			}
		}
	}
	else { // or
		if(value==1) { // value = 1
			// ���� �ϳ��� 1;
			REP(i, 2) {
				int l = get(2*node, 1, i);
				if(l!=-1) {
					if(res!=-1) res = min(res, l);
					else res = l;
				}
			}

			REP(i, 2) {
				int l = get(2*node+1, 1, i);
				if(l!=-1) {
					if(res!=-1) res = min(res, l);
					else res = l;
				}
			}
		}
		else { // value = 0
			// �Ѵ� 0;
			REP(i, 2) REP(j, 2) {
				int l = get(2*node, 0, i);
				int r = get(2*node+1, 0, j);
				if(l!=-1 && r!=-1) {
					if(res!=-1) {
						res = min(res, l+r);
					}
					else res = l+r;
				}
			}
		}
	}

	if(t[node]!=type&&res!=-1) {
		return res+1;
	}
	else return res;
}

int main(void) {
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);

	cin >> N;
	FORE(tc, 1, N) {
		memset(c, 0, sizeof(c));
		memset(v, 0, sizeof(v));
		memset(t, 0, sizeof(t));

		scanf("%d %d", &M, &V);
		FORE(i, 1, M) d[i][0][0]=d[i][1][0]=d[i][0][1]=d[i][1][1]=-2;

		FORE(i, 1, (M-1)/2) {
			int G, C;
			scanf("%d %d", &G, &C);
			if(G==1) t[i]=1;
			else t[i]=0;
			if(C==1) c[i]=1;
			else c[i]=0;
		}

		memset(v, -1, sizeof(v));
		REP(i, (M+1)/2) {
			scanf("%d", &v[M+1-(M+1)/2+i]);
		}
		
		for(int i=M;i>=1;i--) {
			if(v[i]!=-1) continue;
			if(t[i]==1) { // AND
				v[i] = v[2*i]&v[2*i+1];
			}
			else { // OR
				v[i] = v[2*i]|v[2*i+1];
			}
		}

		int res1 = get(1, V, 0);
		int res2 = get(1, V, 1);
		
		if(res1==-1 && res2==-1) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else if(res1==-1) {
			printf("Case #%d: %d\n", tc, res2);
		}
		else if(res2==-1) {
			printf("Case #%d: %d\n", tc, res1);
		}
		else {
			printf("Case #%d: %d\n", tc, min(res1, res2));
		}
	}
	return 0;
}
