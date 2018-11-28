#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){

	//create input and output streams
	ifstream input("B-large.in");
	ofstream output("B-large.out");
	//create the holders for the ammount of maps, hwight and width
	int T, H, W;
	vector<vector<int> > currentMap;
	char nextBasin;
	int lowest, order;
	vector<vector<char> > currentBasins;

	//if both are open correctly, proceeds to solve the problem
	if( input && output ){
		//read the data from the first line
		input >> T;
		
		int counter; //counter for loops
		for(counter=0;counter<T;counter++){
			nextBasin='a';
			output << "Case #" << counter+1 << ":" << endl;
			input >> H;
			input >> W;
			currentMap.clear();
			currentBasins.clear();
			currentMap.resize( H, vector<int>(W));
			currentBasins.resize( H, vector<char>(W, 96));
//cout << "C" << counter+1 << endl;
			int i,j;
			for(i=0;i<H;i++){
				
				for(j=0;j<W;j++){
					input >> currentMap[i][j];
				}
			}

			for(i=0;i<H;i++){
				for(j=0;j<W;j++){
					lowest=currentMap[i][j];
bool usedNew=false;
order=0;
					if(i>0){
						if(currentMap[i-1][j]<lowest){
//							currentBasins[i][j]=currentBasins[i-1][j];
							lowest=currentMap[i-1][j];
							order=1;
						}
					}
					if(j>0){
						if(currentMap[i][j-1]<lowest){
//							currentBasins[i][j]=currentBasins[i][j-1];
							lowest=currentMap[i][j-1];
							order=2;
						}
					}
					if(j<W-1){
						if(currentMap[i][j+1]<lowest){
//							currentBasins[i][j+1]=nextBasin;
//							currentBasins[i][j]=nextBasin;
							lowest=currentMap[i][j+1];
							order=3;
//							nextBasin++;
						}
					}
					if(i<H-1){
						if(currentMap[i+1][j]<lowest){
//							currentBasins[i+1][j]=nextBasin;
//							currentBasins[i][j]=nextBasin;
							lowest=currentMap[i+1][j];
							order=4;
//							nextBasin++;
						}
					}
					currentBasins[i][j]=order;
				}
			}

			for(i=0;i<H;i++){
				
				for(j=0;j<W;j++){
					int curri=i;
					int currj=j;
//cout << "For " << i << " " << j << " n " << (int) currentBasins[i][j] << endl;
					while(currentBasins[curri][currj]<'a' && currentBasins[curri][currj]!=0){
						switch(currentBasins[curri][currj]){
							case 1: curri--; break;
							case 2: currj--; break;
							case 3: currj++; break;
							case 4: curri++; break;
						}
					}
					if(currentBasins[curri][currj]==0){
						currentBasins[curri][currj]=nextBasin;
						nextBasin++;
					}
					currentBasins[i][j]=currentBasins[curri][currj];
				}
			}

	
			for(i=0;i<H;i++){
				
				for(j=0;j<W;j++){
					output << (j!=0 ? " " : "" ) << currentBasins[i][j];
					
				}
				output << endl;
			}

		}
	
	}
	input.close();
	output.close();
	return 0;
}

