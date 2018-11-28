#include <iostream>
#include <map>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
    if (argc < 2) { 
        cout << "Usage " << argv[0] << " <input file>" << endl;
        return 1;
    }
    int N, S, p, t;
    int cases;
    int answer;
    int surprises;
    ifstream in(argv[1]);
    in >> cases;
    for (int c=1; c<=cases; c++) { 
        cout << "Case #" << c << ": ";
        answer = 0;
        surprises = 0;
        in >> N;
        in >> S;
        in >> p;
        for (int i=0; i<N; i++) {  
            in >> t;
            if (t >= 3*p-2) answer++;
            else if ( p>=2 && t< 3*p-2 && t > 3*p-5) { 
                if (surprises < S and surprises <2) { 
                    surprises++;
                    answer++;
                }
            }
        }
        cout << answer << endl;
    }
    return 0;
}
