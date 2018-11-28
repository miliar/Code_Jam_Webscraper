#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("GCJ P A.in");
ofstream fout("GCJ P A.out");

#define cin fin
#define cout fout

int targetO[101],targetB[101];
bool Ot[101];
int n;
int On,Bn;
int t;

void init(){
	cin >> n;
	On=Bn=0;
	char p;
	int s;
	for(int i=0;i<n;i++){
		cin >> p >> s;
		if(p=='O'){
			Ot[i]=true;
			targetO[On++]=s;
		}else{
			Ot[i]=false;
			targetB[Bn++]=s;
		}
	}
}

void process(){
	int Opos=1,Bpos=1;
	int Os=0,Bs=0;
	int tn=0;
	int ans=0;
	while(tn<n){
		ans++;
		bool push=false;
		if(Os<On)
			if(Opos<targetO[Os])
				Opos++;
			else if(Opos>targetO[Os])
				Opos--;
			else if(Ot[tn]){
				Os++;
				push=true;
			}

		if(Bs<Bn)
			if(Bpos<targetB[Bs])
				Bpos++;
			else if(Bpos>targetB[Bs])
				Bpos--;
			else if(!Ot[tn]){
				Bs++;
				push=true;
			}
		if(push)
			++tn;
	}
	cout << ans << endl;
}

int main(){
	cin >> t;
	for(int i=0;i<t;i++){
		cout << "Case #" << i+1 << ": ";
		memset(targetO,0,sizeof(targetO));
		memset(targetB,0,sizeof(targetB));
		init();
		process();
	}
	return 0;
}