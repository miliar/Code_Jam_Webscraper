#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
using namespace std;
unsigned char per[ 31 * 2 ][3] = { 
{0,0,0}, {0,0,0},//0
{1,0,0}, {1,0,0},//1
{1,1,0}, {2,0,0},//2
{1,1,1}, {2,1,0},//3
{2,1,1}, {2,1,1},//4
{2,2,1}, {3,1,1},//5
{2,2,2}, {3,2,1},//6
{3,2,2}, {3,2,2},//7
{3,3,2}, {4,2,2},//8
{3,3,3}, {4,3,2},//9
{4,3,3}, {4,3,3},//10
{4,4,3}, {5,3,3},//11
{4,4,4}, {5,4,3},//12
{5,4,4}, {5,4,4},//13
{5,5,4}, {6,4,4},//14
{5,5,5}, {6,5,4},//15
{6,5,5}, {6,5,5},//16
{6,6,5}, {7,5,5},//17
{6,6,6}, {7,6,5},//18
{7,6,6}, {7,6,6},//19
{7,7,6}, {8,6,6},//20
{7,7,7}, {8,7,6},//21
{8,7,7}, {8,7,7},//22
{8,8,7}, {9,7,7},//23
{8,8,8}, {9,8,7},//24
{9,8,8}, {9,8,8},//25
{9,9,8}, {10,8,8},//26
{9,9,9}, {10,9,8},//27
{10,9,9}, {10,9,9},//28
{10,10,9}, {10,10,9},//29
{10,10,10}, {10,10,10}//30
};

priority_queue<int> pq;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N, T, S, p, num;
	scanf("%d", &N);
	for(int n=0;n<N;++n){
		scanf("%d %d %d", &T, &S, &p);

		pq = priority_queue<int>();
		for(int t=0;t<T;++t){
			scanf("%d", &num);
			pq.push(num);
		}
		int cont = 0;
		while(!pq.empty()){
			int val = pq.top();pq.pop();
			int minA = per[val*2][0];
			if(minA>=p){
				//printf("Min(%d) %d %d %d\n", val, per[val*2][0], per[val*2][1], per[val*2][2]);
				cont++;
				continue;
			}
			int minB = per[val*2+1][0];
			if(S>0 && minB>=p){
				//printf("Max(%d-%d) %d %d %d\n", val,S, per[val*2+1][0], per[val*2+1][1], per[val*2+1][2]);
				cont++;
				S--;
				continue;
			}else break;
			//printf("%d ", pq.top());
		}
		printf("Case #%d: %d\n", n+1, cont);
	}

}