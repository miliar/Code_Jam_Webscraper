#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

  char tab[] = {'y', 'h', 'e', 's', 'o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p', 'f','m','a','q',};
//char tab[] = {'a', 'b', 'c', 'd', 'e','f','v','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z',};
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//there are twenty six factorial possibilities
int main(){
    int t;
    char line[200];
    cin >> t;
    cin.getline(line, 150);

    for(int j = 0; j < t; ++j){
        cin.getline(line, 150);
        cout << "Case #" << j+1 << ": ";
        for(int i = 0; i < strlen(line); ++i){
            if(line[i] >= 'a' && line[i] <= 'z')
                cout << tab[line[i] - 'a'];
            else if(line[i] >= 'A' && line[i] <= 'Z')
                cout << char(tab[line[i] - 'A'] - 'a'+'A');
            else cout << line[i];
        }
        if(j < (t-1))cout << "\n";

    }


    return 0;
}
