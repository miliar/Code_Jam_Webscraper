#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime>
#include <climits>  
#include <fstream>  

using namespace std;

int main()
{
    ifstream in("entrada.txt", ios::in);
    ofstream out("salida.out", ios::out);
                 
    string fin = "yhesocvxduiglbkrztnwjpfmaq";
                 
    string cad;
    int cas=0;
    int num=0;
    in>>num;
    getline(in,cad);
    while(num--)
    {
        getline(in,cad);
        out<<"Case #"<<++cas<<": ";
        for(int i=0; i<cad.length(); i++)
           if(cad[i]!=' ')
              out<<fin[cad[i]-'a'];
           else
              out<<" ";
              
        out<<endl;      
    }
}





