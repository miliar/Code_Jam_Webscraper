#include <iostream>
#include <queue>

using namespace std;

int main(){
	int i=0, n;
	cin >> n;
	while(++i<=n){
		int j, posO=1, posB=1, buf, step = 0;
		char robot;
		queue<int> qO, qB;
		queue<bool> qForO;
		cin >> j;
		while(--j>=0){
			cin >> robot >> buf;
			if(robot=='O'){
				qO.push(buf);
				qForO.push(true);
			}else{
				qB.push(buf);
				qForO.push(false);
			}
		}
		while(qForO.size()>0){
			bool pushed=false;
			step++;
			if(qO.size()>0){
				if(qO.front()>posO){
					posO++;
				}
				else if(qO.front()<posO){
					posO--;
				}else if(qForO.front()){
					qO.pop();
					qForO.pop();
					pushed=true;
				}
			}
			if(qB.size()>0){
				if(qB.front()>posB){
					posB++;
				}
				else if(qB.front()<posB){
					posB--;
				}else{
					if(!qForO.front()&&!pushed){
						qB.pop();
						qForO.pop();
					}
				}
			}
			//cout << step <<"," <<posO << "," << posB << endl;
		}
		cout << "Case #" << i << ": " << step << endl;
	}
	return 0;
}