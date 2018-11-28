#include <iostream>
#include <algorithm>
#include <cstring>
#include <sstream>

using namespace std;

typedef long long ll;

string count(string N){
    //cout << "num:" << N << endl;
    int *array = new int[10];
    for(int i=0;i<10;i++)array[i] = 0;
    for(int i=0;i<N.length();i++){
        //cout << (int)(N.at(i)-49) << endl;
        array[N.at(i)-48]++;
    }    
    stringstream ret;
    for(int i=1;i<10;i++)ret << array[i] << " ";
    //cout << ret.str() << endl;
    return ret.str();
}

int main()
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++){
        ll N;
        cin >> N;
        stringstream blah;
        blah << N;
        string ref = count(blah.str());
        bool found = false;
        while(!found && N<=10000000){
            N++;
            stringstream foo;
            foo << N;
            string tmp = count(foo.str());
            if(ref==tmp)found=true;
	    //else cout << ref << "!=" << tmp << endl;
        }
        cout << "Case #" << i+1 << ": " << N << endl;
    }
    return 0;
}
