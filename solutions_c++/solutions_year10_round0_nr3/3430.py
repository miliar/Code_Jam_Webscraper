
#include <iostream>
#include <fstream>
#include <map>
#include <list>

using namespace std;

struct cheat{
	size_t end;
	unsigned __int64 money;
};

int main(){
	ifstream input("inputC.txt");
	ofstream output("outputC.txt");
	size_t T;
	input >> T;
	size_t R,k,N,next,freePlaces,startFrom,lastCheat;
	size_t *g;
	unsigned __int64 money = 0;
	g = new size_t[10000000];
	map<size_t,cheat> cheats;
	list<size_t> road,way;
	unsigned __int64 sumOfWay = 0,
		sumOfRoad = 0;
	bool endRoad;
	for(size_t i = 0; i < T;i++){
		input >> R >> k >> N;
		for(size_t j = 0; j < N;j++){
			input >> g[j];
		}
		money = 0;
		next = 0;
		lastCheat = next;
		cheats.clear();
		road.clear();
		endRoad = false;
		while(cheats[lastCheat].money == 0){
			cheat temp = cheats[lastCheat];			
			for(list<size_t>::iterator it = road.begin();it!=road.end();it++){
				if(lastCheat == (*it)){
					endRoad = true;
					way = list<size_t>(road.begin(),it);
					road = list<size_t>(it,road.end());
					break;
				}
			}
			if(!endRoad){
				road.push_back(lastCheat);
			}
			size_t startFromC = lastCheat,
				nextC = lastCheat,
				freePlacesC = k;
			do{
				freePlacesC -= g[nextC];
				nextC = (nextC+1)%N;
			}while(g[nextC] <= freePlacesC && nextC != startFromC);
			money += k - freePlacesC;
			temp.money = money;
			temp.end = nextC;
			cheats[lastCheat] = temp;
			money = 0;
			lastCheat = nextC;
		}
		for(list<size_t>::iterator it = road.begin();it!=road.end();it++){
			if(lastCheat == (*it)){
				endRoad = true;
				way = list<size_t>(road.begin(),it);
				road = list<size_t>(it,road.end());
				break;
			}
		}
		sumOfRoad = 0;
		sumOfWay = 0;
		for(list<size_t>::iterator it = way.begin();it!=way.end();it++){
			sumOfWay += cheats[(*it)].money;
		}
		for(list<size_t>::iterator it = road.begin();it!=road.end();it++){
			sumOfRoad += cheats[(*it)].money;
		}
		money = 0;
		if(R >= way.size()){
			R -= way.size();
			money += sumOfWay + sumOfRoad*(R/road.size());
			R %= road.size();
			for(list<size_t>::iterator it = road.begin();it!=road.end() && R > 0;it++){
				R--;
				money += cheats[*it].money;
			}
		}else{
			for(list<size_t>::iterator it = way.begin();it!=way.end() && R > 0;it++){
				R--;
				money += cheats[*it].money;
			}
		}
	}
	return 0;
}