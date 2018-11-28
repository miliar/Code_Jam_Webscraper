
#include <iostream>
#include <vector>



using namespace std;

int miMax(int a, int b)
{
    if(a>b)
    {    
        return a;
    }
    else
    {
        return b;
    }
}

int miAbs(int a)
{
    if(a>0) return a;
    else return -a;
}
int main() 
{
    
    vector<int> o,b;
    vector<bool> seq;
    int n, t;
    cin >> t;
    for(int i=0 ; i <t ; ++i) 
    {
        cin >>n;
        int tiempo = 0;
        int tiempo_libre = 0;
        int anterior = 1;
        int anterior_otra = 1;
        char temp_char;
        char ant_char;
        int temp;
        cin >> temp_char;
        cin >> temp;
        tiempo += temp - anterior + 1;
        tiempo_libre = tiempo;
        ant_char = temp_char;
        anterior = temp;
        for(int j=1; j < n; ++j)
        {
            cin >> temp_char;
            cin >> temp; 
            if(temp_char == ant_char)
            {
                tiempo += miAbs(temp - anterior) + 1;
                tiempo_libre += miAbs(temp - anterior) + 1;
            }
            else
            {
                
                tiempo += miMax(1,miAbs(temp-anterior_otra)+1-tiempo_libre);
                tiempo_libre = miMax(1,miAbs(temp-anterior_otra)+1-tiempo_libre);
                anterior_otra = anterior;
            }
            ant_char = temp_char;
            anterior = temp;
            
        }
        cout << "Case #"<<i+1 << ": " << tiempo << endl;
        
    }
    
    
    return 0;
    
}
