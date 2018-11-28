#include <iostream>
#include <fstream> 
#include <iomanip>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int StringExplode(string str, string separator, vector<string>* results){
    int found;
    int count=0;
    found = str.find_first_of(separator);
    while(found != string::npos){
        if(found > 0){
            results->push_back(str.substr(0,found));
        }
        str = str.substr(found+1);
        count++;
        found = str.find_first_of(separator);
    }
    if(str.length() > 0){
        results->push_back(str);
    }
return count;
}

void dancealg(string str) {

    int len= str.length();
    char temp[255];
    char buffer[255];
    int maxscore,minscore;
    int buf;
    int b=3;
    int c=0;
    int d;
    int e=0;
    int f=0;
    int P;
    vector<string> A;
    P=StringExplode(str, " ", &A);
    strcpy(temp, A[2].c_str());
    minscore = atoi(temp)*3-4;
    strcpy(temp, A[1].c_str());
    d = atoi(temp);
    while(b<=P){
    if(A[b].length()>0){
    buf=atoi(strcpy(temp, A[b].c_str()));
    }
    if(buf>=minscore){
            if(buf!=0||minscore==-4){
        c++;
        if(buf==minscore){
                    d--;
                }else if(buf==minscore+1){
                            d--;
                }else{
                    if(buf!=29){
            e++;
        }
            }
        }                  
    }else{
        if(buf!=1&&buf!=0){
            e++;
        }
    }

    b++;
    }
    if(d<=0){
        c=c+d;
        d=0;
        }else
        
        {
            d=d-e;
            if(d<0){
                d=0;
            }
        }
cout << c-d;
//    cout << c-d << " " << d << " " << e ;
    



}

int main()
{
  vector<string> text_file;
  int i=0;
  ifstream ifs( "input.txt" );
  string temp;

  while( getline( ifs, temp ) ){
        if(i>0){
            cout << "Case #" << i <<": ";
            dancealg(temp);
            cout << "\n";
        }
        i++;
        }
     text_file.push_back( temp );
    
  
}