#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool is_pure(int n, int* order, int* array) {
    int number = n;
    int index;
    do {
        //while (n > 1) {
        index = order[number];
        int n = array[index];
        //cout << number << " is at " << index << ", next value is " << order[index] << endl;
        //cout << "INDEX OF " << index << " is " << number << endl;
        if (number != n) {
            //cout << "exit\n";
            return false;
        }
        if (index == 1) return true;
        number = order[index];
        //n = number;
    } while (number > 1);
    return (number == 1);//true;
    //int index = order[n];
    //if (array[index]
}

int count_pure(int n, int index, int current, int* order, int* array ){
    int var = 0;
//    cout << "INDEX " << index << " / CURRENT " << current << endl;
//    if (index > 1) {//if (current > n) {
        //return 0;
//    }
    array[index] = current;
    order[current] = index;
    if (current == n) {//index > 1) {
        if (index == 1 && current == n) {
            var ++;
        } else if (is_pure(index, order, array)) {
            // cout << "PURE" << endl;
            // cout << "N : ";
            // for (int i = 1; i <= index; i++) {
            //     cout << array[i] << " ";
            // }
            // cout << "\nO : ";
            // for (int i = 1; i <= index; i++) {
            //     cout << order[array[i]] << " ";
            // }
            // cout << endl;
            var ++;//return 1;
        } else {
//            cout << "not pure" << endl;
        }
        //var ++;
    }
    for (int i = current + 1; i <= n; i++ ) {
        //if (array[order[i]] == i) {
        //cout << i << " " << order[i] << " // " << array[order[i]] << endl;
        var = (var + count_pure(n, index + 1, i, order, array) ) % 100003;
        //}
    }
    array[index] = -1;
    order[current] = -1;
    return var % 100003;
}

int main(int argc, char** argv) {
    int T;
    int n;
    cin >> T;
    for ( int c = 1; c <= T; c++ ) {
        cin >> n;
        int * array = new int[n + 1];
        int * order = new int[n + 1];
        for ( int i = 0; i <= n; i++ ) order[i] = -1;
        for ( int i = 0; i <= n; i++ ) array[i] = -1;
        //array[1] = 2;
        //order[2] = 1;
        int var = count_pure(n, 0, 1, order, array);
        cout << "Case #" << c << ": " << var << endl;
        delete[] array;
        delete[] order;
    }
    return 0;
}
