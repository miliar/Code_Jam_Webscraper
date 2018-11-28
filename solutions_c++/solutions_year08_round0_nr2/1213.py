#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int d;

int turn,na,nb;

struct trip{
	bool sta;
	int cz;
};

int arv[2][65*65+500];
vector<trip> dep[65*65+500];

inline int g(){
	int w=0;
	char c;
	while(c=getchar(),c<'0' || c>'9');
	w=c-'0';
	while(c=getchar(),c>='0' && c<='9'){
		w=10*w+c-'0';
	}
	return w;
}

void alg(int c){
	for(int i=0;i<2;i++) for(int j=0;j<24*60;j++) arv[i][j]=0;
	for(int i=0;i<24*60;i++) dep[i].clear();
	turn=g();
	na=g();
	nb=g();
	for(int i=0;i<na;i++){
		int a=g(),b=g(),c=g(),d=g();
		trip cur;
		cur.sta=true;
		cur.cz=(c-a)*60+d-b;
		dep[a*60+b].push_back(cur);
	}
	for(int i=0;i<nb;i++){
		int a=g(),b=g(),c=g(),d=g();
		trip cur;
		cur.sta=false;
		cur.cz=(c-a)*60+d-b;
		dep[a*60+b].push_back(cur);
	}
	int wa=0,wb=0;
	int ca=0,cb=0;
	for(int i=0;i<24*60;i++){
		ca+=arv[0][i];
		cb+=arv[1][i];
		for(int j=0;j<dep[i].size();j++){
			if(dep[i][j].sta){
				if(!ca)
					++wa;
				else --ca;
				++arv[1][i+dep[i][j].cz+turn];
			}else{
				if(!cb)
					++wb;
				else --cb;
				++arv[0][i+dep[i][j].cz+turn];
			}
		}
	}
	printf("Case #%d: %d %d\n",c,wa,wb);
}

int main(){
	d=g();
	for(int i=1;i<=d;i++) alg(i);
}
