#include<iostream>
#include<fstream>
using namespace std;

const int mul10[7] = {10,100,1000,10000,100000,1000000,10000000};

int marked[2000100];
int A, B;
int total;
ifstream fin("C-large.in");
ofstream fout("recycled.out");
int countRecycles(int S, int B) {
    int numDigit;
    for (int m = 0; m < 7; m++) {
        if (mul10[m] > S) {
            numDigit = m + 1;
            break;
        }
    }
    int result = 0;
    for (int m = 0; m < numDigit - 1; m++) {
        int end = S % mul10[m];
        int front = S / mul10[m];
        int recycle = end * mul10[numDigit - m - 2] + front;
        if (recycle > S && recycle <= B && marked[recycle] != S) {
            result++;
            marked[recycle] = S;            
        }
    }
    return result;
}

int main() {
    int ntests;
    fin >> ntests;
    for (int t = 1; t<=ntests; t++) {
        fin >> A >> B;
        total = 0;
        for (int i = A; i <= B; i++)
            marked[i] = 0;
        for (int i = A; i <= B; i++) {
            total += countRecycles(i,B);
        }
        fout << "Case #" << t << ": " << total << endl;
    }
}