#include <iostream>
#include <cstdio>
#include <set>
#include <cstring>

using namespace std;

FILE *fin = fopen ("A-large.in","r");
FILE *fout = fopen ("A-large.out","w");

int main () {
    int T;
    fscanf (fin, "%d",&T);
    for (int run = 1;run <=T; ++run) {
        int N,M;
        set<string> dirset;
        dirset.clear ();
        fscanf (fin, "%d %d", &N, &M);
        //cout<<N<< " "<<M<<endl;
        for (int i = 0;i< N;++i) {
            char c[101];
            fscanf (fin, "%s", c);
            string str(c);
            cout<<str<<endl;
            for (int j = 0;j< str.length ();++j)
                if (str[j] == '/') {
                    int k;
                    for (k = j+1;k<str.length();++k) 
                        if (str[k] == '/') break;
                    string subdir = str.substr (0,k);
                    dirset.insert (subdir);
                }
        }
        //cout<<"here"<<endl;
        int res = 0;
        for (int i = 0;i< M;++i) {
            char c[101];
            fscanf (fin, "%s", c);
            string str (c);
            //cout<<str<<endl;
            if (dirset.count (str) > 0) {
                continue;
            }
            else {
                cout<<"here"<<endl;
                int lj = str.length();
                for (int j = str.length()-1;j>=0;--j) 
                    if (str[j] == '/') {
                        string dir = str.substr (0,lj);
                        cout<<"here"<<endl;
                        if (dirset.count(dir) == 0) {
                            res++;
                            dirset.insert (dir);
                            lj = j;   
                        }
                        else break;
                    }
            }
        }
        fprintf (fout, "Case #%d: %d\n",run,res);
    }    
    cin>>T;
    return 0;
}
