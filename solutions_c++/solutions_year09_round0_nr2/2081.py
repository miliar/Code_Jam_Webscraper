#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

char router(vector<vector<int> >& heights, int col, int row, vector<pair<int,int> >& sinks){
	int max_descent =0;
	char route = 'D';
	int descent;
	if(row>0 && (descent = heights[col][row]-heights[col][row-1])>max_descent){
		route = 'N';
		max_descent = descent;
	}
	if(col>0 && (descent = heights[col][row]-heights[col-1][row])>max_descent){
		route = 'W';
		max_descent = descent;
	}
	if(col<heights.size()-1 && (descent = heights[col][row]-heights[col+1][row])>max_descent){
		route = 'E';
		max_descent = descent;
	}
	if(row<heights[0].size()-1 && (descent = heights[col][row]-heights[col][row+1])>max_descent){
		route = 'S';
		max_descent = descent;
	}
	if(route == 'D')
		sinks.push_back(pair<int,int>(col, row));
	return route;
}

//void label(vector<vector<char> >& route, int col, int row, char label);

void label(vector<vector<char> >& route, int col, int row, char labels){
	route[col][row] = labels;
	if(row>0 && route[col][row-1] == 'S'){
		label(route, col, row-1, labels);
	}
	if(col>0 && route[col-1][row] == 'E'){
		label(route, col-1, row, labels);
	}
	if(col<route.size()-1 && route[col+1][row] == 'W'){
		label(route, col+1, row, labels);
	}
	if(row<route[0].size()-1 && route[col][row+1] == 'N'){
		label(route, col, row+1, labels);
	}
	return;
} 





int main(int argc, int argv[]){


	ifstream input("input.txt");
	ofstream output("output.txt");
	int maps;
	input >> maps;
	for(int i=0; i<maps; i++){
		int height, width;
		input >> height >> width;
		vector<vector<int> > heights(width, vector<int>(height, 0));
		for(int j=0; j<height; j++){
			for(int k=0; k<width; k++){
				input >> heights[k][j];
			}
		}
		vector<vector<char> > route(width, vector<char>(height, 'A'));
		vector<pair<int, int> > sinks;
		for(int j=0; j<height; j++){
			for(int k=0; k<width; k++){
				route[k][j] = router(heights, k, j, sinks);
			}
		}
		for(int l=0; l<sinks.size(); l++){
			label(route, sinks[l].first, sinks[l].second, (char)('a'+l) );
		}
		output << "Case #" << i+1 << ":\n";
		char conv[26];	
		for(int i=0;i<26;i++)
			conv[i]='Ø';
		int sink_nr =0;
		for(int j=0; j<height; j++){
			for(int k=0; k<width; k++){
				char out = route[k][j];
				int pos = int(out)-int('a');
				if(conv[pos] == 'Ø'){
					conv[pos] = (char)('a' + sink_nr);
					sink_nr++;
				}
				output << conv[pos] << ((k==width-1)? "\n" : " ");
			}
		}
	}
}
				
		
		
