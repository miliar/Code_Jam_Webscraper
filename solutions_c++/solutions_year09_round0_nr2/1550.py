#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
using namespace std;

#define MAXALT 10001

unsigned int TC, tc, Row, row, Col, col, i, j;

struct Array{
	int alt;
	int basin;
	char label;
};
Array arr[102][102];//boundary row has MAXALT to guard boundary cases
typedef multimap<int,int> IntIntMMap;
IntIntMMap coll;

typedef map<int,char> IntCharMap;
IntCharMap map1;

bool isSink(int r, int c){
	int alt = arr[r][c].alt;
	if((alt <= arr[r-1][c].alt) && (alt <= arr[r+1][c].alt) && (alt <= arr[r][c-1].alt) && (alt <= arr[r][c+1].alt))
		return true;
	return false;
}

Array * flowsInto(int r, int c){
	int alt1 = arr[r-1][c].alt;
	if((alt1 <= arr[r][c-1].alt) && (alt1 <= arr[r][c+1].alt) && (alt1 <= arr[r+1][c].alt) )
		return &arr[r-1][c];
	else if ((arr[r][c-1].alt <= arr[r][c+1].alt) && (arr[r][c-1].alt <= arr[r+1][c].alt))
		return &arr[r][c-1];
	else if (arr[r][c+1].alt <= arr[r+1][c].alt)
		return &arr[r][c+1];
	else
		return &arr[r+1][c];
}

int main(){
	cin >> TC;
	for(tc=0; tc<TC; ++tc){
		//Input
		cin >> Row;
		cin >> Col;
		coll.clear();
		for(row=0; row<Row+2; ++row){
			for(col=0; col<Col+2; ++col){
				if((row == 0) || (col == 0) || (row == Row+1) || (col == Col+1) )
					arr[row][col].alt = MAXALT;
				else{
					cin >> arr[row][col].alt;
					arr[row][col].basin = -1;
					coll.insert(make_pair(arr[row][col].alt, row*(Col+2) + col));
				}
			}
		}

		//while list1 is not empty
		IntIntMMap::iterator pos;
		int nxtBasin = 0;
		for (pos = coll.begin(); pos != coll.end(); ++pos) {
			if(isSink(pos->second/(Col+2), pos->second % (Col+2))){
				arr[pos->second/(Col+2)][pos->second % (Col+2)].basin = nxtBasin++;
			} else {
				arr[pos->second/(Col+2)][pos->second % (Col+2)].basin = flowsInto(pos->second/(Col+2), pos->second % (Col+2))->basin;
			}
		}

		//Update labels
		char nextLabel = 'a';
		IntCharMap::iterator pos1;
		map1.clear();
		for(row=1; row<Row+1; ++row){
			for(col=1; col<Col+1; ++col){
				pos1 = map1.find(arr[row][col].basin);
				if (pos1 == map1.end()) {
					arr[row][col].label = nextLabel;
					map1[arr[row][col].basin] = nextLabel++;
				} else {
					arr[row][col].label = map1[arr[row][col].basin];
				}
			}
		}

		//Output
		cout << "Case #" << tc+1 << ":" << endl;
		for(row=1; row<Row+1; ++row){
			for(col=1; col<Col+1; ++col){
				cout << arr[row][col].label << " ";
			}
			cout << endl;
		}
	}
	return 0;
}