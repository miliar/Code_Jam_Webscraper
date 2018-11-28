
#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include <limits.h>

unsigned min_cost = INT_MAX;

unsigned calcCost(const std::vector<char> &cell_state, unsigned release_num){
    unsigned cost = 0;
    for(unsigned i = release_num+1; i < cell_state.size(); i++){
        if(cell_state[i] == 0){
            break;
        }
        cost++;
    }

    for(int i = release_num-1; i >= 0; i--){
        if(cell_state[i] == 0){
            break;
        }
        cost++;
    }
    return cost;
}   

unsigned solve(std::vector<char> cell_state, std::vector<unsigned> release_cells, unsigned cur_cost){
    if(cur_cost > min_cost){
        return cur_cost;
    }

    if(release_cells.size() == 0){
        return cur_cost;
    }

    unsigned min = INT_MAX;
    for(unsigned i = 0; i < release_cells.size(); i++){
        std::vector<char> new_cell_state = cell_state;
        std::vector<unsigned> new_release_cells = release_cells;

        new_cell_state[release_cells[i]] = 0;
        new_release_cells[i] = new_release_cells.back();
        new_release_cells.pop_back();

        unsigned r = solve(new_cell_state, new_release_cells, cur_cost + calcCost(cell_state, release_cells[i]));
        if(r < min){
            min = r;
        }
    }

    return min;
}

int main(int argc, char **argv){
    unsigned num_cases;
    std::cin >> num_cases;
    for(unsigned i = 0; i < num_cases; i++){
        unsigned num_cells, num_releases;
        std::cin >> num_cells;
        std::cin >> num_releases;

        std::vector<unsigned> released_cells;
        for(unsigned j = 0; j < num_releases; j++){
            unsigned r;
            std::cin >> r;
            released_cells.push_back(r-1);
        }

        std::vector<char> cells;
        for(unsigned j = 0; j < num_cells; j++){
            cells.push_back(1);
        }

        unsigned result = solve(cells, released_cells, 0);
        std::cout << "Case #" << i+1 << ": " << result << std::endl;
        
    }

    return 0;
}
