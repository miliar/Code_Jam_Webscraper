/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: stefan
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

//#define DEBUG 1

struct comp{
	bool operator()(const pair<char, char>& p, const pair<char, char>& c) const{
		return !(((p.first == c.first) && (p.second == c.second)) || ((p.first == c.second) && (p.second == c.first)));
	}
};

#ifdef DEBUG

void print_list(const vector<char>& v){
	cout<<"[";
	for(size_t i = 0; i < v.size(); i++)
		cout<<v[i]<<" ";
	cout<<"]"<<endl;
}

#endif

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in>>T;

	for(int round = 1; round <= T; round++){
		map<pair<char, char>, char, comp> transformations;
		int C;
		in>>C;

		for(int i = 0; i < C; i++){
			char a, b, c;
			in>>a>>b>>c;
			transformations.insert(make_pair(make_pair(a, b), c));

			while(in.peek() == ' '){
				in.get();
			}
		}

		map<char, vector<char> > opposing;
		int D;
		in>>D;
		for(int i = 0; i < D; i++){
			char a, b;
			in>>a>>b;

			opposing[a].push_back(b);

			opposing[b].push_back(a);

			while(in.peek() == ' '){
				in.get();
			}
		}

		vector<char> invoked;
		int N;
		in>>N;
		for(int i = 0; i < N; i++){
			char a;
			in>>a;
			invoked.push_back(a);

#ifdef DEBUG
			cout<<a<<": ";
#endif

			bool transformed = false;
			if(invoked.size() > 1){
				map<pair<char, char>, char, comp>::iterator it =
						transformations.find(make_pair(invoked[invoked.size()-1], invoked[invoked.size()-2]));
				if(it != transformations.end()){
					// found a transformation

#ifdef DEBUG
					cout<<"\tTransforming "<<invoked[invoked.size()-1]<<" & "<<invoked[invoked.size()-2]<<" into "<<it->second<<endl;
#endif

					invoked.pop_back();
					invoked.pop_back();

					invoked.push_back(it->second);

					transformed = true;
				}
			}

			if(!transformed){
				bool clear_list = false;

				map<char, vector<char> >::iterator it = opposing.find(invoked[invoked.size() - 1]);

				if(it != opposing.end()){
					for(vector<char>::iterator v_it = it->second.begin(); v_it != it->second.end(); v_it++){
						if(find(invoked.begin(), invoked.end(), *v_it) != invoked.end()){
#ifdef DEBUG
							cout<<"Clearing list because found "<<invoked[invoked.size()-1]<<" & "<<*v_it<<endl;
#endif

							clear_list = true;
							break;
						}
					}
				}

				if(clear_list){
					invoked.clear();
				}
			}

#ifdef DEBUG
			print_list(invoked);
#endif
		}

		out<<"Case #"<<round<<": [";
		for(size_t i = 0; i < invoked.size(); i++){
			out<<invoked[i];
			if(i != invoked.size() - 1)
				out<<", ";
		}

		out<<"]"<<endl;

#ifdef DEBUG
		getchar();
#endif
	}

	in.close();
	out.close();

	return 0;
}
