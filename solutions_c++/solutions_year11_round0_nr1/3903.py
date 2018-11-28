#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");

int Ostate,Bstate,Case = 0,Test,sum,N;
vector<int>button,orange,blue;

int Abs(int num) {
	return (num > 0)? num : -num;
}

int main() {
	int i,j,k,n,temp,cnt;
	char ch;
	fin >> Test;
	while(Test > 0) {
		--Test;
		cnt = -1;
		button.clear();
		blue.clear();
		orange.clear();
		Ostate = Bstate = 1;
		sum = 0;
		fin >> N;
		for(i = 0; i < N;++i) {
			fin >> ch;
			fin >> n;
			button.push_back(n);
			if(ch == 'O') {
				orange.push_back(i);
			}
			else {
				blue.push_back(i);
			}
		}
		while(1) {
			++cnt;
			if((button.size() - cnt) == 0)break;
			if(orange.size() == 0) {
				for(i = 0;i < blue.size();++i) {
					sum += ( Abs( button[blue[i]] - Bstate ) + 1 );
					Bstate = button[blue[i]];
				}
				break;
			}
			if(blue.size() == 0) {
				for(i = 0;i < orange.size();++i) {
					sum += ( Abs( button[orange[i]] - Ostate ) + 1);
					Ostate = button[orange[i]];
				}
				break;
			}
			temp = button[cnt];
			j = orange[0];
			k = blue[0];
			if(j < k) {// orange first
				int secondsorange = Abs(temp - Ostate) + 1;
				//if(secondsorange == 0)++secondsorange;
				int secondsblue = Abs(button[k] - Bstate);
				sum += secondsorange;
				Ostate = temp;
				if(Bstate <= button[k]) {
					if(secondsorange >= secondsblue) {
						Bstate = button[k];
					}
					else {
						Bstate += secondsorange;
					}
				}
				else {
					if(secondsorange >= secondsblue) {
						Bstate = button[k];
					}
					else {
						Bstate -= secondsorange;
					}
				}
				orange.erase(orange.begin());
			}
			else if(j > k) {// blue first
				int secondsorange = Abs(button[j] - Ostate);
				int secondsblue = Abs(temp - Bstate) + 1;
				if(secondsblue == 0)++secondsblue;
				sum += secondsblue;
				Bstate = temp;
				if(Ostate <= button[j]) {
					if(secondsblue >= secondsorange) {
						Ostate = button[j];
					}
					else {
						Ostate += secondsblue;
					}
				}
				else {
					if(secondsblue >= secondsorange) {
						Ostate = button[j];
					}
					else {
						Ostate -= secondsblue;
					}
				}
				blue.erase(blue.begin());
			}
			//button.erase(button.begin());
		}
		fout << "Case #" << ++Case << ": " << sum << endl;
	}
	return 0;
}