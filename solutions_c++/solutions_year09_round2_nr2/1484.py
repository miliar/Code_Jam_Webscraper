#include<algorithm>
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<cstdlib>
#include<iostream>
#include<string>
#include <vector>

using namespace std;

void CopyString(char *dest, char *src)
{
    while(*dest++ = *src++);
}



int main(){
    int caso = 0;
    freopen("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
    string buffer;
    getline(cin,buffer,'\n');
    while(getline(cin,buffer,'\n')){
     string original;
     original = buffer;
     //CopyString(&original,&buffer);
     sort(buffer.begin(),buffer.end());
     int i = 0;
     //cout << "Case #" << ++caso << ": " << buffer << endl;
     while(i==0){
         do{
            //cout << buffer << endl; 
            if(buffer > original){
               caso++;
               cout << "Case #" << caso << ": " << buffer<<endl;
               i=1;
               break;
            }
            //cout << i++ << endl;
         }while(next_permutation(buffer.begin(),buffer.end()));
         if(i==0) {
                  prev_permutation(buffer.begin(),buffer.end());
                  //cout << "Original " <<  buffer << endl; 
                  buffer ="0" + buffer;
                  original = buffer;
                  //cout << "Original " <<  buffer << endl; 
                  sort(buffer.begin(),buffer.end());

                  }
     }
     
    }
    
    fclose(stdin);
    return 0;
}
