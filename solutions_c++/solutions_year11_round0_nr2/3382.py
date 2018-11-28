#include<iostream>
#include <cstdlib>
using namespace std;
#include <fstream>


bool member(char c,char *list,int size)
{
    for (int i=0;i<size;i++)
        if(list[i]==c)
            return true;
    return false;
}

int inv(char c1, char c2, char **array, int n) {
    for (int i = 0; i < n; i++) {
        if ((array[0][i] == c1 && array[1][i] == c2) || (array[0][i] == c2 && array[1][i] == c1))
            return i;
    }
    return -1;
}

bool opp(char c, char **opposed,char *list, int n,int size) {
    for (int i = 0; i < n; i++)
    {
        if (opposed[0][i] == c && member(opposed[1][i],list,size))
            return true;
        if (opposed[1][i] == c && member(opposed[0][i],list,size))
            return true;
    }
    return false;
}



int main(int argc, char** argv) {

    char buffer[101];
    ifstream in;
    ofstream out;
    in.open("B-large.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    if (in && out) {
        int m;
        in >> buffer;
        m = atoi(buffer);
        for (int k = 0; k < m; k++) {

            char *invoke[3];
            char *opposed[2];

            in >> buffer;
            int c = atoi(buffer);
            if (c != 0) {
                for (int i = 0; i < 3; i++)
                    invoke[i] = new char[c];
                for (int i = 0; i < c; i++) {
                    in >> buffer;
                    invoke[0][i] = buffer[0];
                    invoke[1][i] = buffer[1];
                    invoke[2][i] = buffer[2];
                }
            }
            in >> buffer;
            int d = atoi(buffer);
            if (d != 0) {
                for (int i = 0; i < 2; i++)
                    opposed[i] = new char[d];
                for (int i = 0; i < d; i++) {
                    in >> buffer;
                    opposed[0][i] = buffer[0];
                    opposed[1][i] = buffer[1];
                }
            }
            in >> buffer;
            int n = atoi(buffer);
            in >> buffer;

            char *list;
            list = new char[n];
            int size = 0;
            //int next=0;

            for (int i = 0; i < n; i++) {
                if (size >= 1) {
                    int b = inv(buffer[i], list[size - 1], invoke, c);
                    if (b != -1) {
                        list[size - 1] = invoke[2][b];
                    } else {
                        bool op = opp(buffer[i], opposed,list, d,size);
                        if (op) {
                            size = 0;
                        } else {
                            list[size] = buffer[i];
                            size++;
                        }
                    }
                } else {
                    list[size] = buffer[i];
                    size++;
                }
            }

            out << "Case #" << k + 1 << ": [";
            if (size >= 1) {
                for (int i = 0; i < size - 1; i++)
                    out << list[i] << ", ";
                out << list[size - 1] << "]"<<endl;
            }
            else
            {
                for (int i = 0; i < size; i++)
                    out<<list[i];
                out<<"]"<<endl;
            }
        }
    }
    in.close();
    out.close();
}


