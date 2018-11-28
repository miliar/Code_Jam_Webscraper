#include <iostream>
#include <string>
#include <vector>
#include <utility>

int main(int argc,char **argv){
	using namespace std;
	int testcase = 0;
	cin >> testcase;
	for(int j=0;j<testcase;j++){
		int step;
		cin >> step;
		vector<pair<char,int> > prog;
		for(int i=0;i<step;i++){
			char whichcolor;
			int placeofbutton;
			cin >> whichcolor;
			cin >> placeofbutton;
			pair<char,int> p;
			p.first = whichcolor;
			p.second = placeofbutton;
			prog.push_back(p);
		}
		int place_o = 1;
		int place_b = 1;
		char con = 1;
		int num = 0;
		while(con==1){
			vector<pair<char,int> >::iterator it = prog.begin();
			char nextcolor = it->first;
			int buttonplace = it->second;
			int anothercolorplace = 1;
			it++;
			while(it != prog.end()){
				if(nextcolor != it->first){
					anothercolorplace = it->second;
					break;
				}
				it++;
			}
			if(nextcolor=='O'){
				if(place_o==buttonplace){
					prog.erase(prog.begin());
				}else if(place_o < buttonplace){
					place_o++;
				}else{
					place_o--;
				}
				if(place_b < anothercolorplace){
					place_b++;
				}else if(place_b > anothercolorplace){
					place_b--;
				}
			}else{
				if(nextcolor=='B'){
					if(place_b==buttonplace){
						prog.erase(prog.begin());
					}else if(place_b < buttonplace){
						place_b++;
					}else{
						place_b--;
					}
					if(place_o < anothercolorplace){
						place_o++;
					}else if(place_o > anothercolorplace){
						place_o--;
					}
				}
			}
			num++;
			if(prog.empty()){
				con = 0;
				cout << "Case #" << j+1 << ": " << num << endl;
			}
		}
	}
}
