#include<fstream>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class level{
public:
	int one, two;
	bool fone, ftwo;
};

bool comp(level a, level b){
	return a.two < b.two;
}

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open("1.txt");
	outfile.open("2.txt");
	int T, N, a, b;
	level temp;
	temp.fone = temp.ftwo = false;
	vector<level> levels;
	infile >> T;
	for(int i = 0; i < T; i++){
		infile >> N;
		for(int j = 0; j < N; j++){
			infile >> a >> b;
			temp.one = a;
			temp.two = b;
			levels.push_back(temp);
		}
		sort(levels.begin(),levels.end(),comp);
		int x = 0, y = 0, z = 0, t = 0;
		bool loop;
		while(x != 2*N){
			//cout << i << " " << x << endl;
			loop = true;
			for(int i = y; i < N;){
				if(levels[i].two <= x && !levels[i].ftwo){
					if(levels[i].one <= x && !levels[i].fone){
						levels[i].fone = true; x++;
					}
					levels[i].ftwo = true; x++; y++; t++; i++;
					loop = false;
				}
				else{
					for(int j = N-1; j >= 0; j--){
						if(levels[j].one <= x && !levels[j].fone){
							levels[j].fone = true; x++; t++;
							loop = false;
							break;
						}
					}
					break;
				}
			}
			if(loop) break;
		}
		if(loop) outfile << "Case #" << i+1 << ": Too Bad" << endl;
		else outfile << "Case #" << i+1 << ": " << t << endl;
		levels.clear();
	}
	return 0;
}
	