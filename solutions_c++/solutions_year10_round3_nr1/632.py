#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <string>
#include <vector>

using namespace std;
class aaa{
public:
    unsigned int x;
    unsigned int y;
};

aaa input[1001];

int is_inter(int a, int b) {
    if( (input[a].x > input[b].x) &&
        (input[a].y < input[b].y) )
        return 1;
    if( (input[a].x < input[b].x) &&
        (input[a].y > input[b].y) )
        return 1;
    return 0;
}

int main()
{
    int T;
    
    cin >> T;

    for(int i=1; i<=T; i++) {
        int N;
        cin >> N;
        for(int j=0; j<N; j++) {
            cin >> input[j].x >> input[j].y;
        }
        unsigned long long sum = 0;
        for(int j=0; j<N; j++) for(int k=j+1; k<N; k++) {
            if( is_inter(j, k) )
                sum++;
        }
        cout << "Case #" << i << ": " << sum << endl;
    }
    
//    cin >> T;
    return 0;
}
