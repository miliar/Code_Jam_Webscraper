#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <iomanip>

struct Data{
	std::vector<char> data;
};

std::string trial(const Data& input){
	char d[4][4];
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			d[i][j]=input.data[i*4+j];
		}
	}

	std::ostringstream oss;
	
	int count;
	// 行について
	for(int i=0;i<4;i++){
		count=0;
		if(d[i][0]=='.')continue;
		else count++;
		if(d[i][0]=='T'){
			if(d[i][1]=='.') continue;
			else count++;
			for(int j=2;j<4;j++){
				if(d[i][j]==d[i][j-1]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[i][1] << " " << "won";
				return oss.str();
			}
		}else{
			for(int j=1;j<4;j++){
				if(d[i][j]=='T'||d[i][0]==d[i][j]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[i][0] << " " << "won";
				return oss.str();
			}
		}
	}

	// 列について
	for(int j=0;j<4;j++){
		count=0;
		if(d[0][j]=='.')continue;
		else count++;
		if(d[0][j]=='T'){
			if(d[1][j]=='.') continue;
			else count++;
			for(int i=2;i<4;i++){
				if(d[i][j]==d[i-1][j]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[1][j] << " " << "won";
				return oss.str();
			}
		}else{
			for(int i=1;i<4;i++){
				if(d[i][j]=='T'||d[0][j]==d[i][j]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[0][j] << " " << "won";
				return oss.str();
			}
		}
	}


	// 斜めについて
	count=0;
	if(d[0][0]=='T'){
			count++;
		if(d[1][1]!='.'){
			count++;
			for(int i=2;i<4;i++){
				if(d[i][i]==d[1][1])count++;
			}
			if(count==4){
				oss.str("");
				oss << d[1][1] << " " << "won";
				return oss.str();
			}
		}
	}else{
		if(d[0][0]!='.'){
			count++;
			for(int i=1;i<4;i++){
				if(d[i][i]=='T'||d[0][0]==d[i][i]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[0][0] << " " << "won";
				return oss.str();
			}
		}
	}
	count=0;
	if(d[0][3]=='T'){
			count++;
		if(d[1][2]!='.'){
			count++;
			for(int i=2;i<4;i++){
				if(d[i][3-i]==d[1][2])count++;
			}
			if(count==4){
				oss.str("");
				oss << d[1][2] << " " << "won";
				return oss.str();
			}
		}
	}else{
		if(d[0][3]!='.'){
			count++;
			for(int i=1;i<4;i++){
				if(d[i][3-i]=='T'||d[0][3]==d[i][3-i]) count++;
			}
			if(count==4){
				oss.str("");
				oss << d[0][3] << " " << "won";
				return oss.str();
			}
		}
	}

	int c=0;
	for(int i=0;i<16;i++){
		if(input.data[i]!='.') c++;
	}
	if(c==16){
		return "Draw";
	}

	return "Game has not completed";
}

int main(int argc, char **argv){
	std::string str;
	int t;

	std::cin >> t;
	std::vector<Data> query(t);
	for(int i=0;i<t;i++){
		char c;
		for(int j=0;j<16;j++){
			std::cin >> c;
			query[i].data.push_back(c);
		}
	}

	std::vector<std::string> result(t);
#ifdef _OPENMP
#pragma omp parallel for
#endif
	for(int i=0;i<t;i++){
		result[i]=trial(query[i]);
	}

	for(int i=0;i<t;i++){
		std::cout << "Case #" << i+1 << ": " << result[i] << std::endl;
	}
	return 0;
}
