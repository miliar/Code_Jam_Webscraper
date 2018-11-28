#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    int T;
    fstream f, f1;
    f.open("A-small-attempt2.in",ios::in);
    f1.open("output",ios::out);
    char googlerese[26];
    string G, N;
    googlerese[0]='y';
    googlerese[1]='h';
    googlerese[2]='e';
    googlerese[3]='s';
    googlerese[4]='o';
    googlerese[5]='c';
    googlerese[6]='v';
    googlerese[7]='x';
    googlerese[8]='d';
    googlerese[9]='u';
    googlerese[10]='i';
    googlerese[11]='g';
    googlerese[12]='l';
    googlerese[13]='b';
    googlerese[14]='k';
    googlerese[15]='r';
    googlerese[16]='z';
    googlerese[17]='t';
    googlerese[18]='n';
    googlerese[19]='w';
    googlerese[20]='j';
    googlerese[21]='p';
    googlerese[22]='f';
    googlerese[23]='m';
    googlerese[24]='a';
    googlerese[25]='q';
    f >> T;
    f.get();
    for(int i=0; i<T; i++) {
            getline(f,G,'\n');
            f1 << "Case #" << i+1 << ": ";
            N = G;
            for(int j=0; G[j]; j++)
                    if(G[j]!=' ')
                               N[j] = googlerese[G[j]-'a'];
            f1 << N << endl;
    }
    return 0;
}
