#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

int main(){
        ifstream cin ("A-small-attempt0.in");
        ofstream cout ("output.txt");
        int t;
        cin >> t;
        for (int i = 0; i < t; i++){
                int n;
                cin >> n;
                int result = 0;
                if (n==1){
                        int a, b;
                        cin >> a >> b;
                        result = 0;
                }
                else {
                        int a, b;
                        int c, d;
                        cin >> a >> b;
                        cin >> c >> d;
                        if (a>c && d > b){
                                result = 1;
                        }
                        else if (c > a && b > d)
                                result = 1;
                }
                cout << "Case #" << i+1 << ": " << result << endl;
        }


        int wait;
        cin >> wait;
        return 0;
}
