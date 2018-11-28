#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



int main(int argc, char *argv[])
{
    int left[1000];
int right[1000];
    ifstream is("in");
    ofstream os("out");
    int ncase;
    is>>ncase;
    for (int c=0;c<ncase;c++) {
        int n;
        is>>n;
        for (int i=0;i<n;i++) {
            is>>left[i]>>right[i];
        }
        int count = 0;
        for (int i=0;i<n;i++) {
            for (int j=0;j<i;j++) {
                if (left[i]>left[j] && right[i]<right[j]) count++;
                else if (left[i]<left[j] && right[i]>right[j]) count++;
            }
        }
        os<<"Case #"<<c+1<<": "<<count<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
