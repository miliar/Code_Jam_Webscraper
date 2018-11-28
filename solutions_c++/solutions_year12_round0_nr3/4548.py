//18min 49seg
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

string convertInt(int number){
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
    }

int main(void){
    int t,a,b,d,c;
    map<int,int> m;
    string cad;
    cin >> t;
    for (int i=1;i<=t;i++){
        c=0;
        cin >> a >> b;        
        for (int j=a;j<=b;j++){
            cad=convertInt(j);
            m.clear();
            for (int z=1;z<cad.size();z++){
                rotate(cad.begin(),cad.begin()+1,cad.end());
                istringstream (cad) >> d;
                if (m.find(d)==m.end()){
                   if (d>j&&d<=b){
                      c++;
                      m[d]=1;        
                      }
                   }
                //cout << z << ")" << cad << "," << d << endl;
                }

            }
        cout << "Case #" << i << ": " << c << endl;
        }
    return 0;
    }
