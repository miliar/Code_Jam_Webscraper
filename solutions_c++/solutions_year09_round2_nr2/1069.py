#include <iostream>
#include <fstream>
#include <vector>
#include <string>
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
    string N;
    input>>T;
    for (int i=0;i<T;i++){
        input>>N;

        char max='0',min=(char)('9'+1),tempN='0';
        int tempk=0;
        int j=0;

        for (j=N.length()-1;j>=0;j--){
            if (N[j]>max) max=N[j];
            else if (N[j]<max){
                min=(char)('9'+1);
                for (int k=j;k<N.length();k++){
                    if (N[k]>N[j]){
                        if (N[k]<min){
                            min=N[k];
                            tempk=k;
                        }
                    }
                }
                tempN=N[j];
                N[j]=min;
                N[tempk]=tempN;

                string sub1=N.substr(0,j+1);
                string sub2=N.substr(j+1);
                string sub2Sorted="";

                for (int k=0;k<sub2.length();k++){
                    char min='9'+1;
                    int templ=0;
                    for (int l=0;l<sub2.length();l++){
                         if(sub2[l]<min) {
                             min=sub2[l];
                             templ=l;
                         }
                    }
                    sub2[templ]='9'+1;
                    sub2Sorted+=min;
                }
                N=sub1+sub2Sorted;
                break;
            }
            if (j==0){
              N="0"+N;
              j++;
            }
        }


        output<<"Case #"<<(i+1)<<": "<<N<<endl;
    }

    input.close();
    output.close();
    cout<<"result has been saved!"<<endl;
    return 0;
}

