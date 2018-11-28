#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream IN("B-large.in");
ofstream OUT("B-large.out");

int get_min(string hour){
	int h = atoi(hour.substr(0,2).c_str());
	int m = atoi(hour.substr(3,2).c_str());
	return h*60+m;
}

bool available(int min, vector <int> &llegan){
	vector<int>::reverse_iterator rit = llegan.rbegin();
	for (;rit!=llegan.rend();rit++){
		if (*rit <= min){
			llegan.erase((rit+1).base());
			return true;
		}
	}
	return false;
}


int main(){
   int NC;
   IN >> NC;
   
   int turntime, ntfA, ntfB;
   
   for (int cas=1; cas<=NC; cas++){
		IN >> turntime;
		IN >> ntfA >> ntfB;
		
		vector <int> fromA, toB, fromB, toA;
		string h1, h2;
		
		for (int i=0;i<ntfA;i++){
			IN >> h1 >> h2;
			fromA.push_back(get_min(h1));
			toB.push_back(get_min(h2)+turntime);
		}
		
		for (int i=0;i<ntfB;i++){
			IN >> h1 >> h2;
			fromB.push_back(get_min(h1));
			toA.push_back(get_min(h2)+turntime);
		}
		
		sort(fromA.begin(), fromA.end());
		sort(fromB.begin(), fromB.end());
		sort(toA.begin(), toA.end());
		sort(toB.begin(), toB.end());
		
		/*
		OUT << "desde A:" << endl;
		for (int i=0;i<ntfA;i++){
			OUT << fromA[i] << "-->" << toB[i] << endl;
		}
		OUT << "desde B:" << endl;
		for (int i=0;i<ntfB;i++){
			OUT << fromB[i] << "-->" << toA[i] << endl;
		}
		*/
		
		int needA=0, needB=0;
		
		if (ntfB){
			for (int i=0; i<fromA.size(); i++){
				if (!available(fromA[i], toA)) needA++;
			}
		}
		else needA = ntfA;
		
		if (ntfA){
			for (int i=0; i<fromB.size(); i++){
				if (!available(fromB[i], toB)) needB++;
			}
		}
		else needB = ntfB;
		
		
		OUT << "Case #" << cas << ": " << needA << " " << needB << endl;
   }
}
