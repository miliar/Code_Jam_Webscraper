#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int found;

void find_w(string);
void find_we(string,int);
void find_wel(string,int);
void find_welc(string str, int pos);
void find_welco(string str, int pos);
void find_welcom(string str, int pos);
void find_welcome(string str, int pos);
void find_welcome_(string str, int pos);
void find_welcome_t(string str, int pos);
void find_welcome_to(string str, int pos);
void find_welcome_to_(string str, int pos);
void find_welcome_to_c(string str, int pos);
void find_welcome_to_co(string str, int pos);
void find_welcome_to_cod(string str, int pos);
void find_welcome_to_code(string str, int pos);
void find_welcome_to_code_(string str, int pos);
void find_welcome_to_code_j(string str, int pos);
void find_welcome_to_code_ja(string str, int pos);
void find_welcome_to_code_jam(string str, int pos);


int main(int argc, char** argv)
{
	int N;
	string s, result1, result2;
	ifstream input;
	ostringstream ss;
	input.open ("C-small-attempt0.in");

	input >> N;
	getline(input,s);

	for (int i = 0; i < N; i++){
		found = 0;
		getline(input,s);
		find_w(s);
		ss.str("");
		ss << found;
		result1 = ss.str();
		if (result1.length() == 1){
			 cout << "Case #" << i+1 << ": 000" << result1 << endl;
		}
		else if (result1.length() == 2){
			cout << "Case #" << i+1 << ": 00" << result1 << endl;
		}
		else if (result1.length() == 3){
			cout << "Case #" << i+1 << ": 0" << result1 << endl;
		}
		else{
			cout << "Case #" << i+1 << ": " << result1 << endl;
		}
	}


	return 0;
}

void find_w(string str){
	int pos = -1;
	while (1){
		pos = str.find("w",pos+1);
		if (pos != string::npos){
			find_we(str, pos);
		}
		else break;
	}
}

void find_we(string str, int pos){
	while (1){
		pos = str.find("e",pos+1);
		if (pos != string::npos){
			find_wel(str, pos);
		}
		else break;
	}
}

void find_wel(string str, int pos){
	while (1){
		pos = str.find("l",pos+1);
		if (pos != string::npos){
			find_welc(str, pos);
		}
		else break;
	}
}

void find_welc(string str, int pos){
	while (1){
		pos = str.find("c",pos+1);
		if (pos != string::npos){
			find_welco(str, pos);
		}
		else break;
	}
}

void find_welco(string str, int pos){
	while (1){
		pos = str.find("o",pos+1);
		if (pos != string::npos){
			find_welcom(str, pos);
		}
		else break;
	}
}

void find_welcom(string str, int pos){
	while (1){
		pos = str.find("m",pos+1);
		if (pos != string::npos){
			find_welcome(str, pos);
		}
		else break;
	}
}

void find_welcome(string str, int pos){
	while (1){
		pos = str.find("e",pos+1);
		if (pos != string::npos){
			find_welcome_(str, pos);
		}
		else break;
	}
}

void find_welcome_(string str, int pos){
	while (1){
		pos = str.find(" ",pos+1);
		if (pos != string::npos){
			find_welcome_t(str, pos);
		}
		else break;
	}
}

void find_welcome_t(string str, int pos){
	while (1){
		pos = str.find("t",pos+1);
		if (pos != string::npos){
			find_welcome_to(str, pos);
		}
		else break;
	}
}

void find_welcome_to(string str, int pos){
	while (1){
		pos = str.find("o",pos+1);
		if (pos != string::npos){
			find_welcome_to_(str, pos);
		}
		else break;
	}
}

void find_welcome_to_(string str, int pos){
	while (1){
		pos = str.find(" ",pos+1);
		if (pos != string::npos){
			find_welcome_to_c(str, pos);
		}
		else break;
	}
}

void find_welcome_to_c(string str, int pos){
	while (1){
		pos = str.find("c",pos+1);
		if (pos != string::npos){
			find_welcome_to_co(str, pos);
		}
		else break;
	}
}

void find_welcome_to_co(string str, int pos){
	while (1){
		pos = str.find("o",pos+1);
		if (pos != string::npos){
			find_welcome_to_cod(str, pos);
		}
		else break;
	}
}

void find_welcome_to_cod(string str, int pos){
	while (1){
		pos = str.find("d",pos+1);
		if (pos != string::npos){
			find_welcome_to_code(str, pos);
		}
		else break;
	}
}

void find_welcome_to_code(string str, int pos){
	while (1){
		pos = str.find("e",pos+1);
		if (pos != string::npos){
			find_welcome_to_code_(str, pos);
		}
		else break;
	}
}

void find_welcome_to_code_(string str, int pos){
	while (1){
		pos = str.find(" ",pos+1);
		if (pos != string::npos){
			find_welcome_to_code_j(str, pos);
		}
		else break;
	}
}

void find_welcome_to_code_j(string str, int pos){
	while (1){
		pos = str.find("j",pos+1);
		if (pos != string::npos){
			find_welcome_to_code_ja(str, pos);
		}
		else break;
	}
}

void find_welcome_to_code_ja(string str, int pos){
	while (1){
		pos = str.find("a",pos+1);
		if (pos != string::npos){
			find_welcome_to_code_jam(str, pos);
		}
		else break;
	}
}

void find_welcome_to_code_jam(string str, int pos){
	while (1){
		pos = str.find("m",pos+1);
		if (pos != string::npos){
			found++;
			if (found == 10000)
				found = 0;
		}
		else break;
	}
}

