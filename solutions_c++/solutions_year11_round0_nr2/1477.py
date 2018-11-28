#include <iostream>
#include <fstream>
#include <vector>
#include <string>


using namespace std;

class Combine{
	public:
		bool combine(vector<char> & v, char c){
			if(v.size()==0){
				return false;
			}
			if((v.back()==l1 && c==l2)
					||(v.back()==l2 && c==l1)){
				v.pop_back();
				v.push_back(r);
				return true;
			}
			return false;
		}
		char l1;
		char l2;
		char r;
};

class Opposed{
	public:
		bool opposed(vector<char> & v, char c){
			if(v.size()==0){
				return false;
			}
			bool flag = false;
			for(int i = 0; i < v.size(); i++){
				if((v[i]==l && c==r)
						||(v[i]==r && c==l)){
					flag = true;
					break;
				}
			}
			if(flag){
				v.clear();
				return true;
			}
			return false;
		}
		char l;
		char r;
};

string print(vector<char> & v){
	string ret;
	ret.push_back('[');
	if(v.size() != 0){
		ret.push_back(v[0]);
		for(int i = 1; i < v.size(); i++){
			ret.append(", ");
			ret.push_back(v[i]);
		}
	}
	ret.push_back(']');
	return ret;
}

int main(){
	ifstream in("B-large.in");
	ofstream out("result.out");
	int T;
	in >> T;
	for(int i = 1; i <= T; i++){
		int cnum;
		in >> cnum;
		vector<Combine*> cvec;
		for(int j = 0; j < cnum; j++){
			Combine * c = new Combine;
			in >> c->l1;
			in >> c->l2;
			in >> c->r;
			cvec.push_back(c);
		}		
		int onum;
		in >> onum;
		vector<Opposed*> ovec;
		for(int j = 0; j < onum; j++){
			Opposed * o = new Opposed;
			in >> o->l;
			in >> o->r;
			ovec.push_back(o);
		}
		int elenum;
		in >> elenum;
		vector<char> elevec;
		char c;
		for(int j = 0; j < elenum; j++){
			in >> c;
			bool flag = false;
			for(int k = 0; k < cnum; k++){
				if(flag){
					break;
				}
				flag = cvec[k]->combine(elevec, c);
			}
			for(int k = 0; k < onum; k++){
				if(flag){
					break;
				}
				flag = ovec[k]->opposed(elevec, c);
			}
			if(!flag){
				elevec.push_back(c);
			}
		}
		out << "Case #" << i << ": " << print(elevec) << endl; 
	}


	return 0;
}
