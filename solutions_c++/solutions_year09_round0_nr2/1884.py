#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

int t;

enum dir {
    NORTH, WEST, EAST, SOUTH
};

bool is_in_range(int y, int x, int h, int w) {
    return y >= 0 && y < h && x >= 0 && x < w;
}

bool is_sink(const std::vector<std::vector<int> >& f, int y, int x) {
    if(is_in_range(y-1,x,f.size(),f[0].size())) {
        if(f[y-1][x] < f[y][x]) return false;
    }
    if(is_in_range(y+1,x,f.size(),f[0].size())) {
        if(f[y+1][x] < f[y][x]) return false;
    }
    if(is_in_range(y,x-1,f.size(),f[0].size())) {
        if(f[y][x-1] < f[y][x]) return false;
    }
    if(is_in_range(y,x+1,f.size(),f[0].size())) {
        if(f[y][x+1] < f[y][x]) return false;
    }
    return true;
}

std::vector<std::pair<int,int> > find_sinks(const std::vector<std::vector<int> >& f) {
    std::vector<std::pair<int,int> > ret;
    for(int y = 0; y < f.size(); ++y) {
        for(int x = 0; x < f[y].size(); ++x) {
            if(is_sink(f,y,x)) {
                ret.push_back(std::make_pair(y,x));
            }
        }
    }
    return ret;
}

std::pair<int,int> next_flow(const std::vector<std::vector<int> >& field, int y, int x) {
	std::vector<std::pair<int,dir> > order;

    if(is_in_range(y-1,x,field.size(),field[0].size())) {
        order.push_back(std::make_pair(field[y-1][x],NORTH));
    }
    if(is_in_range(y+1,x,field.size(),field[0].size())) {
        order.push_back(std::make_pair(field[y+1][x],SOUTH));
    }
    if(is_in_range(y,x-1,field.size(),field[0].size())) {
        order.push_back(std::make_pair(field[y][x-1],WEST));
    }
    if(is_in_range(y,x+1,field.size(),field[0].size())) {
        order.push_back(std::make_pair(field[y][x+1],EAST));
    }

    std::sort(order.begin(),order.end());
    
    switch(order[0].second) {
        case NORTH:
            return std::make_pair(y-1,x);
        case WEST:
            return std::make_pair(y,x-1);
        case EAST:
            return std::make_pair(y,x+1);
    }

    return std::make_pair(y+1,x);
}

char rec(std::vector<std::vector<int> >& cf, const std::vector<std::vector<int> >& field, int y, int x) {
    if(cf[y][x] != -1) {
        return cf[y][x]; 
    }
    std::pair<int,int> next = next_flow(field,y,x);
    return cf[y][x] = rec(cf,field,next.first,next.second);
}

int main() {
    std::cin>>t;	

    for(int a = 0; a < t; ++a) {
        int h,w;
        std::cin>>h>>w; 

        std::vector<std::vector<int> > field(h,std::vector<int>(w));

        for(int y = 0; y < h; ++y) {
            for(int x = 0; x < w; ++x) {
                std::cin>>field[y][x];
            }
        }

        std::vector<std::pair<int,int> > sinks = find_sinks(field);

        std::cout<<"Case #"<<a+1<<":"<<std::endl;
        /*
        for(int j = 0; j < sinks.size(); ++j) {
            std::cout<<sinks[j].first<<" "<<sinks[j].second<<std::endl;
        }
        */

        std::sort(sinks.begin(),sinks.end());

        std::vector<std::vector<int> > cf(h,std::vector<int>(w));

        for(int i = 0; i < cf.size(); ++i) {
            for(int j = 0; j < cf[0].size(); ++j) {
                 cf[i][j] = -1;
            }
        }

        for(int i = 0; i < sinks.size(); ++i) {
            cf[sinks[i].first][sinks[i].second] = i+1;
        }

        for(int y = 0; y < cf.size(); ++y) {
            for(int x = 0; x < cf[0].size(); ++x) {
            	if(cf[y][x] == -1) cf[y][x] = rec(cf,field,y,x); 
            }
        }

        char next = 'a';
        std::map<int,char> rplc;

        for(int y = 0; y < cf.size(); ++y) {
            for(int x = 0; x < cf[0].size(); ++x) {
                if(rplc[cf[y][x]] == 0) {
                    rplc[cf[y][x]] = next;
                    next++;
                } 
            }
        }

        for(int y = 0; y < cf.size(); ++y) {
            for(int x = 0; x < cf[0].size(); ++x) {
                std::cout<<rplc[cf[y][x]]<<" ";
            }
            std::cout<<std::endl;
        }
    }

    return 0;
}
