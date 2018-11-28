#include <iostream>
#include <list>
using namespace std;

int main(){
	int pos[2];
	list<int> button[2];
	list<bool> turn;
	int t;
	cin>>t;
	for(int case_num=1; case_num<=t; case_num++){
		// cerr<<"-- #"<<case_num<<" --"<<endl;
		pos[0]=1; pos[1]=1;
		button[0].clear(); button[1].clear();
		turn.clear();
		
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			char c;
			bool is_blue;
			int button_pos;
			cin>>c;
			if(c=='O'){is_blue=0;}else{is_blue=1;}
			cin>>button_pos;
			button[is_blue].push_back(button_pos);
			turn.push_back(is_blue);
		}

		int count=0;
		list<int>::const_iterator next[2];
		list<bool>::const_iterator in_turn=turn.begin();
		next[0]=button[0].begin(); next[1]=button[1].begin();
		bool is_operated[2];
		while(in_turn!=turn.end()){
			count++;
			is_operated[0]=false; is_operated[1]=false;

			if(!is_operated[*in_turn]&&*next[*in_turn]==pos[*in_turn]){
				// push button
				next[*in_turn]++;
				is_operated[*in_turn]=true;
				// cerr<<count<<"> "<<*in_turn<<": "<<"push "<<pos[*in_turn]<<endl;

				in_turn++;
				if(in_turn==turn.end())break;
			}

			if(!is_operated[*in_turn]&&*next[*in_turn]!=pos[*in_turn]){
				// move to next
				int diff=*next[*in_turn]-pos[*in_turn];
				if(diff>0){pos[*in_turn]++;}
				else{pos[*in_turn]--;}
				is_operated[*in_turn]=true;
				// cerr<<count<<"> "<<*in_turn<<": "<<"move "<<pos[*in_turn]<<endl;
			}

			if(!is_operated[!*in_turn]&&next[!*in_turn]!=button[!*in_turn].end()&&*next[!*in_turn]!=pos[!*in_turn]){
				// the other's move
				int diff=*next[!*in_turn]-pos[!*in_turn];
				if(diff>0){pos[!*in_turn]++;}
				else{pos[!*in_turn]--;}
				is_operated[!*in_turn]=true;
				// cerr<<count<<"> "<<!*in_turn<<": "<<"move "<<pos[*in_turn]<<endl;
			}
		}
		cout<<"Case #"<<case_num<<": "<<count<<endl;
		// cerr<<endl;
	}
	return 0;
}