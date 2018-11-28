#include <iostream>
#include <set>
#include <vector>
#include <string>

int l,d,n;

int main() {
	std::cin>>l>>d>>n;
	std::vector<std::string> words(d);

    for(int i = 0; i < d; ++i) {
        std::cin>>words[i];
    }

    for(int i = 0; i < n; ++i) {
        std::string input;
        std::cin>>input;

        std::vector<std::set<char> > choices(l);
        int index = 0;
        int ci = 0;
        while(index < l) {
            if(input[ci] == '(') {
                ++ci;
                while(input[ci] != ')') {
                    choices[index].insert(input[ci]);
                    ++ci;
                }
                ++ci;
            } else {
                choices[index].insert(input[ci]);
                ++ci;
            }
            ++index;
        }

        int sum = 0;

        for(int j = 0; j < words.size(); ++j) {
        	bool ok = true;
            for(int k = 0; k < choices.size(); ++k) {
                if(choices[k].count(words[j][k]) == 0) {
                    ok = false;
                    break;
                }
            }
            if(ok) ++sum;
        }

        std::cout<<"Case #"<<i+1<<": "<<sum<<std::endl;
    }

    return 0;
}
