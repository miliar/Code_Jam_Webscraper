#include<iostream>
#include<fstream>
using namespace::std;

int main()
{
    int X[2000];
    bool Y[2000];
    ifstream ifs ("D-large.in", ifstream::in);
    ofstream ofs ("out.txt", ofstream::out);
    int N;
    ifs >> N;
    for (int i=0;i<N;i++)
    {
        int M;
        double total = 0;
        memset(Y,false, sizeof(bool)*2000);
        ifs >> M;
        for (int j=1;j<=M;j++)
            ifs >> X[j];
        for (int j=1;j<=M;j++)
        {
            if(Y[j]==true||X[j]==j)continue;
            int count = 0;
            int ind = j;
            while(1)
            {
                Y[ind] = true;
                count++;
                ind = X[ind];
                if(ind==j)break;
            }
            total += count;
        }
        ofs << "Case #" << i+1 << ": " << total << endl;
    }
}
