#include <stdio.h>
#include <vector>
#include <iostream>


using namespace std;

#define dbg(...)  \
	fprintf(stdout,__VA_ARGS__); \
	fprintf(stdout,"\n");

struct Move {
	char robot;
	int move;
	int seq;

	Move(char robot,int move,int seq) {
		this->move = move;
		this->robot = robot;
		this->seq = seq;
	}
};


class Robot {

private:
	FILE * fin;
	FILE * fout;
	vector <Move*> moves_o;
	vector <Move*> moves_b;
	long int timer;

public:
	Robot(char *fileName);
	~Robot() {
		fclose(fout);
		fclose (fin);
	}
	void ReadInputs();
	void CalculateBestTime();
	void PrintResults();
	void CleanMoveVec( vector <Move *> & vec);
	void ResetTimer() { timer = 0;}
	void IncrTime(int bpos,int opos,int cnt = 1) { 
		timer+= cnt; 
		dbg("B: %d  O: %d  T: %d\n",bpos,opos,timer);
	}
	long int GetTime() { return timer;}
	int mod(int val) { return (val > 0? val : -1* val); }
};


Robot::Robot(char *fileName) : timer(0) {
	if (!fileName) {
		cout << "No input file name!"<<endl;
		exit(1);
	}

	fin = fopen(fileName,"r");
	if (!fin) {
		cout << "Cannot open file "<<fileName<<endl;
		exit(1);
	}

	fout = fopen("C:/out.txt","w");
	if (!fout) {
		cout << "Cannot open file "<<"C:/out.txt"<<endl;
		exit(1);
	}
	ReadInputs();
}


void Robot::ReadInputs () {
	int T = 0;
	fscanf(fin,"%d",&T);
	dbg("Number of tests : %d",T);

	for (int i = 0; i < T; i++) {
		int N = 0;
		fscanf(fin,"%d ",&N);
		dbg("Number of buttons : %d",N);

		for (int j = 0;j < N;j++) {
			char Ri = 0;
			int Pi = 0;
			fscanf(fin,"%c %d ",&Ri,&Pi);
			dbg ("Robot Name : %c , Position : %d",Ri,Pi);
			Move *newpos = new Move(Ri,Pi,j+1);
			if ( Ri == 'O' || Ri == 'o' ) 
				moves_o.push_back(newpos);
			else
				moves_b.push_back(newpos);
		}

		CalculateBestTime();
		cout << "Case #"<<i+1<<": "<<GetTime() << endl;
		fprintf(fout,"Case #%d: %d\n",i+1,GetTime());
		CleanMoveVec(moves_o);
		CleanMoveVec(moves_b);
	}
}

void Robot::CleanMoveVec(vector <Move*> & vec) {
	unsigned int i = 0;
	while(i < vec.size() ) {
		free (vec[i]);
		i++;
	}
	vec.clear();
}


/* Algorithm
1.	Constraint is one Push button sequence.
2.  Moves can be done togather. No constraint there.
3.  1 unit time for push and move(s), move over lap is possible.
4.  Now Algo
a. Get one move for each type
*/
void Robot::CalculateBestTime() {
	dbg ("Total number of moves in moves_o  : %d , moves_b : %d",
		moves_o.size(),moves_b.size());
	int opos = 1;
	int bpos = 1;
	int seq_found = 0;
	int i = 0;
	int j = 0;
	int g_seq = 1;
	int jump_step = 0;

	ResetTimer();
	IncrTime(bpos,opos,0);
	while ( i < moves_o.size() || j < moves_b.size() ) {

		if (i < moves_o.size()) {
			if (g_seq == moves_o[i]->seq ) {
				seq_found = 1;
				jump_step = mod(moves_o[i ]->move - opos);
				if (0 == jump_step) {
					if (j < moves_b.size() && moves_b[j]->move != bpos) {
						bpos += ((moves_b[j]->move >= bpos)? 1 : -1);
					}
					IncrTime(bpos,opos);
					seq_found = 0;
					g_seq++;
					i++;
					continue;
				}
				else {
					opos = moves_o[i]->move;
					IncrTime(bpos,opos,jump_step);
				}
			} else {
				if (seq_found && moves_o[i]->move != opos) {
					if (jump_step && jump_step <= mod(moves_o[i]->move - opos) )
						opos += ((moves_o[i]->move >= opos)? jump_step : (-1* jump_step));
					else if ( jump_step && jump_step > mod(moves_o[i]->move - opos))
						opos = moves_o[i]->move;
					else
						opos += ((moves_o[i]->move >= opos)? 1: -1);

				}
			}
		}

		if ( j < moves_b.size()) {
			if (g_seq == moves_b[j]->seq ) {
				seq_found = 1;
				jump_step = mod(moves_b[j]->move - bpos);
				if (0 == jump_step) { 
					if (i < moves_o.size() && moves_o[i]->move != opos) {
						opos += ((moves_o[i]->move >= opos)? 1:-1);
					}
					IncrTime(bpos,opos);
					g_seq++;
					seq_found = 0;
					j++;
					continue;
				}
				else {
					bpos = moves_b[j]->move;
					IncrTime(bpos,opos,jump_step);
				}
			} else {
				if (seq_found && moves_b[j]->move != bpos) {
					if (jump_step && jump_step <= mod(moves_b[j]->move - bpos) )
						bpos += ((moves_b[j]->move >= bpos)? jump_step : (-1* jump_step));
					else if ( jump_step && jump_step > mod(moves_b[j]->move - bpos))
						bpos = moves_b[j]->move;
					else
						bpos += ((moves_b[j]->move >= bpos)? 1: -1);
				}
			}
		}
	}
}


int main(int argc,char * argv[]) {
	Robot obj("C:/input.txt");
	return 0;
}