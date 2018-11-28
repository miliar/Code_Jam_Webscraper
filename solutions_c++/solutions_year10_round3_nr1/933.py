
#include <math.h>
#include <iostream>
#include <fstream>
#include <limits.h>
#include <list>
#include <deque>

#define F(a,b,c) for(size_t a = b;a != c;a++)
#define FF(a,b,c) for(size_t a = b;a != c-1;a--)

using namespace std;

int main(){
	ifstream input("inputA.txt");
	ofstream output("outputA.txt");
	size_t T;
	input >> T;
	deque<pair<int,int>> points1;
	deque<pair<int,int>> points2;
	size_t N,a;
	pair<int,int> mp1,mp2,mp3;
	F(i,0,T){
		cout << i+1<<endl;
		input >> N;
		a = 0;
		points1.clear();
		points2.clear();
		F(j,0,N){
			input >> mp1.first >> mp1.second;
			points1.push_back(mp1);
		}
		F(j,0,points1.size()){
			F(k,0,points1.size()){
				//cout << points1[j].first << " " << points1[k].first << " " << points1[j].second << " " << points1[k].second<<endl;
				if((points1[j].first < points1[k].first && points1[j].second > points1[k].second)
					//||(points1[j].first < points1[k].first && points1[j].second > points1[k].second)
				){
					a++;
				}
			}
		}
		output << "Case #"<<(i+1)<<": "<< a <<"\n";
	}
	return 0;
}