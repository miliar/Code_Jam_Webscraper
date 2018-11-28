#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#define MAXSIZE 1000
using namespace std;


int main(int argc, char* argv[]){

    if (argc != 2){
        fprintf(stderr, "Usage: ./stadisitcs [Input File]");
        return 1;
    }

    ifstream in(argv[1], ifstream:: in);
    ofstream out("stadistics.out", ofstream:: out);
    char buff[MAXSIZE];

    in.getline(buff, MAXSIZE);
    int cases = atoi(buff);

    for (int i = 1; i <= cases; i++){
        in.getline(buff, MAXSIZE);

        int N = atoi(strtok(buff, " "));
        int Pd = atoi(strtok(NULL, " "));
        int Pg = atoi(strtok(NULL, " "));
        bool result = false;

        if (Pg == 100 && Pd != 100 || Pg == 0 && Pd > 0){
            result = false;
        }
        else{
            for (int j = 1; j <= N; j++){
            float fp = (j*Pd)/100.0;
            int  ip = (int)fp;
            float decimal = fp - ip;
            if (decimal == 0.0){
                 result =  true;
                 break;
            }
          }
        }


        if (result == true)
            out << "Case #"<< i <<": Possible\n";
        else
            out << "Case #"<< i <<": Broken\n";
    }
    return 0;
}
