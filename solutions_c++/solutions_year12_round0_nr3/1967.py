#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int mov(int aa, int a, int b){
    int sum = 0;
    char ch[10];
    itoa(aa, ch, 10);
    string str(ch);
    vector<int> su;
    for(size_t i = str.length() - 1; i >0; --i){
        string tmp = str.substr(str.length() - 1, 1) + str.substr(0, str.length() - 1);
        int tt = atoi(tmp.c_str());
        if(tt <= b && tt >= a && tt != aa && tt > aa){
//            cout << aa << " " << tt << endl;
            if(find(su.begin(), su.end(), tt) == su.end()){
                su.push_back(tt);
                sum++;
            }
        }
        str = tmp;
    }
    return sum;
}

int main()
{
    ifstream ifs("c:/io.txt");
    ofstream ofs("c:/out.txt");
    int num;
    ifs >> num;
    for(size_t i = 0; i < num; ++i){
        int a, b, sum = 0;
        ifs >> a >> b;
        for(int j = a; j <= b; ++j){
            sum += mov(j, a, b);
        }
        ofs << "Case #" << i + 1 << ": " << sum << endl;
    }
    ifs.close();
    ofs.close();
    system("pause");
    return 0;
}
