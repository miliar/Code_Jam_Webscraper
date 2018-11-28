#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("Input.txt");
    fout.open("Output2.txt");
    char arr[29][4]={"027","143","751","935","607","903","991","335","047","943","471","055","447","463","991","095","607","263","151","855","527","743","351","135","407","903","791","135","647"};
    int kases;
    fin>>kases;
    for(int i=0;i<kases;i++)
    {
        int N;
        fin>>N;
        fout<<"Case #"<<i+1<<": "<<arr[N-2]<<"\n";
    }
    fin.close();
    fout.close();
    system("Pause");
    return 0;
}
    
