#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

long gcd(long num1, long num2){
	long a,b,temp;

	if(num1 > num2){
		temp = num1;
		num1 = num2;
		num2 = temp;
	}

	a = num1; 
	b = num2;
	while(b != 0){
		temp = a%b;
		a = b;
		b = temp;
	}

	//cout<<"gcd:"<<a<<endl;
	//cout<<"lcm:"<<num1*num2/a<<endl;
	return a;
}

int main(){
	

	//FILE* in_file = fopen("test.in","r");
	FILE* in_file = fopen("B-small-attempt1.in","r");

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
	//getchar();
	int case_iter = 0;

	while(case_iter < case_num){
		ch = 0;
		line = "";
		int N;
		while(true){
			ch = fgetc(in_file);
			if(ch == ' ')
				break;
			line += ch;
		}
		N = atoi(line.c_str());
		
		//cout<<"N: "<<N<<endl;
		int n_iter = 0;
		long e[N];

		for(n_iter = 0 ;n_iter < N; n_iter++){
			ch = 0;
			line = "";

			while(true){
				ch = fgetc(in_file);
				if(n_iter == (N -1) ){
					if(ch == '\n'){
						break;
					}
				}else{
					if(ch == ' ')
						break;
				}

				line += ch;
			}

			e[n_iter] = atol(line.c_str());
		}
		
		/*
		for(n_iter = 0 ;n_iter < N; n_iter++){
			cout<<e[n_iter]<<" ";
		}
		*/

		long max_l = 0;

		long min_l = 0;
		bool found = false;

		if(N == 2){
			min_l = abs(e[0]-e[1]);

			if(min_l == 0){
				min_l = e[0];
				found = true;
				max_l = e[0];
			};
		}else{
			if(e[0] != e[1] && e[1] != e[2] && e[0] != e[2])
				min_l = min( abs(e[0]-e[1]),min(abs(e[2] - e[1]),abs(e[2] - e[0])) );
			else if(e[0] != e[1]){
				min_l = abs(e[0] - e[1]);
			}else if( e[1] != e[2]){
				min_l = abs(e[1] - e[2]);
			}else if(e[0] != e[2])
				min_l = abs(e[0] - e[2]);
			else{
				found = true;
				max_l = e[0];
			}
		}
		/*
		if(min_l !=0){
			cout<<"min_l: " <<min_l<<endl;
			
		}
		if(max_l !=0){
			cout<<"max_l: " <<max_l<<endl;
		}*/
		
		long muti_factor = 1;
		
		cout<<"Case #"<<case_iter + 1<<": ";
		if(!found){
		
			
			while(true){
				if(min_l*muti_factor - e[0] >=0)
					break;
				else{
					muti_factor++;
				}
			}

			int min_add = muti_factor*min_l - e[0];
			if(N == 2){
				long a = gcd((e[0] + min_add),(e[1] + min_add));
				long b = gcd(e[0],e[1]);
				if( a == 1|| a == b){
					cout<<0<<endl;
				}else{
					
					min_l = a;
					muti_factor = 1;
					while(true){
						if(min_l*muti_factor - e[0] >=0)
							break;
						else{
							muti_factor++;
						}
					}
					

					min_add = muti_factor*min_l - e[0];

					cout<<min_add<<endl;
				}
			}

			if(N == 3){
				long a = gcd((e[0] + min_add), gcd((e[1] + min_add),(e[2] + min_add)) );
				long b = gcd(e[0], gcd(e[1],e[2]) );
				if(a == 1 || a == b){
					cout<<0<<endl;
				}else{
					min_l = a;
		
					min_l = a;
					muti_factor = 1;
					while(true){
						if(min_l*muti_factor - e[0] >=0)
							break;
						else{
							muti_factor++;
						}
					}
					

					min_add = muti_factor*min_l - e[0];
					cout<<min_add<<endl;
				}
			}
			//cout<<min_add<<endl;
		}else{
			cout<<max_l<<endl;
		}	

		

		
		
		case_iter ++;

		
	}

	return 0;
}   
  
