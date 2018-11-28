#include<iostream>
#include<fstream>
#include<vector>
using namespace::std;
int main()
{
    ifstream ifs("C-large.in", ifstream::in);
    ofstream ofs("out.txt", ofstream::out);
    int N;
    ifs >> N;
    for(int i=0;i<N;i++)
    {
        int M,curr;
        ifs >> M;
        int total = 0;
        int total_b = 0;
        int _min = 1000001;
        for(int j=0;j<M;j++)
        {
            ifs >> curr;
            if (curr<_min)_min=curr;
            total_b = total_b ^ curr;
            total += curr;
        }
        ofs << "Case #" << i+1 << ": ";
        if(total_b == 0) ofs << total-_min<< endl;
        else ofs << "NO" << endl; 
    }
}
