#include <iostream>
#include <string>
#include <string.h>

using namespace std;

char convert(char i){
    char list[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    if(i ==' ' || i == '\n')
        return i;
    else
        return list[i-'a'];
}

int main(){
    int num;
    char line[200];
    cin >> num;
    cin.getline(line,200);
    for(int i=0;i<num;i++){
        cin.getline(line,200);
        cout << "Case #" << i+1 << ": ";
        int len = strlen(line);
        for(int j=0; j<len;j++){
            cout << convert(line[j]);
        }
        cout << endl;
    }
}
        

