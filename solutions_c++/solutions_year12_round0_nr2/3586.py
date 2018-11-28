#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

int main(int argc, char **argv) {

    // read input file
    ifstream ifile (argv[1]);
    ofstream ofile (argv[2]);

    if (!ifile || !ofile) { cout << "Error: files cant be opened"; exit (1); }

    int T, t = 1;
    int N, S, p;

    ifile >> T;

    while (t <= T) {
        ifile >> N >> S >> p;
        int x[N];
        int counter = 0;



        int max_num = 0, temp, remain, max=0, min=10, counter = 0;
        bool contains = false;
        int triplet[3];

        for (int i = 0; i < N; i++) {
            ifile >> x[i];
        }

        for (int i = 0; i < N; i++) {
            contains = false;
            if (x[i] == 0){
                if(p == 0){
                    counter++;
                }
            }
            else
            {
                temp = x[i] / 3;

                for (int j = 0; j < 3; j++) {
                    triplet[j] = temp;
                }

                remain = x[i] - (temp * 3);

                for (int k = 0; k < remain; k++) {
                    triplet[k] += 1;
                }

                for (int k = 0; k < 3; k++) {
                        if (triplet[k] >= p){
                            contains = true;
                        }
                    }

                if (S > 0 && !contains){
                    if (remain == 1) {
                        triplet[1] -= 1;
                        triplet[2] += 1;
                    } else {
                        triplet[0] -= 1;
                        triplet[1] += 1;
                    }
                }

                    max = 0; min = 10; contains = false;
                    for (int k = 0; k < 3; k++) {
                        if(triplet[k] > max)
                            max = triplet[k];
                        if(triplet[k] < min)
                            min = triplet[k];
                    }

                    for (int k = 0; k < 3; k++) {
                        if (triplet[k] >= p){
                            contains = true;
                        }
                    }
                    if ((max - min == 2) && contains){
                        S--;
                        counter++;
                    }
                    else if(contains){
                        counter++;
                    }

                }

        }

        ofile << "Case #" << t << ": " << counter << endl;
        t++;
    }
}

