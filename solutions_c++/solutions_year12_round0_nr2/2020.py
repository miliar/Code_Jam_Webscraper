#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

string convStr(int j){
    ostringstream conv;
    conv  << j;
    string t = conv.str();
    return t;
}

int main(int argc, const char * argv[])
{
    ifstream input("/Users/vajda/Desktop/prog/googleCodeJam/b/b/input.txt");
    ofstream output("/Users/vajda/Desktop/prog/googleCodeJam/b/b/output.txt");
    int T;
    input >> T;
    for(int i=0;i<T;i++){
        cout << "Case: " <<  i << endl;
        output << "Case #" << i+1 << ": ";
        
        int N,S,p, count=0;
        input >> N >> S >> p;
        if(p<2) S=0;
        for(int j=0;j<N;++j){
            int t;
            input >> t;
            if(t>3*p-3){
                ++count;
            }else if(t>3*p-5 && S>0){
                ++count;
                --S;
            }
        }
        output << count << endl;
        cout << count << endl;
    }
    input.close();
    output.close();
    
    return 0;
}

