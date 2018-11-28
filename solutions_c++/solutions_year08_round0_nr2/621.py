#include<algorithm>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
using namespace std;

#define NUM_TYPE	 int
struct Num{NUM_TYPE nVal;string sVal;Num(string str){sVal = str;istringstream stream(sVal);stream >> nVal;}Num(NUM_TYPE n){nVal = n;ostringstream stream(sVal);stream << fixed << n;sVal = stream.str();}};

vector<string> split(string str, string pattern){

	vector<string> vec;
	string current = "";
	for(int i = 0 ; i < str.size() ; i++){
		if(str.substr(i, pattern.size()) == pattern){
			i+=pattern.size()-1;
			if(current.size() > 0)
				vec.push_back(current);
			current = "";
		}else
			current += str[i];
	}
	if(current.size() > 0)
		vec.push_back(current);
	return vec;
}
///////////////////////////

int T, NA, NB;
struct trip{
	int h1, m1, h2, m2, s;
	bool operator<(const trip& t)const{
		return make_pair(h1,m1) < make_pair(t.h1,t.m1) ||
		(make_pair(h1,m1) == make_pair(t.h1,t.m1) && make_pair(h2,m2) < make_pair(t.h2,t.m2));
	}
};
vector<trip> table;

trip getTrip(string s1, string s2, int s){
	
	vector<string> v1 = split(s1, ":");
	Num n1(v1[0]), n2(v1[1]);
	
	vector<string> v2 = split(s2, ":");
	Num n3(v2[0]), n4(v2[1]);
	
	
	trip t = {n1.nVal, n2.nVal, n3.nVal, n4.nVal, s};
	return t;
}

struct train{
	int h, m;	//to go
	int s;
};
vector<train> trains;

int getTrain(int h, int m, int s){
	
	for(int i = 0 ; i < trains.size() ; i++){
		if(trains[i].s != s)continue;
		if(make_pair(trains[i].h, trains[i].m) <= make_pair(h,m))
			return i;
	}
	return -1;
}

int main(){
	
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);	
	
	int tt; cin >> tt;
	for(int t = 0 ;t < tt ; t++){
		
		table.clear();
		trains.clear();
		//
		
		cin >> T >> NA >> NB;
		int i;
		for(i = 0 ; i < NA ; i++){
			string s1, s2; cin >> s1 >> s2;
			table.push_back(getTrip(s1,s2,0));
		}
		for(i = 0 ; i < NB ; i++){
			string s1, s2; cin >> s1 >> s2;
			table.push_back(getTrip(s1,s2,1));
		}
		sort(table.begin(), table.end());
		
		int r[2] = {0,0};
		for(i = 0 ; i < table.size() ; i++){
			int index = getTrain(table[i].h1, table[i].m1, table[i].s);
			if(index == -1){	//no train
				train nt = {table[i].h1, table[i].m1, table[i].s};
				trains.push_back(nt);
				index = trains.size()-1;
				r[table[i].s]++;
			}
			
			//make trip
			trains[index].s = (trains[index].s+1)%2;
			
			trains[index].h = table[i].h2;
			trains[index].m = table[i].m2;
			trains[index].m += T;
			if(trains[index].m >= 60){
				trains[index].m %= 60;
				trains[index].h++;
			}
		}
		
		cout << "Case #" << t+1 << ": " << r[0] << " " << r[1] << endl;
	}
	
	return 0;
}
