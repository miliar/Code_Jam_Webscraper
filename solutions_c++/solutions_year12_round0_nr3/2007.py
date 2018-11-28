#include <cstdio>
#include <string>
#include <string.h>
#include <algorithm>
#include <set>

using namespace std;

inline string rotate (string s){

    return s[s.length() - 1] + s.substr(0, s.length() -1);

}

int main (){


    FILE *fin = fopen("C-large.in", "r");
    FILE *fout = fopen ("out.txt", "w");
    int T;
    fscanf (fin, "%d", &T);

    for (int test_case = 0; test_case < T; test_case++){

        int counter = 0;
        int a,b;
        fscanf (fin, "%d %d", &a, &b);


        for (int i = a; i <= b; i++){
            char numberz[50];
            string s = "";
            sprintf (numberz, "%d", i);
            set <int> visited;
            for (int k = 0; k < strlen(numberz); k++){
                s += numberz[k];
            }
            for (int k = 1; k < strlen(numberz); k++){
                s = rotate(s);
                if (s[0] == '0') continue;
                int temp;
                sscanf(s.c_str(), "%d", &temp);
                if (i < temp && temp <= b && visited.find(temp) == visited.end()){
                    visited.insert(temp);
                    counter++;
                    //if (i % 10000 == 1) printf ("%d %d\n", i, temp);

                }
            }

        }



        fprintf (fout, "Case #%d: %d\n", test_case+1, counter);
        printf ("Case #%d: %d\n", test_case+1, counter);
        //system("PAUSE");
    }

}
