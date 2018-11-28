#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

long fixmod(long x, int N) {
        x = x % N;
        if (x < 0) return x + N;
        return x;
}


int main() {
    ifstream inFile("C.in");
    ofstream outFile("results.txt");
    int T;
    inFile >> T;
    for (int s = 1; s <= T; s++) {
        long R,k,N;
        inFile >> R >> k >> N;
        long* numbers = new long[N];
        for (int i = 0; i < N; i++)
            inFile >> numbers[i];
        long** sum = new long*[N];
        for (int i = 0; i < N; i++) {
                sum[i] = new long[N];
                sum[i][i] = numbers[i];
                for (int j = i+1; j % N != i; j++) {
                    sum[i][j%N] = sum[i][(j-1)%N] + numbers[j%N];
                }
        }
        long euros = 0; // what we've earned
        long start = 0; // start of the queue
        while (R > 0) {
                long i = start;
                for (; sum[start][i%N] <= k && i != start + N; i++);
                if (i == start + N) { // Alle kommen rein
                    long pos = fixmod(start-1,N);
                    if (sum[start][pos] <= k) euros += sum[start][pos];
                    else {
                        euros += sum[start][fixmod(start-2,N)];
                        start = pos;
                    }
                }
                else { // Start bis Start + i - 1 kommen rein
                    euros += sum[start][fixmod(i-1,N)];
                    start = fixmod(i,N);
                }
                R--;
        }
        for (int i = 0; i < N; i++)
            delete [] sum[i];
        delete [] sum;
        delete [] numbers;
        outFile << "Case #" << s << ": " << euros << endl;
    }
    inFile.close();
    outFile.close();
}
