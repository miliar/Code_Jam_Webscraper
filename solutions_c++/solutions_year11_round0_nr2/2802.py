#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int getindex(char temp);
void cleards();
vector<char> getlist(string elements, int n);
vector<char> trycombine(vector<char> list);
vector<char> tryoppose(vector<char> list);
char combine[8][8];
bool oppose[8][8];
int main() {
	int t;
	int c, d, n, x, y;
	string temp;
	vector<char> list;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cleards();
		cin>>c;
		for(int j=0;j<c;j++){
			cin>>temp;
			x = getindex(temp[0]);
			y = getindex(temp[1]);
			combine[x][y] = temp[2];
			combine[y][x] = temp[2];
		}
		cin>>d;
		for(int j=0;j<d;j++){
			cin>>temp;
			x = getindex(temp[0]);
			y = getindex(temp[1]);
			oppose[x][y] = 1;
			oppose[y][x] = 1;
		}
		cin>>n;
		cin>>temp;
		cout<<"Case #"<<i<<": [";
		list = getlist(temp,n);
		if(list.empty()) {
			cout<<"]"<<endl;
		}
		else {
	 		for(int l=0;l<list.size()-1;l++) {
	 			cout<<list[l]<<", ";
	 		}
	 		cout<<list.back()<<"]"<<endl;
 		}
	}
}

int getindex(char temp) {
	if(temp == 'Q')
		return 0;
	else if(temp == 'W')
		return 1;
	else if(temp == 'E')
		return 2;
	else if(temp == 'R')
		return 3;
	else if(temp == 'A')
		return 4;
	else if(temp == 'S')
		return 5;
	else if(temp == 'D')
		return 6;
	else if(temp == 'F')
		return 7;		
	else
		return -1;
}

void cleards() {
	for(int i=0;i<8;i++) {
		for(int j=0;j<8;j++) {
			combine[i][j] = ' ';
			oppose[i][j] = false;
		}
	}	
}


vector<char> getlist(string elements, int n) {
	vector<char> list;
	for(int i=0;i<n;i++) {
		list.push_back(elements[i]);
		list = trycombine(list);
		list = tryoppose(list);
	}
	return list;	
}

vector<char> trycombine(vector<char> list) {
	if(list.size()>=2) {
		int x = getindex(list.back());
		int y = getindex(list[list.size()-2]);
		if(x>=0 && y>=0) {
			char ch = combine[x][y];
			if(ch != ' ') {
				list.pop_back();
				list.pop_back();
				list.push_back(ch);
			}
		}
	}
	return list;
}
vector<char> tryoppose(vector<char> list) {
	int x = getindex(list.back());
	int y;
	if(x>=0) {
		for(int i=0;i<list.size()-1;i++) {
			y = getindex(list[i]);
			if(y>=0 && oppose[x][y]) {
				list.clear();			
				break;
			}		
		}
	}
	return list;
}

