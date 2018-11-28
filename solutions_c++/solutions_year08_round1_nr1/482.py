#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("Input.txt");
    fout.open("Output1.txt");
    int kases;
    fin>>kases;
    for(int i=0;i<kases;i++)
    {
        int N,num;
        fin>>N;
        vector<int> A,B;
        for(int j=0;j<N;j++)
        {
                fin>>num;
                A.push_back(num);
            
        }
        for(int j=0;j<N;j++)
        {
                fin>>num;
                B.push_back(num);
        }
        sort(A.begin(),A.end());
        sort(B.begin(),B.end());
        int Sum=0;
        for(int j=0;j<N;j++)
        {
                Sum+=(A[j]*B[N-j-1]);
        }
        fout<<"Case #"<<i+1<<": "<<Sum<<"\n";
    }
    fin.close();
    fout.close();
    system("Pause");
    return 0;
}
    
