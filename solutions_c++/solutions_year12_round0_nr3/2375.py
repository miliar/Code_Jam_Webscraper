/* 
 * File:   Recycled.cpp
 * Author: asaroha
 *
 * Created on April 14, 2012, 6:24 PM
 */

#include <cstdlib>
#include <math.h>
#include <map>
#include <fstream>
#include<iostream>

using namespace std;
class Recycled {
 public:
    Recycled();
    void parseFile();
    void cyclicPerms(int);
    int power(int);
private:
    int m_a, m_b;
    int p_count, length, examined;
    int * checked;
};

Recycled::Recycled() {
}
void Recycled::parseFile(){
    ifstream file;
    file.open("C-large.in",ios::in);
    ofstream o_file;
    o_file.open("output.txt",ios::out);
    int t, count = 0,i,c_n;
    
    file>>t;
    cout<<"num cases"<<t<<"\n";
    while(count <t) {
        file>>m_a;
        file>>m_b;

        p_count = 0;
        length = 0;

        c_n = m_a;
        while (c_n != 0) {
                length++; // 12 1 0
                c_n /= 10;
        }
        cout<<"Number "<<m_a<<"\n";
        cout<<"Number "<<m_b<<"\n";
        for (i = m_a; i <= m_b; i++) {        
                cyclicPerms(i);
        }

        o_file<<"Case #"<<count+1<<": "<<p_count;
        o_file<<"\n";
        count ++;
    }
}

void Recycled::cyclicPerms(int n ){
    //cout<<"Number "<<n<<"\n";
    int trailing;
    int c_n = n;
    
    int exp = 1;
    int div = 1;
    
    int i, j;
    map<int,int> c_perms;

    exp = power(length - 1);
        for (int i = 0; i < length - 1; i++) { // 0 1 2
            div *= 10;  //10  100
            trailing = n%div; //  1 11
            while(trailing < div/10) { // 1 < 1  11 < 10
                div *= 10;  //
                exp /= 10;
                i++; // 2
                trailing = n%div;
            }
            
            if(i == length -1)  //  0 == 2 1 == 2
                    break;
            c_n = n/div; // 11 1
            
            c_n = c_n + trailing * exp; // 1* 100 + 11  11 *10  + 1
            if(c_n <=m_b && c_n >=m_a)
            if (c_n <= m_b && c_n >= m_a && c_n > n && c_perms.find(c_n) == c_perms.end()) {//make sure the gen number is not counted twice(1212 => 2 121 212 1)
                c_perms.insert(pair<int,int>(c_n,1));
                p_count++;
            }
            exp /= 10; // 10
        }
}

int Recycled::power(int n) {
    int i=1,j;
    for(j=0;j<n;j++) {
        i *= 10;
    }
    return i;
}

//int Recycled::digitSort(int n) {
//    
//}

int main(int argc, char** argv) {
    Recycled instance;
    instance.parseFile();
    return 0;
}

