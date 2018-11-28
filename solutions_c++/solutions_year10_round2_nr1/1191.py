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


#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

typedef struct _tagNode{
	string name;
	vector<struct _tagNode> child;
} NODE;

int createTree(NODE& root,vector<string>::iterator path,int size,int& cmkdir){
	if(size == 0) return 1;
	for(vector<struct _tagNode>::iterator ite = root.child.begin(); ite != root.child.end(); ite++){
		if((ite)->name == *path){
			return createTree((*ite),path+1,size-1,cmkdir);
		}
	}
	struct _tagNode node;
	node.name = *path;
	root.child.push_back(node);
	return createTree(*(root.child.end()-1),path+1,size-1,++cmkdir);
}

int findPath(NODE& root,vector<string>::iterator path,int size){
	if(size == 0) return 1;
	for(vector<struct _tagNode>::iterator ite = root.child.begin(); ite != root.child.end(); ite++){
		if((ite)->name == *path){
			return findPath(*ite,path+1,size-1);
		}
	}
	return 0;
}

int main(int argc,char* argv[]){
	fstream fstr(argv[1]);
	string buf;

	if(!fstr||!getline(fstr,buf)) return 1;
	int T = atoi(buf.c_str());

	while(T-->0){
		if(!fstr||!getline(fstr,buf)) return 1;
		vector<int> in = parseStrIntV(buf," ");
		int N = in[0];
		int M = in[1];
		vector<string> exists;
		vector<string> create;

		for(int i=0;i<N;i++){
			if(!fstr||!getline(fstr,buf)) return 1;
			exists.push_back(buf);
		}

		for(int i=0;i<M;i++){
			if(!fstr||!getline(fstr,buf)) return 1;
			create.push_back(buf);
		}

		NODE root;
		root.name = "/";

		int cmkdir = 0;
		for(int i=0;i<N;i++){
			vector<string> path = parseStrStrV(exists[i],"/");

			createTree(root,path.begin(),path.size(),cmkdir);
		}

		cmkdir = 0;
		for(int i=0;i<M;i++){
			vector<string> path = parseStrStrV(create[i],"/");
			createTree(root,path.begin(),path.size(),cmkdir);
		}

		gout << cmkdir << std::endl;

	}

}