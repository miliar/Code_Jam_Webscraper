#include<iostream>
#include<string>
using namespace std;

long n,t;
string str;

char temp;

int main() {
    cin >> t;
    for (int i=0;i<t;i++) {
        cin >> str;
        bool flag=true;
        int min;
        for (int j=str.length()-2;j>=0;j--) {
            if (!flag) {continue;};
            temp='9';            
            for (int k=j+1;k<str.length();k++) {
                if (str[j]<str[k]) {
                   flag=false;
                   if (str[k]<=temp) {
                      temp=str[k];
                      min=k;
                   }
                }
            }
            if (!flag) {
               temp=str[min];
               str[min]=str[j];
               str[j]=temp;
               for (int ii=j+1;ii<str.length();ii++) {
                   for (int k=j+1;k<str.length()-ii+j;k++) {
                       if (str[k]>str[k+1]) {
                          temp=str[k];
                          str[k]=str[k+1];
                          str[k+1]=temp;                                        
                       }
                   }
               }                       
            }
        }
        if (!flag) {
           cout << "Case #" << i+1 << ": " << str << endl;
        }
        else {
             min=0;
             for (int ii=1;ii<str.length();ii++) {
                 if ((str[ii]<str[min]) && (str[ii]!='0')) {
                    min=ii;
                 }
             }
             char temp2;
             temp2=str[min];
             str[min]='0';    
             for (int ii=0;ii<str.length();ii++) {
                   for (int k=0;k<str.length()-1-ii;k++) {
                       if (str[k]>str[k+1]) {
                          temp=str[k];
                          str[k]=str[k+1];
                          str[k+1]=temp;                                        
                       }
                   }
             }  
             cout << "Case #" << i+1 << ": " << temp2 << str << endl;            
        }
    }
    return 0;
}
