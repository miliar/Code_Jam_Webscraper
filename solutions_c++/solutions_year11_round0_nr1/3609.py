#include <cstdio>
#include <vector>

using namespace std;

struct Command{
	Command(short index, Command* wait_for):wait_for_(wait_for), completed_(false), index_(index)/*, robot_(robot)*/{}
	Command *wait_for_;
	bool completed_;
	short index_;
	bool prev_completed(){
		if(wait_for_ == 0){
			return true;
		}
		return wait_for_->completed_;
	}
};
short abs(short n){
	return (n<0?-n:n);
}

int main(){
	unsigned int t;
	char r;
	unsigned int p, n;
	scanf("%d", &t);
	for(unsigned int i = 0; i < t; ++i){
		vector<Command*> blueCommands;
		vector<Command*> orangeCommands;
		scanf("%d ", &n);
		Command *prev=0;
		for(unsigned int j = 0; j < n; ++j){
			scanf(" %c %d", &r, &p);
			Command *new_c = new Command(p-1, prev);
			prev = new_c;
			if(r == 'O'){
				orangeCommands.push_back(new_c);
			}else if(r == 'B'){
				blueCommands.push_back(new_c);
			}
		}
		unsigned int b_i, o_i;
		b_i = 0;
		o_i = 0;
		short b_pos, o_pos;
		b_pos = 0;
		o_pos = 0;
		unsigned int steps = 0;
		unsigned int blue_steps = 0, orange_steps = 0;
		while(b_i < blueCommands.size() || o_i < orangeCommands.size()){
			if(b_i < blueCommands.size()){
				blue_steps = abs(b_pos - blueCommands[b_i]->index_);
			}
			if(o_i < orangeCommands.size()){
				orange_steps = abs(o_pos - orangeCommands[o_i]->index_);
			}
			if(b_i < blueCommands.size() && o_i < orangeCommands.size()){
				if(blue_steps == 0){
					if(blueCommands[b_i]->prev_completed()){
						blueCommands[b_i]->completed_ = true;
						++b_i;
						++steps;
						if(orange_steps != 0){
							if(o_pos < orangeCommands[o_i]->index_){
								++o_pos;
							}else{
								--o_pos;
							}
						}
						continue;
					}
					
					o_pos = orangeCommands[o_i]->index_;
					steps += orange_steps;
					if(orangeCommands[o_i]->prev_completed()){
						orangeCommands[o_i]->completed_ = true;
						++steps;
						++o_i;
					}
					continue;
				}
				if(orange_steps == 0){
					if(orangeCommands[o_i]->prev_completed()){
						orangeCommands[o_i]->completed_ = true;
						++o_i;
						++steps;
						if(blue_steps != 0){
							if(b_pos < blueCommands[b_i]->index_){
								++b_pos;
							}else{
								--b_pos;
							}
						}
						continue;
					}
					b_pos = blueCommands[b_i]->index_;
					steps += blue_steps;
					if(blueCommands[b_i]->prev_completed()){
						blueCommands[b_i]->completed_ = true;
						++steps;
						++b_i;
					}
					continue;
				}
				if(blue_steps < orange_steps){
					b_pos = blueCommands[b_i]->index_;
					steps += blue_steps;
					if(o_pos < orangeCommands[o_i]->index_){
						o_pos += blue_steps;
					}else{
						o_pos -= blue_steps;
					}
					if(blueCommands[b_i]->prev_completed()){
						blueCommands[b_i]->completed_ = true;
						++steps;
						++b_i;
						if(o_pos < orangeCommands[o_i]->index_){
							++o_pos;
						}else{
							--o_pos;
						}
					}
					continue;
				}
				if(orange_steps < blue_steps){
					o_pos = orangeCommands[o_i]->index_;
					steps += orange_steps;
					if(b_pos < blueCommands[b_i]->index_){
						b_pos += orange_steps;
					}else{
						b_pos -= orange_steps;
					}
					if(orangeCommands[o_i]->prev_completed()){
						orangeCommands[o_i]->completed_ = true;
						++o_i;
						++steps;
						if(b_pos < blueCommands[b_i]->index_){
							++b_pos;
						}else{
							--b_pos;
						}
					}
					continue;
				}
				o_pos = orangeCommands[o_i]->index_;
				b_pos = blueCommands[b_i]->index_;
				steps += blue_steps+1;
				if(orangeCommands[o_i]->prev_completed()){
					orangeCommands[o_i]->completed_ = true;
					++o_i;
				}else{
					blueCommands[b_i]->completed_ = true;
					++b_i;
				}
			}else if(b_i < blueCommands.size()){
				steps += blue_steps+1;
				b_pos = blueCommands[b_i]->index_;
				blueCommands[b_i]->completed_ = true;
				++b_i;
			}else if(o_i < orangeCommands.size()){
				steps += orange_steps +1;
				o_pos = orangeCommands[o_i]->index_;
				orangeCommands[o_i]->completed_ = true;
				++o_i;
			}
		}
		printf("Case #%d: %d%s",i+1, steps, (i<t-1?"\n":""));
	}
	return 0;
}
