#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(){
	//cout<<"hello"<<endl;	

	FILE* in_file = fopen("C-small-attempt0.in","r");

	if(in_file == NULL){
		cerr<<"error in read file";
		exit(0);
	}

	int case_num = 0;

	int ch;
	string line = "";
	while(true){
		ch = fgetc(in_file);
		if(ch == '\n'){
			break;
		}
		line += ch;
		
	}

	case_num = atoi(line.c_str());

	//cout<<case_num<<endl;

	int case_iter = 0;

	while(case_iter < case_num){
		
		long R = 0;
		long K = 0;
		int N = 0;
		
		ch = 0;
		line = "";
		while(true){
			ch = fgetc(in_file);
			if(ch == ' ')
				break;
			line += ch;	
		}
		
		R = atol(line.c_str());
		
		ch = 0;
		line = "";
		while(true){
			

			ch = fgetc(in_file);
			if(ch == ' ')
				break;
			line += ch;		
		}

		K = atol(line.c_str());

		ch = 0;
		line = "";
		while(true){
			

			ch = fgetc(in_file);
			if(ch == '\n')
				break;
			line += ch;		
		}

		N = atoi(line.c_str());
		//cout<<R<<" "<<K<<" "<<N<<endl;
		
		long g[N];
		
		int n_iter = 0;

		for(n_iter = 0; n_iter < N; n_iter++){
			ch = 0;
			line = "";
			while(true){
				
				ch = fgetc(in_file);
				if(n_iter != (N -1) ){
					if(ch == ' ')
						break;
				}else{
					if(ch == '\n')
						break;
				}
				line += ch;		
			}

			g[n_iter] = atol(line.c_str());
			
		}

		
		list<long> queue;
		list<long> rest;
		

		for(n_iter = 0; n_iter < N; n_iter++){
			queue.push_back(g[n_iter]);
		}

		int R_iter = 0;
		long long total = 0;
		for(R_iter = 0; R_iter < R; R_iter++ ){
			list<long>::iterator q_iter;
			
			long sum = 0;
			int numOfpop = 0;
			for(q_iter = queue.begin(); q_iter != queue.end(); q_iter++){
				if( (sum + *q_iter) <= K){
					sum += *q_iter;
					long temp = *q_iter;
					//queue.pop_front();
					numOfpop++;
					rest.push_back(temp);
				}else{
					break;
				}
			}

			for(int i = 0; i < numOfpop; i++){
				queue.pop_front();
			}

			list<long>::iterator r_iter2;
			for(r_iter2 = rest.begin(); r_iter2 != rest.end(); r_iter2++){
				queue.push_back(*r_iter2);
			}

			int r_iter = 0;
			int r_size = rest.size();
			for(r_iter = 0; r_iter < r_size; r_iter++){
				rest.pop_front();
			}
			//cout<< sum <<endl;
			total += sum;
		}

		//Case #1: 21
		cout<<"Case #"<<case_iter+1<<": ";
		cout<<total<<endl;	
		//getchar();
		
		case_iter++;
	}





	
}
