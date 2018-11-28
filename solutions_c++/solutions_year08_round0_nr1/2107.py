#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main() {
   ifstream in("A-large.in");
   //ifstream in("a.in");
   ofstream cout("al.out");
   int n, s, q, i, j, k, c, sel, tmp;
   string lq, line;
   in >> n;
   in.ignore();
   for(i=1; i<=n; i++){
        in >> s;
        in.ignore();
        string ls[s];
        bool bs[s];
        for(j=0; j<s; j++){
            getline(in, line);
            ls[j] = line;
            bs[j] = 1;
        }
        
        sel = 0;
        c = 0;
        in >> q;
        in.ignore();
        for(j=0; j<q; j++){
            getline(in, line);
            lq = line;
            for(k=0; k<s; k++){
                if(ls[k].compare(lq) == 0){
                    if(bs[k]){
                        bs[k] = 0;
                        sel++;
                        tmp = k;
                    }
                    break;
                }
            }
            if(sel == s){
                sel = 1;
                c++;
                for(k=0; k<s; k++)
                    bs[k] = 1;
                bs[tmp] = 0;
            }
        }
        cout << "Case #" << i << ": " << c << endl;
   }   
   in.close();
   cout.close();
   //system("pause");
   return 0;
}
