#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
namespace
{
    enum{
        MAX_C=1000000
    };
}

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        int sum=0, exor=0, minimum=MAX_C;
        for(int j=0; j<N; j++){
            int tmp;
            cin >> tmp;
            sum+=tmp;
            exor^=tmp;
            minimum=min<int>(minimum, tmp);
        }
        if(exor==0){
            cout << "Case #" << (i+1) << ": " << (sum-minimum) << endl;
        }else{
            cout << "Case #" << (i+1) << ": NO" << endl;
        }
    }
    return 0;
}
