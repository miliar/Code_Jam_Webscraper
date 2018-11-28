#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <string.h>
#include <stdlib.h>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;


//ifstream fin("sample.txt");
//#define cin fin


void run(){
    int n, sur, ms;
    cin >> n >> sur >> ms;
    int ts;
    int os;
    int a = 0;
    for(int i = 0; i < n; i++){
        cin >> ts;
        if(ts == 0){
            if(ms == 0){
                a++;
            }
        } else if(ts%3 == 1){
            os = ts/3;
            if(os+1 >= ms){
                a++;
            }
        } else if (ts%3 == 2){
            os = ts/3;
            if(os+1 >= ms){
                a++;
            } else if(os+2 >= ms && sur > 0){
                a++;
                sur--;
            }
        } else if (ts%3 == 0){
            os = ts/3;
            if(os >= ms){
                a++;
            } else if(os+1 >= ms && sur > 0){
                a++;
                sur--;
            }
        }
    }
    cout << a;
}


int main(){
    int numCase;
    cin >> numCase;
    for(int i = 0; i < numCase; i++){
        cout << "Case #" << i+1 << ": ";
        run();
        cout << endl;
    }
    return 0;
}

