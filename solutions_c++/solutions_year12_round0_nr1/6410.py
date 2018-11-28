#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
//  ifstream cin("A-small-attempt7.in");
 // ofstream cout("salida.out");

    char arr [30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
                      'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
                      
    char verdad [30] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    
    
    int c;
    string s;
    cin>>c;
    cin.ignore();
    for(int i =0;i<c;++i )//Casos de prueba
    {
        getline(cin,s);
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<s.size();++j)//Recorer el string
        {
            if(s[j] == ' ')
              cout<<' ';
            for(int k =0;k<30;++k)//Buscar la letra dentro del arreglo
            {
                if(verdad[k] == s[j])
                   cout<<arr[k];
            }
        }
        cout<<endl;
    }
 //  system("pause");
}
