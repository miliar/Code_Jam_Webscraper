#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n;
    string radka;
    string tr = "yhesocvxduiglbkrztnwjpfmaq";
    ifstream Vstup("input");
    Vstup >> n;
    int test=n;
    getline(Vstup,radka);
    ofstream Vystup("output");
    while(n--)
    {
        Vystup << "Case #" << test-n << ": ";
        getline(Vstup,radka);

        for(int i=0; i<radka.size(); i++)
        {
            if(radka[i]-' '==0) Vystup << " ";
            else Vystup << tr[radka[i]-'a'];
        }

        Vystup << endl;
    }
    Vystup.close();
    return 0;
}
