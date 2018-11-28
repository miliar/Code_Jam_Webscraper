#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>

int main(){
    int T;
    std::cin >> T;
    for(int t=1; t<=T; ++t){
        std::cout << "Case #" << t << ": ";
        std::vector<std::vector<bool> > oppos(26, std::vector<bool>(26, false));
        std::vector<std::vector<char> > combi(26, std::vector<char>(26, 0));

        int n;
        std::string buf;

        std::cin >> n; // Combinaisons
        for(int i=0; i<n; ++i){
            std::cin >> buf;
            combi[buf[0]-'A'][buf[1]-'A']=buf[2];
            combi[buf[1]-'A'][buf[0]-'A']=buf[2];
        }

        std::cin >> n;
        for(int i=0; i<n; ++i){
            std::cin >> buf;
            oppos[buf[0]-'A'][buf[1]-'A']=true;
            oppos[buf[1]-'A'][buf[0]-'A']=true;
        }

        std::cin >> n;
        std::cin.ignore(1, ' ');
        std::vector<int> nb(26, 0);
        std::list<char> ele;

        for(int i=0; i<n; ++i){
            char b;
            std::cin >> b;
            char c=ele.empty()?0:combi[b-'A'][ele.back()-'A'];
            if(c){
                nb[ele.back()-'A']--;
                nb[c-'A']++;
                ele.back()=c;
            } else {
                for(char x=0; x<26; ++x)
                    if(nb[x] && oppos[x][b-'A']){
                        std::fill(nb.begin(), nb.end(), 0);
                        ele.clear();
                        goto endcase;
                    }
                ele.push_back(b);
                nb[b-'A']++;
            }
            endcase:(void) 0;
        }
        std::cout << "[";
        if(!ele.empty()){
            for(std::list<char>::iterator it=ele.begin(); it!=ele.end(); ++it){
                std::list<char>::iterator next=it;
                if(++next!=ele.end())
                    std::cout << *it << ", ";
            }
            std::cout << ele.back();
        }
        std::cout << "]" << std::endl;
    }
}
