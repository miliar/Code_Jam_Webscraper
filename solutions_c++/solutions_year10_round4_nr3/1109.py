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


class POINT{
public:
	int x,y;
	
};

bool operator <(const POINT& obj1,const POINT& obj2){
	return (obj1.x *1000000 + obj1.y) < (obj2.x *1000000 + obj2.y);
}

bool operator >(const POINT& obj1,const POINT& obj2){
	return (obj1.x *1000000 + obj1.y) > (obj2.x *1000000 + obj2.y);
}

bool operator ==(const POINT& obj1,const POINT& obj2){
	return (obj1.x== obj2.x) && (obj1.y == obj2.y);
}


int main(int argc,char* argv[]){
	fstream fstr(argv[1]);
	string buf;

	if(!fstr||!getline(fstr,buf)) return 1;
	int T = atoi(buf.c_str());

	while(T-->0){
		if(!fstr||!getline(fstr,buf)) return 1;
		int N = atoi(buf.c_str());

		set<POINT> bac;

		for(int i=0;i<N;i++){
			if(!fstr||!getline(fstr,buf)) return 1;
			vector<int> in = parseStrIntV(buf," ");

			for(int  x=in[0];x<=in[2];x++){
				for(int  y=in[1]; y<=in[3];y++){
					POINT tmp = {x,y};
					bac.insert(tmp);
				}
			}
		}
		set<POINT> bac2;
		set<POINT>* work;
		set<POINT>* work2;

		int t;
		for(t=1;;t++){
			
			if(t %2 == 1){
				work = &bac;
				work2 = &bac2;
			}else{
				work = &bac2;
				work2 = &bac;
			}
			work2->clear();
			printf("%d\n",work->size());

			for(set<POINT>::iterator ite = work->begin(); ite != work->end();ite++){
				//printf("%d %d\n",ite->x,ite->y);
				POINT pos;

				pos.x = ite->x+1;
				pos.y = ite->y-1;
				if(work->find(pos) != work->end()){
					pos.x = ite->x+1;
					pos.y = ite->y;
					//printf("%d %d created\n",pos.x,pos.y);
					work2->insert(pos);
				}

				pos.x = ite->x-1;
				pos.y = ite->y+1;
				if(work->find(pos) != work->end()){
					pos.x = ite->x;
					pos.y = ite->y+1;
					//printf("%d %d created\n",pos.x,pos.y);
					work2->insert(pos);
				}
				
			}
			for(set<POINT>::iterator ite = work->begin();ite!=work->end();ite++){
				POINT pos1,pos2;

				pos1.x = ite->x-1;
				pos1.y = ite->y;
				pos2.x = ite->x;
				pos2.y = ite->y-1;


				if(work->find(pos1) == work->end() && work->find(pos2) == work->end()){
					//printf("%d %d deleted\n",ite->x,ite->y);
				}else{
					work2->insert(*ite);
				}
			}		
			if(work2->size() == 0){
				break;
			}
			
		}

		gout << t << std::endl;
	}

}