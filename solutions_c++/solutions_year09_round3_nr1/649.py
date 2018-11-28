#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include   <iomanip>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;

    string inFileName,outFileName;
    cout<<"Please input the input file's location:"<<endl;
    cin>>inFileName;
    cout<<"Please input the output file's location:"<<endl;
    cin>>outFileName;
    input.open(inFileName.data());
    output.open(outFileName.data());

    int T;
    input>>T;
    double seconds;
    string alienNum;
    string table;
    for (int i=0;i<T;i++){
        table.clear();
        seconds=0;
        input>>alienNum;
        //setTable
        int length=alienNum.length();
        for (int j=0;j<length;j++){
            if (table.find(alienNum[j])==string::npos){
                table+=alienNum[j];
            }
        }
        if (table.length()==1){
            table+='0';
        }
        char temp=table[0];
        table[0]=table[1];
        table[1]=temp;

        //Translate
        double base=1;
        for (int j=0;j<length;j++){
            seconds+=base*(int)table.find(alienNum[length-j-1]);
            base*=table.length();
        }
        output.precision(18);
        output<<"Case #"<<(i+1)<<": "<<seconds<<endl;
        cout.precision(18);
        cout<<seconds<<endl;

    }

    input.close();
    output.close();
    cout<<"result has been saved!"<<endl;
    return 0;
}

