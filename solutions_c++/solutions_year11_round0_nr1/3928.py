#include <fstream>
using namespace std;

int N;
char sequence_robot[100];
int sequence[100];

int b_sequence[100];
int o_sequence[100];
int b_sequence_count;
int o_sequence_count;
int b_sequence_counter;
int o_sequence_counter;

int buttons_pressed;
int b_position;
int o_position;

void b_my_button(int temp){
	if(b_position==sequence[temp]){
		buttons_pressed++;
		b_sequence_counter++;
	}
	else{
		if(b_position<sequence[temp]) b_position++;
		else b_position--;
	}
}

void b_your_button(int temp){
	if(b_sequence_counter<b_sequence_count){
		if(b_position<b_sequence[b_sequence_counter]) b_position++;
		else if(b_position>b_sequence[b_sequence_counter]) b_position--;
	}
}

void o_my_button(int temp){
	if(o_position==sequence[temp]){
		buttons_pressed++;
		o_sequence_counter++;
	}
	else{
		if(o_position<sequence[temp]) o_position++;
		else o_position--;
	}
}

void o_your_button(int temp){
	if(o_sequence_counter<o_sequence_count){
		if(o_position<o_sequence[o_sequence_counter]) o_position++;
		else if(o_position>o_sequence[o_sequence_counter]) o_position--;
	}
}

void main(){
	ifstream in;
	in.open("A.in");
	ofstream out;
	out.open("A.out");
	int T;
	in>>T;
	for(int cases=0;cases<T;cases++){
		b_sequence_count=0;
		o_sequence_count=0;
		b_sequence_counter=0;
		o_sequence_counter=0;
		buttons_pressed=0;
		b_position=1;
		o_position=1;
		in>>N;
		for(int buttons=0;buttons<N;buttons++){
			in>>sequence_robot[buttons];
			in>>sequence[buttons];
			if(sequence_robot[buttons]=='B'){
				b_sequence[b_sequence_count]=sequence[buttons];
				b_sequence_count++;
			}else{
				o_sequence[o_sequence_count]=sequence[buttons];
				o_sequence_count++;
			}
		}
		int count=0;
		while(buttons_pressed<N){
			int temp=buttons_pressed;
			if(sequence_robot[temp]=='B'){
				b_my_button(temp);
				o_your_button(temp);
			}else{
				o_my_button(temp);
				b_your_button(temp);
			}
			count++;
		}
		out<<"Case #"<<(cases+1)<<": "<<count<<endl;
	}
	in.close();
	out.close();
	system("pause");
}