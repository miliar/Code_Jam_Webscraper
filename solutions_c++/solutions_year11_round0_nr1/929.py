#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){

    string line;
    getline(cin, line);
    istringstream iss(line);
    int n;
    iss>>n;
for(int i=0;i<n;i++){
    int place[2];
    place[0]=1;
    place[1]=1;
    string line;
    getline(cin, line);
    istringstream iss(line);
    int num;
    iss>>num;
    if(num==0){
        cout<<"Case #"<<i+1<<": "<<0<<endl;
        continue;
    }
    int steps=0;
    char c1;
    int b1;
    int d1;
    char c2;
    int d2;
    int b2;
    iss>>c1;
    if(c1=='O') b1=0; else b1=1;
    iss>>d1;
    int cur=0;
            while(iss>>c2){

                    if(c2=='O') b2=0; else b2=1;
                    iss>>d2;
                    int temp = abs(place[b1]-d1)+1;
                    if(c1==c2)
                    {
                           steps += temp;
                           cur += temp;
                           place[b1] = d1;
                    }
                    else
                    {
                           steps += temp;
                           cur += temp;
                           place[b1]=d1;
                           if( cur >= abs(place[b2]-d2))
                           {
                                 place[b2]=d2;
                           }
                           else
                           {
                                 if(place[b2] > d2)
                                 {
                                      place[b2] -= cur;
                                 }
                                 else 
                                 {
                                      place[b2] += cur;
                                 }
                           }
                           cur = 0;
                           c1=c2; b1=b2;
                    }
            d1=d2;
            }
     steps += abs(place[b1]-d1)+1;
     cout<<"Case #"<<i+1<<": "<<steps<<endl;
    }
return 0;
}
