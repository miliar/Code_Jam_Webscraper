#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>
#include <list>

using namespace std;


vector<double> parseStrDoubleV(string str,string del){
	int cut;
	string buf;
	vector<double> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atof(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atof(str.c_str()));
	}
	return result;
}	

list<double> parseStrDoubleL(string str,string del){
	int cut;
	string buf;
	list<double> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atof(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atof(str.c_str()));
	}
	return result;
}	


list<int> parseStrIntL(string str,string del){
	int cut;
	string buf;
	list<int> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atoi(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atoi(str.c_str()));
	}
	return result;
}	

vector<int> parseStrIntV(string str,string del){
	int cut;
	string buf;
	vector<int> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(atoi(buf.c_str()));	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back(atoi(str.c_str()));
	}
	return result;
}	

vector<string> parseStrStrV(string str,string del){
	int cut;
	string buf;
	vector<string> result;
	while( (cut = str.find_first_of(del)) != str.npos){
		if(cut > 0){
			buf = str.substr(0,cut);
			if(buf.length() == 0){
				continue;
			}
			result.push_back(buf.c_str());	
		}
		str = str.substr(cut+1);
	}
	if(str.length() > 0){
		result.push_back((str.c_str()));
	}
	return result;
}


int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout

int isCross(int A1,int B1,int A2,int B2){
	return (A1-A2)*(B1-B2) < 0;
}

int main(int argc,char* argv[]){
	fstream fstr(argv[1]);
	string buf;

	if(!fstr||!getline(fstr,buf)) return 1;
	int T = atoi(buf.c_str());

	while(T-->0){
		if(!fstr||!getline(fstr,buf)) return 1;
		int N = atoi(buf.c_str());

		vector<int> A(N);
		vector<int> B(N);
		for(int i=0;i<N;i++){
			if(!fstr||!getline(fstr,buf)) return 1;
			
			vector<string> in = parseStrStrV(buf," ");
			A[i] = atoi(in[0].c_str());
			B[i] = atoi(in[1].c_str());			
		}

		int c=0;
		for(int i=0;i<N;i++){
			for(int j=i+1;j<N;j++){
				if(isCross(A[i],B[i],A[j],B[j])){
					c++;
				}
			}
		}
		gout << c << std::endl;
	}

}