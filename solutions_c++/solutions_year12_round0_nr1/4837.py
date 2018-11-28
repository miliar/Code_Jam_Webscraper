#include <iostream>
#include <string>
#include <vector>
using namespace std;
string poisk(string s){
        string g = s;
        int t = s.length();
        for (int i = 0; i < t; i++){
                switch (s[i]){
                        case 'a':  g[i] = 'y';   break;
                        case 'b':  g[i] = 'h';    break;
                        case 'c':  g[i] = 'e';    break;
                        case 'd':  g[i] = 's';    break;
                        case 'e':  g[i] = 'o';    break;
                        case 'f':  g[i] = 'c';    break;
                        case 'g':  g[i] = 'v';    break;
                        case 'h':  g[i] = 'x';    break;
                        case 'i':  g[i] = 'd';    break;
                        case 'j':  g[i] = 'u';    break;
                        case 'k':  g[i] = 'i';    break;
                        case 'l':  g[i] = 'g';    break;
                        case 'm':  g[i] = 'l';    break;
                        case 'n':  g[i] = 'b';    break;
                        case 'o':  g[i] = 'k';    break;
                        case 'p':  g[i] = 'r';    break;
                        case 'q':  g[i] = 'z';    break;
                        case 'r':  g[i] = 't';    break;
                        case 's':  g[i] = 'n';    break;
                        case 't':  g[i] = 'w';    break;
                        case 'u':  g[i] = 'j';    break;
                        case 'v':  g[i] = 'p';    break;
                        case 'w':  g[i] = 'f';    break;
                        case 'x':  g[i] = 'm';    break;
                        case 'y':  g[i] = 'a';    break;
                        case 'z':  g[i] = 'q';    break;
                        case ' ':  g[i] = ' ';    break;

                }
        }
        return g;

}
int main(void){
        int n;
        freopen("input.in","r", stdin);
        freopen("output.out","w", stdout);
        cin >> n;
        string str = "";
        getline(cin, str);
        for (int i = 0; i < n; i++){
                getline(cin, str);
                string s = poisk(str);
                cout <<"Case #" << i+1<<": " << s << endl;
        }
        

        fclose(stdin);
        fclose(stdout);

return 0;
}

