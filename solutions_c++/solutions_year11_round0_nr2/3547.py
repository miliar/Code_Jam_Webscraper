#include <fstream>
using namespace std;

void main(){
	ifstream in;
	in.open("B.in");
	ofstream out;
	out.open("B.out");
	int T;
	in>>T;
	for(int cases=0;cases<T;cases++){
		int C;
		in>>C;
		char combination[36][4];
		for(int combinations=0;combinations<C;combinations++){
			in>>combination[combinations];
		}
		int D;
		in>>D;
		char opposition[28][3];
		for(int oppositions=0;oppositions<D;oppositions++){
			in>>opposition[oppositions];
		}
		int	N;
		in>>N;
		char stack[100];
		int stack_top=-1;
		char temp;
		in.ignore();
		for(int invocations=0;invocations<N;invocations++){
			temp=in.get();
			if(stack_top>=0){
				bool flag=false;
				for(int combinations=0;combinations<C;combinations++){
					if(((combination[combinations][0]==temp)&&(combination[combinations][1]==stack[stack_top]))||((combination[combinations][0]==stack[stack_top])&&(combination[combinations][1]==temp))){
						stack[stack_top]=combination[combinations][2];
						flag=true;
					}
				}
				if(flag==false){
						stack[(stack_top+1)]=temp;
						stack_top++;
				}
				for(int sieve=0;sieve<stack_top;sieve++){
					for(int oppositions=0;oppositions<D;oppositions++){
						if(stack_top>=0){
						if(((opposition[oppositions][0]==stack[stack_top])&&(opposition[oppositions][1]==stack[sieve]))||((opposition[oppositions][0]==stack[sieve])&&(opposition[oppositions][1]==stack[stack_top]))){
							stack_top=-1;
						}
						}
					}
				}
			}else{
				stack[(stack_top+1)]=temp;
				stack_top++;
			}
		}
		out<<"Case #"<<(cases+1)<<": [";
		for(int stack_count=0;stack_count<stack_top;stack_count++){
			out<<stack[stack_count]<<", ";
		}
		if(stack_top>=0) out<<stack[stack_top];
		out<<"]"<<endl;
	}
	in.close();
	out.close();
	system("pause");
}