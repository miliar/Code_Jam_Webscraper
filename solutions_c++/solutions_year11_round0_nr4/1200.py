#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

int  main(){
     int T,N,tmp,wrong;
     
     ifstream in("1.in");
     ofstream out("1.out");
     
     in >> T;
     
     for (int i = 0;i<T;i++){
         wrong = 0;
         in >> N;
         for(int j = 0;j<N;j++){
           in >> tmp;
           if (tmp != j+1)
              wrong++;
         }
         out << "Case #" << i+1 << ": " << wrong << ".000000" <<endl;
     }
}
