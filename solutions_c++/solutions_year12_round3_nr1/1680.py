#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int num_trials;

int adj[1001][1001]; // adj[x][y] = num paths from x to y

int num_nodes;
int num_paths;

string answer;

void clear_adj() {
	for (int i = 1; i <= 1000; i++) { // just clear the important ones!
		for (int j = 1; j <= 1000; j++) {
			adj[i][j] = 0;
		}
	}
}
	
void print_adj() {
	for (int i = 1; i <= num_nodes; i++) {
		for (int j = 1; j <= num_nodes; j++) {
			cout << adj[i][j] << " ";
		}
		cout << endl;
	}
}

void process(int x, int y) {
	
//	cout << "\nNow processing " << x << " " << y << endl;
	
	adj[x][y] += 1; 
	if (adj[x][y] >= 2) {
		answer = "Yes";
	}

	for (int i = 1; i <= num_nodes; i++) {
		for (int j = 1; j <= num_nodes; j++) { 
			// new path from i -> x -> y -> j
			adj[i][j] += adj[i][x]*adj[y][j]; // new path from i -> x -> y
			if (adj[i][j] >= 2) {
				answer = "Yes";
			}
		}
	}
	// don't need to worry about i=x or j=y (overlap) because adj[x][x] = 0
	
	for (int i = 1; i <= num_nodes; i++) {
		adj[i][y] += adj[i][x]; // new path from i -> x -> y
		if (adj[i][y] >= 2) {
			answer = "Yes";
		}
	}
	
	for (int j = 1; j <= num_nodes; j++) {
		adj[x][j] += adj[y][j]; // new path from x -> y -> j
		if (adj[x][j] >= 2) {
			answer = "Yes";
		}
	}
	
	// don't need to worry about i=x or j=y (overlap) because adj[x][x] = 0
	
//	cout << endl;
//	print_adj();
}



int main(int argc, const char* argv[])  {
    ofstream fout ("a.out");
    ifstream fin ("a.in");

	fin >> num_trials;
	
	for (int trial = 1; trial <= num_trials; trial++) {
		fin >> num_nodes; // ugh...
		
		clear_adj();
		answer = "No";
		

		for (int x = 1; x <= num_nodes; x++) {
			fin >> num_paths; // num paths from x
			for (int y_i = 1; y_i <= num_paths; y_i++) { // don't actually use y_i
				int y;
				fin >> y;
				process(x,y);
			}
		}

		//cout << "Case #" << trial << ": " << answer  << endl;		
		//print_adj();
		//cout << endl;
		//cin.get();
		
		fout << "Case #" << trial << ": " << answer  << endl;
	}
	
}
