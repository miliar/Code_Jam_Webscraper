//code by Carlo Piovesan
//GCJ 2009, qualification Round, problem B

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

////DISJOINT SET DATA STRUCTURE
vector <int> P;
vector <int> R;
void create_set(int x) {
	P[x]=x;
	R[x]=0;
	}
int find_set(int x) {
	int q=0;
	int a=x;
	while (a!=P[a]) a=P[a];
	int b=x;
	int c=x;
	while (b!=P[b]) {
		c=P[c];
		P[b]=a;
		b=c;
		}
	return a;
	}
void merge_sets(int x, int y) {
	int PX=find_set(x);
	int PY=find_set(y);
	if (PX==PY) return;
	if (R[PX]>R[PY]) P[PY]=PX;
	else P[PX]=PY;
	if (R[PX]==R[PY]) R[PY]++;
	}
void merge_sets_whitout_rank(int x, int y) {
	int PX=find_set(x);
	int PY=find_set(y);
	if (PX==PY) return;
	P[PY]=PX;
	if (R[PX]==R[PY]) R[PY]++;
	}

int dh[5]={0, -1, 0, 0, 1};
int dw[5]={0, 0, -1, 1, 0};

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		//input
		int H,W;
		FILE>>H>>W;
		vector < vector <int> > A(H+2, vector <int> (W+2, 20000));
		for (int h=1; h<=H; h++) for (int w=1; w<=W; w++) FILE>>A[h][w];
		
		//inizialize disjoint set data structure
		vector < vector <int> > CODE(H+2, vector <int> (W+2));
		for (int h=0; h<=H+1; h++) for (int w=0; w<=W+1; w++) CODE[h][w]=h*(W+2)+w+100;
		P.resize((W+2)*(H+2)+100);
		R.resize((W+2)*(H+2)+100);
		for (int h=0; h<=H+1; h++) for (int w=0; w<=W+1; w++) create_set(CODE[h][w]);
		
		//merge two basin when needed
		for (int h=1; h<=H; h++) for (int w=1; w<=W; w++) {
			int BEST=30000, DIR=-1;
			for (int i=0; i<5; i++) if (A[h+dh[i]][w+dw[i]]<BEST) {
				BEST=A[h+dh[i]][w+dw[i]];
				DIR=i;
				}
			merge_sets(CODE[h][w], CODE[h+dh[DIR]][w+dw[DIR]]);
			}
		
		//find the currect labelling
		int CURR=0;
		for (int i=0; i<26; i++) create_set(i);
		for (int h=1; h<=H; h++) for (int w=1; w<=W; w++) if (find_set(CODE[h][w])>50) {
			merge_sets_whitout_rank(CURR, CODE[h][w]);
			CURR++;
			}
		
		//output
		OUT<<"Case #"<<z<<":\n";
		for (int h=1; h<=H; h++) {
			OUT<<(char)('a'+find_set(CODE[h][1]));
			for (int w=2; w<=W; w++) OUT<<" "<<(char)('a'+find_set(CODE[h][w]));
			OUT<<"\n";
			}
        	}
    FILE.close();
    OUT.close();
    return 0;
    }
