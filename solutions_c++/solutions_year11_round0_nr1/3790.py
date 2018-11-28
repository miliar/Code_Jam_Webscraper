#include<iostream>
#include<fstream>
#include<string>
#include<cstdio>

using namespace std;

class Q{
public:
	char color;
	int num;
};

Q *q;
int top = 0;
int b = 1;
int o = 1;

Q * find_top(char color, int cases){
	for(int i = top; i < cases; i++){
		if(q[i].color == color)
			return &q[i];
	}
	return NULL;
}

int next(int from, int to){
	if(from == to)
		return from;
	else if(from < to)
		return from + 1;
	else
		return from - 1;
}

void one_step(int cases, int *b_pre, int *o_pre){
	bool push = false;
	Q *b_dst = find_top('B', cases);
	Q *o_dst = find_top('O', cases);

	if((q[top].color == 'B' && q[top].num == *b_pre)){
		//cout<<"B Push";
		push = true;
	}else if(b_dst != NULL){
		*b_pre = next(*b_pre, b_dst->num);
		//cout<<"B Move to "<<*b_pre;
	}

	//cout<<" ";

	if(q[top].color == 'O' && q[top].num == *o_pre){
		//cout<<"O Push";
		push = true;
	}else if(o_dst != NULL){
		*o_pre = next(*o_pre, o_dst->num);
		//cout<<"O Move to "<<*o_pre;
	}
	if(push)
		top++;
	//cout<<endl;
}

int main(int argc, char *argv[]){
	if(argc != 2)
		return -1;
	ifstream fin(argv[1]);
	int tests = 1;
	int cases = 0;
	string str;
	
	fin>>str;
	while(!fin.eof()){
		fin>>str;
		if(!fin)
			break;
		cases = atoi(str.c_str());
		//cout<<cases;
		q = new Q[cases];
		for(int i = 0; i < cases; i++){
			fin>>str;
			q[i].color = str.c_str()[0];
			fin>>str;
			q[i].num = atoi(str.c_str());
			//cout<<q[i].color<<q[i].num;
		}
		//cout<<endl;

		int b_pre, o_pre, steps;
		b_pre = o_pre = 1;
		steps = 0;
		while(top < cases){
			one_step(cases, &b_pre, &o_pre);
			steps++;
		}

		cout<<"Case #"<<tests++<<": "<<steps<<endl;

		top = 0;
		cases = 0;
		delete [] q;
	}

	fin.close();
	return 0;
}
