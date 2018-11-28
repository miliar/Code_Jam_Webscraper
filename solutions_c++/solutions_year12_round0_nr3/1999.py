#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
using namespace std;

multimap<int, int>lst;

int totalDigit(int n) {
    int t =10;
    int d =0;
    while(n>0) {
        d++;
        n=n/10;
    }

    return d;
}

int getAfter(int n, int th) {

    int k = totalDigit(n)-th+1;
    int a =pow(10,k);

    int after = n%a * pow(10,th-1);

    int before = n/a;

    return after + before;
}

bool checkist(int key, int value) {

    multimap<int, int>::iterator it;
    for (it =  lst.equal_range(key).first; it !=lst.equal_range(key).second; ++it) {
        if ((*it).second == value)
            return true;
        //cout << (*it).second << endl;
    }

    lst.insert(pair<int,int> (key,value));
    return false;

}


int get(int a, int b) {


    if (a <=10 && b<=10) return 0;

    int sum = 0;
    int changeN;
    // assume all double digit or above
    for (int cont = max(11, a); cont <= b; cont++) {
        for (int i =2; i<=totalDigit(cont); i++) {
            changeN = getAfter(cont, i);

            if (changeN <= b && changeN > cont && !checkist(cont,changeN)) {
                sum  = sum+1;
            }
            // one to many here problem here

        }

    }

    lst.clear();
    return sum;
}


int main() {

    int cases;
    int a;
    int b;
    cin >> cases;
    for (int j = 1; j<=cases;j++){

        cin >> a;
        cin >> b;


        cout << "Case #" << j <<": " << get(a,b)<<endl;
    }


    return 0;
}
