#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <deque>
#include <vector>
using namespace std;

void update_pos(int &,int);

int main(){
	int T=0,N=0;
	freopen("BotTrust.in","r",stdin);
	freopen("BotTrust.out","w",stdout);
	cin>>T;
	for(int Case=0;Case<T;++Case){
		cin>>N;
		string order="";
		queue<int>orange;
		queue<int>blue;
		string moves="";
		for(int i=0;i<N;++i){
			char P;
			int R=0;
			cin>>P>>R;
			if(P=='O')orange.push(R);
			else blue.push(R);
			moves+=P;
		}
		int cur=0,time=0;
		int A=1,B=1;
		int a=1,b=1;
		if(!orange.empty()){
			a=orange.front();
			orange.pop();
		}
		if(!blue.empty()){
			b=blue.front();
			blue.pop();
		}
		while(cur<N){
			char c = moves[cur];
			if(c=='O'){
				if(A==a){
					cur++;
					time++;
					if(!orange.empty()){
						a=orange.front();
						orange.pop();
					}
					update_pos(B,b);
				}
				else{
					update_pos(A,a);
					update_pos(B,b);
					time++;
				}	
			}
			if(c=='B'){
				if(B==b){
					cur++;
					time++;
					if(!blue.empty()){
						b=blue.front();
						blue.pop();
					}
					update_pos(A,a);
				}
				else{
					update_pos(A,a);
					update_pos(B,b);
					time++;
				}
			}
		}
		cout<<"Case #"<<Case+1<<": "<<time<<endl;
	}
	return 0;
}
void update_pos(int & a, int b){
	if(a<b)a++;
	else if(a>b)a--;
	else if(a==b)a=b;
}