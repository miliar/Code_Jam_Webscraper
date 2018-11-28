
#include <iostream>
#include <cassert>
#include <vector>
#include <limits.h>
#include <map>

struct Map {
    std::vector<std::vector<unsigned> > heights; // indexed [y][x]
    std::vector<std::vector<int> > sink_locations;
    unsigned width, height;
};


unsigned getXCoord(int location, const struct Map &map){
    return location%map.width;
}

unsigned getYCoord(int location, const struct Map &map){
    return location/map.width;
}

int coordsToLocation(unsigned x, unsigned y, const struct Map &map){
    return x + y*map.width;
}

bool isMinimum(unsigned x, unsigned y, const struct Map &map){
    unsigned cur_val = map.heights[y][x];
    
    if(x > 0 && map.heights[y][x-1] < cur_val){
        return false;        
    }
    if(y > 0 && map.heights[y-1][x] < cur_val){
        return false;        
    }

    if(x < map.width-1 && map.heights[y][x+1] < cur_val){
        return false;        
    }
    if(y < map.height-1 && map.heights[y+1][x] < cur_val){
        return false;        
    }

    return true;
}

void findMinimumNeighbour(unsigned x, unsigned y, const struct Map &map, unsigned &rx, unsigned &ry){
    unsigned up_val = INT_MAX, down_val = INT_MAX, left_val = INT_MAX, right_val = INT_MAX;

    if(x > 0){ left_val = map.heights[y][x-1]; }
    if(y > 0){ up_val = map.heights[y-1][x]; }

    if(x < map.width-1){ right_val = map.heights[y][x+1]; }
    if(y < map.height-1){ down_val = map.heights[y+1][x]; }

    if(up_val <= down_val && up_val <= left_val && up_val <= right_val){
        rx = x;
        ry = y-1;
    }
    else if(left_val <= down_val && left_val <= right_val){
        rx = x-1;
        ry = y;
    }
    else if(right_val <= down_val){
        rx = x+1;
        ry = y;
    }
    else{
        rx = x;
        ry = y+1;
    }
}


int findSinkLocation(unsigned x, unsigned y, struct Map &map){
    if(map.sink_locations[y][x] != -1){
        return map.sink_locations[y][x];
    }

    if(isMinimum(x, y, map)){
        map.sink_locations[y][x] = coordsToLocation(x, y, map);
        return map.sink_locations[y][x];
    }

    unsigned nx, ny;
    findMinimumNeighbour(x, y, map, nx, ny);

    map.sink_locations[y][x] = findSinkLocation(nx, ny, map);
    return map.sink_locations[y][x];
}

void solveMap(struct Map &map){
    for(unsigned y = 0; y < map.height; y++){
        for(unsigned x = 0; x < map.width; x++){
            map.sink_locations[y][x] = findSinkLocation(x, y, map);
        }
    }
}

void printMap(struct Map map){
    std::cout << std::endl;
    for(unsigned y = 0; y < map.height; y++){
        for(unsigned x = 0; x < map.width; x++){
            std::cout << map.heights[y][x] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

void printSinkLocations(struct Map map){
    std::map<int, char> sink_to_char;
    char cur_char = 'a';

    for(unsigned y = 0; y < map.height; y++){
        for(unsigned x = 0; x < map.width; x++){
            int sl = map.sink_locations[y][x];
            std::map<int, char>::iterator it;

            it = sink_to_char.find(sl);
            if(it == sink_to_char.end()){
                sink_to_char[sl] = cur_char;
                std::cout << cur_char++ << " ";
            }
            else{
                std::cout << it->second << " ";
            }
        }
        std::cout << std::endl;
    }
}


int main(int argc, char **argv){
    unsigned num_maps = 0;
    std::cin >> num_maps;

    for(unsigned i = 0; i < num_maps; i++){
        struct Map new_map;
        std::cin >> new_map.height;
        std::cin >> new_map.width;

        for(unsigned y = 0; y < new_map.height; y++){
            std::vector<unsigned> row;
            for(unsigned x = 0; x < new_map.width; x++){
                unsigned h;
                std::cin >> h;
                row.push_back(h);
            }
            new_map.heights.push_back(row);

            std::vector<int> row_sink_locations(new_map.width, -1);
            new_map.sink_locations.push_back(row_sink_locations);
        }

        //printMap(new_map);
        solveMap(new_map);
        std::cout << "Case #" << i+1 << ":" << std::endl;
        printSinkLocations(new_map);
    }

    return 0;
}

