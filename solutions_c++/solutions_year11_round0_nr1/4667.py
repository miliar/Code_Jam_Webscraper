#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

struct Move{
	bool orange;
	unsigned char to;
};

int getnext(vector<Move> moves,bool orange){
	for(int i = 0; i < moves.size(); i++){
		if(moves[i].orange == orange)
			return i;
	}
	return -1;
}

int main(int argc, char **argv){
	if(argc <=1){
		//cout<<"Needs 1 paramtre (the file)"<<std::endl;
		return 1;
	}
	// read the input
	ifstream file;
	vector<vector<Move> > moves;
	file.open(argv[1]);
	if(!file.is_open()){
		//cout<<"Can't open the file"<<std::endl;
		return 2;
	}
	string b;
	getline(file,b);
	stringstream ss2(b);
	int count;
	ss2 >> count;
	moves.resize(count);
	// parse file
	int _case = 0;
	while(!file.eof()){

		string line;
		bool i = true;
		unsigned char to;
		bool orange;
		int movez;
		
		getline(file,line);
		//cout << line <<std::endl;
		stringstream ss(line);
		ss >> movez; // ignore the number...
		while(ss){
			if(i){
				ss >> to;
				i = !i;
			} else {
				ss >> movez;
				Move move;
				move.orange = (to == 'O');
				move.to = movez;
				moves[_case].push_back(move);
				i = !i;
			}
		}
		_case++;
	}
	ofstream o;
	o.open("o.txt");
	//start solving
	for(int i = 0; i < moves.size(); i++){
		for(int x = 0; x < moves[i].size(); x++){
			//cout << i << " " << x  << ": " << (moves[i][x].orange?"O":"B") << " " << (int) moves[i][x].to << std::endl;
		}
	}
	for(int i = 0; i < count; i++){
		int O = 1,B = 1;
		int t_O = 0,t_B = 0;
		int time = 0;
		Move process;
		bool completed = true;
		bool running = true;
		while(running){
			//cout << time << " ";
			if(completed){
				process = moves[i].front();
				moves[i].erase(moves[i].begin());
				completed = false;
				if(process.orange) t_O = process.to;
				else t_B = process.to;
				//cout << "new ";
			}
			if(t_O == 0){
				int index = getnext(moves[i],true);
				if(i >= 0) t_O = moves[i][index].to;
			}
			if(t_B == 0){
				int index = getnext(moves[i],false);
				if(i >= 0) t_B = moves[i][index].to;
			}
			if(process.to == (process.orange ? O : B)){
				completed = true;
				if(process.orange) t_O = 0;
				else t_B = 0;
				//cout << (process.orange ? "O":"B") << " there ";
			}
			if(O < t_O){
				O++;
				//cout << "O forward ";
			}
			else {
				if( O > t_O && t_O != 0){
					O--;
					//cout << "O back ";
				}
			} 
			if(B < t_B){
				B++;
				//cout << "B forward ";
			}
			else {
				if(B > t_B && t_B != 0){
					B--;
					//cout << "B back ";
				}
			}
			if(completed && moves[i].size() == 0) running = false;
			time++;
			//cout << std::endl;
		}
		o << "Case #" << (i+1) << ": " << time << std::endl;
	}
	o.close();
		
}
