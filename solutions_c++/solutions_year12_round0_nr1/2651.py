#include <iostream>
#include <fstream>

using namespace std;

char dic[]="yhesocvxduiglbkrztnwjpfmaq";

inline char replace(char& a){
    return dic[a-'a'];
}

int main(){
    ifstream input("input.txt");
    ofstream output("output.txt");

    int N = 0;
    input >> N;
    char temp[128]={0};
    input.getline(temp,128);
    for(int i=0; i<N; i++){
        char message[128]={0};
        input.getline(message,128);
        for(int k=0; k<128; k++){
            if(message[k]>='a' && message[k]<='z'){
                message[k] = replace(message[k]);
            }
        }
        output << "Case #" << i+1 << ": " << message << endl;
    }

    input.close();
    output.close();
    return 0;
}
