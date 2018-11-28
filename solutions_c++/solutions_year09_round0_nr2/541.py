#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int GetInput(
	const std::string &file_name,
	std::vector<std::vector<std::vector<unsigned int> > > *map_list
);
void OutputData(
	const std::vector<std::vector<std::vector<unsigned int> > > &map_list
);
std::vector<std::vector<std::vector<char> > > Solve(
	const std::vector<std::vector<std::vector<unsigned int> > > &map_list
);
bool GetNext(
	const std::vector<std::vector<unsigned int> > &map,
	const unsigned int h, const unsigned int w,
	unsigned int *next_h, unsigned int *next_w
);
void Replace(
	const unsigned int h,
	const unsigned int w,
	const char old_char,
	const char new_char,
	std::vector<std::vector<char> > *map
);
int OutputResult(const std::vector<std::vector<std::vector<char> > > &map_list);

//=========================================================================//
//     Main
//=========================================================================//
int main(int argc, char *argv[]){
	std::string file_name;
	if(argc > 1){
		file_name = argv[1];
	}
	else{
		file_name = "./test.txt";
	}

	std::vector<std::vector<std::vector<unsigned int> > > map_list;
	GetInput(file_name, &map_list);
	//OutputData(map_list);

	std::vector<std::vector<std::vector<char> > > result = Solve(map_list);
	OutputResult(result);
}

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(
	const std::string &file_name,
	std::vector<std::vector<std::vector<unsigned int> > > *map_list
){
	// File Open
	std::ifstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}
	// Input
	unsigned int T, H, W;
	file >> T;
	map_list->resize(T);
	for(unsigned int i=0; i<T; ++i){
		file >> H >> W;
		(*map_list)[i].resize(H);
		for(unsigned int h=0; h<H; ++h){
			(*map_list)[i][h].resize(W);
			for(unsigned int w=0; w<W; ++w){
				file >> (*map_list)[i][h][w];
			}
		}
	}

	return 0;
}

//=========================================================================//
//     Output Data
//=========================================================================//
void OutputData(const std::vector<std::vector<std::vector<unsigned int> > > &map_list){
	using std::cout;
	using std::endl;

	cout << map_list.size() << endl;
	for(unsigned int i=0; i<map_list.size(); ++i){
		cout << map_list[i].size() << " " << map_list[i][0].size() << endl;
		for(unsigned int h=0; h<map_list[i].size(); ++h){
			for(unsigned int w=0; w<map_list[i][h].size(); ++w){
				cout << map_list[i][h][w] << " ";
			}
			cout << endl;
		}
	}
}

//=========================================================================//
//     Solve
//=========================================================================//
std::vector<std::vector<std::vector<char> > > Solve(
	const std::vector<std::vector<std::vector<unsigned int> > > &map_list
){
	std::vector<std::vector<std::vector<char> > > result;

	// Initialize Result
	result.resize(map_list.size());
	for(unsigned int i=0; i<map_list.size(); ++i){
		result[i].resize(map_list[i].size());
		for(unsigned int h=0; h<map_list[i].size(); ++h){
			result[i][h].resize(map_list[i][h].size());
		}
	}

	unsigned int next_h, next_w, current_h, current_w;
	char next_char, current_char;
	for(unsigned int i=0; i<map_list.size(); ++i){
		next_char = 'a';
		for(unsigned int h=0; h<map_list[i].size(); ++h){
			for(unsigned int w=0; w<map_list[i][h].size(); ++w){
				if(result[i][h][w] != 0){
					continue;
				}
				
				current_h = h;
				current_w = w;
				current_char = 0;
				do{
					if(!GetNext(map_list[i], current_h, current_w, &next_h, &next_w)){
						// this cell is sink
						if(current_char == 0){
							result[i][current_h][current_w] = next_char;
							next_char += 1;
						}
						else{
							result[i][current_h][current_w] = current_char;
						}
						break;
					}

					if(result[i][next_h][next_w] != 0){
						if(current_char != 0){
							next_char -= 1;
							Replace(current_h, current_w, current_char, result[i][next_h][next_w], &result[i]);
							break;
						}
						else{
							result[i][current_h][current_w] = result[i][next_h][next_w];
						}
						break;
					}

					if(current_char == 0){
						current_char = next_char;
						next_char += 1;
					}
					result[i][current_h][current_w] = current_char;
					current_h = next_h;
					current_w = next_w;
				}while(1);
			}
		}
	}

	return result;
}

bool GetNext(
	const std::vector<std::vector<unsigned int> > &map,
	const unsigned int h, const unsigned int w,
	unsigned int *next_h, unsigned int *next_w
){
	static const int NOT_FOUND = 0xffffffff;
	unsigned int min = map[h][w];
	*next_h = NOT_FOUND;
	*next_w = NOT_FOUND;
	// North
	if(h > 0 && min > map[h-1][w]){
		*next_h = h-1;
		*next_w = w;
		min = map[*next_h][*next_w];
	}
	// West
	if(w > 0 && min > map[h][w-1]){
		*next_h = h;
		*next_w = w-1;
		min = map[*next_h][*next_w];
	}
	// East
	if(w+1 < map[0].size() && min > map[h][w+1]){
		*next_h = h;
		*next_w = w+1;
		min = map[*next_h][*next_w];
	}
	// South
	if(h+1 < map.size() && min > map[h+1][w]){
		*next_h = h+1;
		*next_w = w;
		min = map[*next_h][*next_w];
	}
	if(*next_h == NOT_FOUND){
		return false;
	}
	return true;
}

void Replace(
	const unsigned int h,
	const unsigned int w,
	const char old_char,
	const char new_char,
	std::vector<std::vector<char> > *map
){
	// North
	if(h > 0 && (*map)[h-1][w] == old_char){
		(*map)[h-1][w] = new_char;
		Replace(h-1, w, old_char, new_char, map);
	}
	// West
	if(w > 0 && (*map)[h][w-1] == old_char){
		(*map)[h][w-1] = new_char;
		Replace(h, w-1, old_char, new_char, map);
	}
	// East
	if(w+1 < (*map)[0].size() && (*map)[h][w+1] == old_char){
		(*map)[h][w+1] = new_char;
		Replace(h, w+1, old_char, new_char, map);
	}
	// South
	if(h+1 < (*map).size() && (*map)[h+1][w] == old_char){
		(*map)[h+1][w] = new_char;
		Replace(h+1, w, old_char, new_char, map);
	}
}

//=========================================================================//
//     Output Result
//=========================================================================//
int OutputResult(const std::vector<std::vector<std::vector<char> > > &map_list){
	using std::cout;
	using std::endl;

	std::string file_name = "./result.txt";
	std::ofstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	for(unsigned int i=0; i<map_list.size(); ++i){
		file << "Case #" << (i+1) << ":" << endl;
		cout << "Case #" << (i+1) << ":" << endl;
		for(unsigned int h=0; h<map_list[i].size(); ++h){
			for(unsigned int w=0; w<map_list[i][h].size(); ++w){
				file << map_list[i][h][w];
				cout << map_list[i][h][w];
				if(w != map_list[i][h].size()-1){
					file << " ";
					cout << " ";
				}
			}
			file << endl;
			cout << endl;
		}
	}

	file.close();
	return 0;
}