/*
  Name: a.cpp
  Author: Abhishek Dilliwal
  Date: 17/07/08 04:06
  Description: A problem in codejam 17th July 2008
*/

#include<iostream>
#include<vector>
#include<string>

using namespace std;

class engine{
public:
	string name;
	int pos;
	int count;
	engine(){
		pos=-1;
		count=0;
	}
};


void display_engine(vector<engine>& eng){
	for(int temp1=0;temp1<eng.size();temp1++){
		cout<<"Engine name: "<<eng[temp1].name<<endl;
		cout<<"Engine count: "<<eng[temp1].count<<endl;
		cout<<"Engine position: "<<eng[temp1].pos<<endl;
	}
}

void reset_eng(vector<engine>& eng){
	for(int temp1=0;temp1<eng.size();temp1++){
		eng[temp1].pos = -1;
	}
}

bool chk_zero(vector<engine>& eng){
	for(int i=0;i<eng.size();i++){
		if(eng[i].pos==-1){
			return true;
		}
	}
	return false;
}

void sort_eng(vector<engine>& eng){
	int i,j;
	for(i=0;i<eng.size();i++){
		for(j=i+1;j<eng.size();j++){
			if(eng[i].pos < eng[j].pos){
				engine t;t=eng[i];eng[i]= eng[j];eng[j] = t;
			}
		}
	}
}

int return_pos(vector<string>& que, int t, vector<engine>& eng){
	reset_eng(eng);
	for(int temp = t; temp<que.size() ; temp++){
		for(int i = 0; i< eng.size(); i++){
			if(eng[i].name == que[temp] && eng[i].pos == -1){
				eng[i].pos = temp;
			}
		}
	}
	sort_eng(eng);
	if(chk_zero(eng))
		return -1;
	return eng[0].pos;
}

void give_pos(vector<string>& que, vector<engine>& eng){
	for(int temp = 0; temp<que.size() ; temp++){
		for(int i = 0; i< eng.size(); i++){
			if(eng[i].name == que[temp] && eng[i].pos == -1){
				eng[i].pos = temp;
			}
		}
	}
}

int main(){
	int i, N;
	
	cin>>N;
	for(i=0;i<N;i++){
		int S, Q;
		cin>>S;
		vector <engine> eng;
		vector <string> que;
		cin.get();
		for(int j=0;j<S;j++){
			engine e;
			getline(cin,e.name);
			eng.push_back(e);
		}
		cin>>Q;
		cin.get();
		for(int k=0;k<Q;k++){
			string q;
			getline(cin,q);
			que.push_back(q);
		}
		//give_pos(que,eng);
		//if(chk_zero(eng)){
		//	cout<<"Case #"<<i+1<<": 0\n";
		//	continue;
		//}
		int change = 0;
		for(int t=0;t<que.size();){
			
			t = return_pos(que,t,eng);
			if(t==-1) break;
			change++;
			
		}
		cout<<"Case #"<<i+1<<": "<<change<<"\n";
	}
	return 0;
}
