#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <vector>

#define POS(x,y) ((x)*MAX + (y))
#define X(p) ((p)/MAX)
#define Y(p) ((p)%MAX)
#define SUP(x) ((x)*MAX*MAX)
#define SDOWN(x) ((x)/(MAX*MAX))
#define MOD(n) (((n)+MODN)%MODN)

using namespace std;

int nTestCases;
int testCase;
long long ans;

int const MAX = 1100;
int R;
long long X1[MAX], X2[MAX], Y1[MAX], Y2[MAX];
vector<int> edge[MAX];
bool visited[MAX];
long long ptop, pleft, pright, pbottom;


void DFS(int i){
  visited[i] = true;

  if(X1[i]+Y1[i] < ptop+pleft){
	ptop = X1[i];  pleft = Y1[i];
  }

  if(X2[i] > pbottom)
	pbottom = X2[i];
  if(Y2[i] > pright)
	pright = Y2[i];

  for(int idx=0; idx<edge[i].size(); idx++){
	if(visited[edge[i][idx]]==false){
	  DFS(edge[i][idx]);
	}
  }
}


inline bool run(){
  memset(visited, false, sizeof(visited));
  ans = 0;
  for(int i=0; i<R; i++) if(visited[i] == false){
	ptop = 10000000;
	pleft = 10000000;
	pright = -1;
	pbottom = -1;
	DFS(i);
	ans = max(ans, (pbottom+pright-(ptop+pleft)+1));
  }
  return true;
}

inline bool connected(int i, int j){
  long long pt = X1[i]; long long pl = Y1[i]; long long pb = X2[i]; long long pr = Y2[i];
  if(pt > X1[j]) pt = X1[j];
  if(pl > Y1[j]) pl = Y1[j];
  if(pb < X2[j]) pb = X2[j];
  if(pr < Y2[j]) pr = Y2[j];

  if((abs(X1[i]-X2[i])+abs(X1[j]-X2[j])+2 >= pb-pt+1) &&
	(abs(Y1[i]-Y2[i])+abs(Y1[j]-Y2[j])+2 > pr-pl+1))
	return true;

  if((abs(X1[i]-X2[i])+abs(X1[j]-X2[j])+2 > pb-pt+1) &&
	(abs(Y1[i]-Y2[i])+abs(Y1[j]-Y2[j])+2 >= pr-pl+1))
	return true;

  if(X1[i] == X2[j]+1 && Y2[i]+1 == Y1[j]) 
	return true;  

  if(X1[j] == X2[i]+1 && Y2[j]+1 == Y1[i])
	return true;

  return false;
}

inline void init(){
  for(int i=0; i<MAX; i++)
	edge[i].clear();

  cin >> R;
  for(int r=0; r<R; r++)
	cin >> X1[r] >> Y1[r] >> X2[r] >> Y2[r];

  for(int i=0; i<R; i++) for(int j=i+1; j<R; j++) 
	if(connected(i, j)){
	  edge[i].push_back(j);
	  edge[j].push_back(i);
	}
}

void main()
{
  FILE *fin, *fout;
  fin = freopen("z:\\input.txt", "r", stdin);
  fout = freopen("z:\\output.txt", "w", stdout);

  scanf("%d", &nTestCases);

  for(testCase = 1; testCase <= nTestCases; testCase++){
	init();
	
	run();

	printf("Case #%d: %d\n", testCase, ans);
  }

  fflush(fout);
  fclose(fin);
  fclose(fout);
}