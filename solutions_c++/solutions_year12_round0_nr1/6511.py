#include <iostream>
#include <fstream>

using namespace std;

int main()
{
        char str[200], ch;
        int n;
        ifstream obj("input.txt");
        obj >> n;
        obj.get(ch);
        char *a="yhesocvxduiglbkrztnwjpfmaq";
        for(int tc=1; tc<=n; tc++)
        {
                cout << "Case #" << tc << ": ";
                memset(str, 0, 200);
                obj.getline(str, 200);
                //cout << str;
                for(int i=0; i<strlen(str); i++)
                {
                        if(str[i] == ' ')
                        cout << str[i];
                        else
                        cout << a[str[i]-97];
                }
                //if(tc!=n)
                cout << endl;
        }
        return 0;
}
