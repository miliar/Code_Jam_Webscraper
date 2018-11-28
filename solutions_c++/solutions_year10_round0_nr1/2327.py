#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(){
	//cout<<"hello"<<endl;	

	FILE* in_file = fopen("A-large.in","r");

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
	//getchar();

	while(case_iter < case_num){
		ch = 0;
		line = "";

		int N;
		while(true){
			ch = getc(in_file);
			if(ch == ' '){
				break;
			}
			line += ch;
		}

		N = atoi(line.c_str());

		line = "";
		ch = 0;

		long long K;
		
		int numOfdigit = 1;
		while(true){
			ch = getc(in_file);
			if(ch == '\n'){
				break;
			}

			if(numOfdigit == 9){
				line += ch;
				break;
			}else{
				line += ch;
			}
			numOfdigit++;
			
			
		}

		if(ch == '\n'){
			K = atol(line.c_str());
		}else{
			ch = 0;
			long long temp = atol(line.c_str());
			//cout<<temp<<endl;
			numOfdigit = 0;
			line ="";
			while(true){
				ch = getc(in_file);
				if(ch == '\n'){
					break;
				}
				numOfdigit++;
				line += ch;
			}

			while(numOfdigit != 0){
				temp = temp *10;
				numOfdigit --;
			}
			
			K = temp + atol(line.c_str());
		}

		//K = atoi(line.c_str());
		//cout<<N<<" "<<K<<endl;

		long long circle = 1;

		while(N > 0){
			circle *= 2;
			N--;
		}
		long long  remain = circle -1;
		//cout<<circle<<" "<<remain<<endl;
		cout<<"Case #"<<case_iter+1<<": ";

		if(K == 0)
			cout<<"OFF"<<endl;
		else{
			if( (K % circle) == remain){
				cout<<"ON"<<endl;
			}else{
				cout<<"OFF"<<endl;
			}
		}
		
		//getchar();

		case_iter++;
	}
}
