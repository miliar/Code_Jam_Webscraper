#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int Tcases;
    string line;
    ifstream infile ("input.txt");
    ofstream outfile ("output.txt");

    getline (infile,line);
    Tcases = atoi(line.c_str());

    for(int i = 0; i<Tcases; i++)
    {
        int Rtimes, Ngroups, Kcapacity;
        string buf;

        getline (infile,line);
        stringstream ss (stringstream::in | stringstream::out);
        ss << line;
        int j = 0;
        while (ss >> buf){
            switch(j){
                case 0:
                    Rtimes = atoi(buf.c_str());
                    break;
                case 1:
                    Kcapacity = atoi(buf.c_str());
                    break;
                case 2:
                    Ngroups = atoi(buf.c_str());
                    break;
            }
            j++;
        }
        /*cout << Rtimes << " " << Kcapacity << " " << Ngroups << endl;
        system("pause");*/
        int groups[Ngroups];
        getline (infile,line);
        stringstream ss2 (stringstream::in | stringstream::out);
        ss2 << line;
        j = 0;
        while (ss2 >> buf){
            groups[j] = atoi(buf.c_str());
            j++;
        }
        //RECOGI DATOS

        int ganancia = 0;
        for(j=0; j<Rtimes; j++)
        {
            //for(int n=0; n<Ngroups;n++) cout << groups[n] << " "; cout << endl;


            int suma = 0;
            int index = 0;
            while(suma+groups[index] <= Kcapacity && index < Ngroups){
                suma += groups[index];
                index++;
            }
            //cout << index<< endl;
            //system("pause");

            ganancia += suma;
            int aux[Ngroups];
            for(int m = 0; m<Ngroups - index;m++)
            {
                aux[m] = groups[index + m];
            }
            for(int m = Ngroups-index; m<Ngroups;m++)
            {
                aux[m] = groups[m - (Ngroups-index)];
                //cout << aux[m]<<" *";system("pause");
            }


            for(int n=0; n<Ngroups;n++) groups[n] = aux[n];
        }

        outfile << "Case #" << i+1 << ": " << ganancia << endl;

    }
    return 0;
}
