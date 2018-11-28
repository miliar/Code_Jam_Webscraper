#include<iostream>
#include<cassert>
#include<string.h>
using namespace std;

const int MAXNA = 102;
const int MAXNB = 102;
int NC;
int N[2];
int T;
int min0, min1;
struct train{
	int f;
	int b;
};
train TR[2][MAXNA];
int pos[2];
bool tag[2][MAXNA];
int num[2];

int cmp(const void* va, const void* vb){
	train * a = (train*)va;
	train * b = (train*)vb;
	int comp = a->f - b->f;
	if(comp == 0)
		comp = a->b - b->b;
	return comp;
}

int get_time(){
	int h,m;
	cin>>h;
	char c = cin.get();
	assert(c == ':');
	cin>>m;
	return h*60 + m;
}

void get_train(train &tr){
	tr.f = get_time();
	tr.b = T + get_time();
}

void init(){
	cin>>T;
	cin>>N[0]>>N[1];
	for(int i=0; i<2; i++){
		for(int j=0; j<N[i]; j++){
			get_train(TR[i][j]);
			tag[i][j] = false;
		}
		qsort(TR[i], N[i], sizeof(train), cmp);
		pos[i] = 0;
		num[i] = 0;
	}
	min0 = min1 = 25*60;
}

void get_pos(){
	for(int i=0; i<2; i++){
		while(pos[i] < N[i] && tag[i][pos[i]])
			pos[i] ++;
	}
}
 
void search();
void dfs(int from, int p, int end){
	tag[from][p] = true;
	int to = 1 - from;
	int i;
	for(i=0; i<N[to]; i++){
		if(!tag[to][i] && TR[to][i].f >= end)
			break;
	}

	if(i < N[to])
		dfs(to, i, TR[to][i].b);
	else
		search();
}

void search(){
	int from;
	
	get_pos();
	if(pos[0] >= N[0] && pos[1] >= N[1])
		return;

	if(pos[0] >= N[0])
		from = 1;
	else if(pos[1] >= N[1])
		from = 0;
	else{
		if(cmp(&TR[0][pos[0]], &TR[1][pos[1]]) <= 0)
			from = 0;
		else
			from = 1;
	}

	num[from] ++;
	dfs(from, pos[from],  TR[from][pos[from]].b);
}

int main(){
	cin>>NC;
	for(int i=1; i<=NC; i++){
		init();
		search();
		cout<<"Case #"<<i<<": "<<num[0]<<" "<<num[1]<<endl;
	}
	return 0;
}
