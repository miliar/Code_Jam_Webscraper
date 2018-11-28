#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("happy.txt");
    ofstream outfile("sad.txt");
    long long cases;
    infile >> cases;
    for (long long i = 0; i < cases; i++)
    {
    
        vector<long long> vec1;
        vector<long long> vec2;
        long long size;
        infile >> size;
        
        for (long long j = 0; j < size; j++)
        {
            long long a;
            infile >> a;
            vec1.push_back(a);
        }
        for (long long j = 0; j < size; j++)
        {
            long long a;
            infile >> a;
            vec2.push_back(a);
        }
    
        long long sum = 0;
        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());
        
        for (long long j = 0; j < size; j++)
            sum += (vec1[j] * vec2[size-1-j]);
        outfile << "Case #" << (i+1) << ": " << sum << endl;
    }
    return 0;
    
}
