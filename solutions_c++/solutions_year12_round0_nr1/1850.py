#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
char mapp[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    std::vector<bool> flag(26, false);
    
    ifstream ifs("c:/io.txt");
    ofstream ofs("c:/out.txt");
    int num;
    ifs >> num;
    for(size_t i = 0; i < num + 1; ++i){
        string str;
        getline(ifs, str);
        if(i == 0)
            continue;
        cout << str << endl;
        for(size_t j = 0; j < str.length(); ++j) {
            if(str[j] != ' '){
                int index = int(str[j] - 'a');
                str[j] = mapp[index];
            }
        }
        ofs << "Case #" << i << ": " << str << endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
