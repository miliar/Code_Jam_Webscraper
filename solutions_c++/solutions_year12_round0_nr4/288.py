#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <utility>

std::pair<int, int> reduction(std::pair<int, int> const& v)
{
    int a = v.first;
    int b = v.second;
    
    if(a == 0 && b == 0) return std::make_pair(0, 0);
    else if(a == 0) return std::make_pair(0, (b>0)?1:-1);
    else if(b == 0) return std::make_pair((a>0)?1:-1, 0);
    
    for(int i = std::min(std::abs(a), std::abs(b)); i > 1; --i){
        if((a % i == 0) && (b % i == 0)){
            a /= i;
            b /= i;
            break;
        }
    }
    return std::make_pair(a, b);
}

int main()
{
    int t;
    std::cin >> t;
    
    
    std::ofstream out("small.txt");
    for(int i = 0; i < t; ++i){
        int h, w, d;
        std::cin >> h >> w >> d;
        
        std::vector<std::string> map;
        int x, y;
        for(int j = 0; j < h; ++j){
            std::string s;
            std::cin >> s;
            map.push_back(s);
            if(s.find('X') != std::string::npos){
                x = (s.find('X') - 1) * 2 + 1;
                y = (j - 1) * 2 + 1;
                std::cout << x << " " << y << std::endl;
            }
        }
        
        w -= 2;
        h -= 2;
        std::cout << "h=" << h << ", " << "w=" << w << std::endl;
        std::set<std::pair<int,int>> vec;
        int dd = d*d;
        int hmax = 200;
        int wmax = 200;
        for(int a = -hmax; a <= hmax; ++a){
        for(int b = -wmax; b <= wmax; ++b){
            int px = w * b;
            int py = h * a;
            if((b % 2) != 0){
                px = w * b + w - x;
            }
            if((a % 2) != 0){
                py = h * a + h - y;
            }
            if(px != 0 || py != 0){
                if((px * px + py * py) <= dd){
                    vec.insert(reduction(std::make_pair(py, px)));
                }
            }
        }}
        auto it = vec.begin();
        auto end = vec.end();
        while(it != end){
            std::cout << it->first << "/2 " << it->second << "/2" << std::endl;
            ++it;
        }
        std::cout << std::endl;
        out << "Case #" << i + 1 << ": " << vec.size() << std::endl;
    }
}

