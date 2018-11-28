#include <iostream>
#include<queue>
#include<cstdio>
using namespace std;

void move(int &p,int target){//&para poder modificar el p original
    if(target>p)p++;
    else if(target<p)p--;
    //caso contrario dejarlo asi ;)
}

int main() {

	int T;
	cin>>T;
	int k = 1;
	while(T--){
		int pO = 1;
		int pB = 1;
		int N;
		cin>>N;
		queue<int> O;
		queue<int> B;
		string orden;

		while(N--){
			char c;
			int t;
			cin>>c>>t;
			if(c=='B')
				B.push(t);
			if(c=='O')
				O.push(t);
			orden+=c;
		}
		//
		int sec = 0;
		//cout<<orden<<endl;
		for(int i = 0;i<orden.size();i++){
			if(orden[i]=='B'){

				while(pB!=B.front()){
					sec++;
					move(pB,B.front());
					if(!O.empty()){
						move(pO,O.front());
					}
				}
				sec++;
				B.pop();
				if(!O.empty()){
                    move(pO,O.front());
                }
			}
			else{
				while(pO!=O.front()){
					sec++;
					move(pO,O.front());
					if(!B.empty()){
						move(pB,B.front());
					}
				}
				O.pop();
				sec++;
				if(!B.empty()){
                    move(pB,B.front());
                }
			}
			//cout<< pO << endl;
			//cout << pB << endl;
		}
		printf("Case #%d: %d\n",k++,sec);
		//cout<<sec<<endl;Case #1: 6
	}


	return 0;
}
