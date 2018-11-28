#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

const int MAXN = 501;

int N, slen;
int a[MAXN];
string s;

void solving(char bf, char ch)
{  
    for (int i = 0; i < slen; i++)
    {        
        if (s[i] == ch)
        {                 
           int tmp = 0;      
           for (int j = 0; j < i; j++)
               if (s[j] == bf)
                   tmp = (tmp + a[j]) % 10000;
           a[i] = tmp;
        }
    } 
}

int main(int argc, char *argv[])
{
    ifstream cin("c-large.in");
    ofstream cout("c-large.out");
    
    cin >> N;
    getline(cin, s);
    
    for (int k = 0; k < N; k++)
    {
        getline(cin, s);
        
        slen = s.length();
        for (int i = 0; i < slen; i++)
            if (s[i] == 'w') a[i] = 1;
        
        solving('w','e');
        solving('e','l');
        solving('l','c');
        solving('c','o');
        solving('o','m');
        solving('m','e');
        solving('e',' ');
        solving(' ','t');
        solving('t','o');
        solving('o',' ');
        solving(' ','c');
        solving('c','o');
        solving('o','d');
        solving('d','e');
        solving('e',' ');
        solving(' ','j');
        solving('j','a');
        solving('a','m');  

        /*for (int i = 0; i < slen; i++)
            cout << a[i] << " ";
        cout << endl;*/
        
        int kq = 0;
        for (int i = 0; i < slen; i++)
            if (s[i] == 'm') kq = (kq + a[i]) % 10000;
            
        cout << "Case #" << k+1 << ": ";           
        if (kq < 1000) cout << 0;      
        if (kq < 100) cout << 0;
        if (kq < 10) cout << 0;
        cout << kq << endl;
    }    
    
    cout.close();
    cin.close();    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
