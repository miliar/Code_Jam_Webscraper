#include <iostream>
#include <fstream> 
#include <iomanip>
#include <string>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>


using namespace std;

void StringExplode(string str, string separator, vector<string>* results){
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

}

void reversealg(string str) {

    int len= str.length();
    char temp[255];
    char buffer[255];
    int A,B,n,alen,p,q,r,s=0;
    char a[20],b[20];
    vector<string> C;
    StringExplode(str, " ", &C);
    strcpy(temp, C[0].c_str());
    A = atoi(temp);
    strcpy(temp, C[1].c_str());
    B = atoi(temp);
    int counter=A;
    
    while(counter<=B){
        n=sprintf(a, "%d",counter);
        int alen=strlen(a);
        q=0;
        while(q<(alen-1)){
          if(q!=0){
            r=0;
            while(r<alen){
            a[r]=b[r];
            r++; 
            }
            }
        p=0;
        while(p<alen){
            if(p+1<alen){b[p]=a[p+1];}else{b[p]=a[-(alen-p-1)];}
            p++;
        }
        b[p]=0;
        if(counter==atoi(b)){break;}
        if(atoi(b)>=A&atoi(b)<=B&atoi(b)!=counter){s++;}
        
        q++;
    }

        counter++;
    }
      cout << s/2;
//    cout << "\n" << A << " "<< B;


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
            reversealg(temp);
            cout << "\n";
        }
        i++;
        }
     text_file.push_back( temp );
    
  
}