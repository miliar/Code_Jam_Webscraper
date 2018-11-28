#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
#include<time.h>
#include<sstream>
#include<vector>
#include<set>
using namespace std;

template<class T>
string toString(const T &t) {
       stringstream ss; ss << t;
       return ss.str();
}

string conv(int decimal, int base){
    if(decimal == 0) return "0";
    char NUMS[] = "0123456789ABCDEF"; 
    std::string result = ""; 
    do{
        result.push_back(NUMS[decimal%base]);
        decimal /= base;
    }while(decimal != 0);
    return std::string(result.rbegin(), result.rend());
}
vector<string> explode( const string &delimiter, const string &str)
{
    vector<string> arr;

    int strleng = str.length();
    int delleng = delimiter.length();
    if (delleng==0)
        return arr;

    int i=0;
    int k=0;
    while( i<strleng )
    {
        int j=0;
        while (i+j<strleng && j<delleng && str[i+j]==delimiter[j])
            j++;
        if (j==delleng)
        {
            arr.push_back(  str.substr(k, i-k) );
            i+=delleng;
            k=i;
        }
        else
        {
            i++;
        }
    }
    arr.push_back(  str.substr(k, i-k) );
    return arr;
}

int reclevel = 0;

bool checkHappy(string num, int base, vector<int> &rec) {
     if (num.length() == 1 && (((num[0]-48)*(num[0]-48)) == base)) {
        return true;
     } else if (atoi(num.c_str()) == 1) {
        return true; 
     } else {
       int res = 0;
       for (int i=0; i<num.length(); i++) {
           res += (num[i]-48)*(num[i]-48);
       }
        //  cout << "[r] " << res << " [cr] " << conv(res,base) << " [n] " << num << endl;
        //  getch();
       
       bool recur = false;
       for (int i=0; i<rec.size(); i++) {
           if (res == rec[i]) {
              recur = true;
              break;
           }
       }
       if (recur) {
          return false;
       } else {
          rec.push_back(res);
          return checkHappy(toString(conv(res,base)),base,rec);
       }
     }
}

int main() {
    
    
    ofstream out("p1.out");
    ifstream in("A-small-attempt2.in");
    int cases;
    int ct = 0;
    in >> cases;
    string t;
    getline(in, t);
    for (int i=0; i<cases; i++) {
        string t;
        getline(in, t);
        
        vector<int> bases;
        vector<string> x = explode(" ",t);
        for (int j=0; j<x.size(); j++) {
            int base = atoi(x[j].c_str());
            bases.push_back(base);
        }
        int happynum = 0;
        int j = 2;
        while (1) {
            int num = j;
            bool happy = true;
            for (int z=0; z<bases.size(); z++) {
                int base = bases[z];
                string numConv = conv(num,base);
                reclevel = 0;
                vector<int> rr; rr.push_back(atoi(numConv.c_str()));
                if (!checkHappy(numConv,base,rr))
                   happy = false;
            }
            if (happy) {
               out << "Case #" << ++ct << ": " << j << endl;
               break;
            }
            j++;
        }
        
    }
    return 0;   
}
