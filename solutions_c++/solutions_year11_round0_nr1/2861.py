#include<stdio.h>
#include<iostream>
#include<sstream>
#include<vector>
#include<math.h>
//#include<pair>

using namespace std;

class BotTrust1{
public:
	string getTime(vector< vector< pair<char,int> > > v){
		int i;
		stringstream out(stringstream::in | stringstream::out);
		for(i=0;i<v.size();i++)
			out << "Case #" <<  (i+1) <<  ": " << getEach(v[i]) << "\n";
		cout <<out.str();
		return out.str();
	}
	int getEach(vector< pair<char,int> >v){
		int i,time=0,ia=0,ib=0,apos=1,bpos=1,arep=0,brep=0;
		vector< int >a,b;
		for(i=0;i<v.size();i++){
			move(time, apos, bpos, arep, brep, v,i);
		}
		//cout << "time: " << time << endl;
		return time;
	}
	void move(int &time, int &apos, int &bpos, int &arep, int &brep, vector< pair<char,int> >v, int cur){
		if(cur < v.size()){
			if(v[cur].first == 'O'){
				if(arep >= abs(v[cur].second-apos)){	
					brep++;
					time++;
				}
				else{
					brep += abs(v[cur].second - apos) - arep + 1;
					time += abs(v[cur].second - apos) - arep + 1;
				}
				arep = 0;
				apos = v[cur].second;
				//cout << "move: time: " << time << endl;
			}
			else if(v[cur].first == 'B'){
				if(brep >= abs(v[cur].second-bpos) ){	
					arep++;
					time++;
				}
				else{
					arep += abs(v[cur].second - bpos) - brep +1;
					time += abs(v[cur].second - bpos) - brep +1;
				}
				brep = 0;
				bpos = v[cur].second;
				//cout << "move: time: " << time << endl;
			}
		}

	}
	int getNext(vector< int >v, int index){	return index >= v.size()-1? index:index+1;}

	/*vector< int >getTask(vector< pair<char,int> >v, char target){
		int i;
		vector<int >out;
		for(i=0;i<v.size();i++)
			if(v[i].first == target)
				out.push_back(v[i].second);
		printSingle(out, target);
		return out;
	}
	
	 void printSingle( vector< int > v, char target){
		cout << "target:" << target << " ";
		int i;
		for(i=0;i<v.size();i++)
			cout << v[i] << " ";
		cout <<endl;
	 }*/
};


 void getContent(vector< vector< pair<char,int> > > &v){
	int cases,i,j, steps, button;
	char robot;

	scanf("%d\n", &cases);
	for(i=0;i<cases;i++){
		scanf("%d\n", &steps);	
		vector< pair<char,int> >task;
		for(j=0;j<steps;j++){
			scanf("%c %d", &robot,&button);	
			scanf("\n");	
			pair<char,int>p(robot, button);
			task.push_back(p);
		}
		v.push_back(task);
	}
}

 /*void print(vector< vector< pair<char,int> > > v){
	int i,j;
	for(i=0;i<v.size();i++){
		cout << i<<endl;
		for(j=0;j<v[i].size();j++)
			cout << v[i][j].first << " " << v[i][j].second <<" ";
		cout << endl;
	}
 }*/
void main(int argc, char *argv[]){
	vector< vector< pair<char,int> > > v;
	getContent(v);
	BotTrust1 *bt = new BotTrust1();
	string out = bt->getTime(v);
}