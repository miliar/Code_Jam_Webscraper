#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

class snapper
{
public:
    snapper() { isOn = false; isPower = false; }
    ~snapper() 
    { 
        left = NULL; 
        right = NULL;
    }
    bool isOn;
    bool isPower;
    snapper* left;
    snapper* right;
    void clap()
    {
        if(isPower)
        {
            isOn = !isOn;
        }
    }
};

int main(int argc, char *argv[])
{
    int t;
    int n[20000],k[20000];
    int i,j,counter;
    snapper* power = new snapper;
    snapper* snappers[200];
    
    ifstream fin;
    ofstream fout;
    fout.open("output.txt",ios::out);
    fin.open("A-small-attempt1.in",ios::in);
    //fin.open("data.txt",ios::in);
    fin >> t;
    power->isOn = true;
    power->isPower = true;
    i = 0 ;
    
    while(!fin.eof())
    {
        fin >> n[i] >> k[i];
        i++;
    } 
    for(i = 0 ; i < t ; i++)
    {
        for(j = 0 ; j < n[i] ; j++)
        {
            snappers[j] = new snapper;
            if(j == 0)
            {
                snappers[j]->left = power;
                snappers[j]->isPower = true;
            }
            else
            {
                snappers[j]->left = snappers[j-1];
                snappers[j-1]->right = snappers[j];
            }
        }
        
        for(j = 0 ; j < k[i] ; j++)
        {
            for(counter = 0 ; counter < n[i] ; counter++)
            {
                snappers[counter]->clap();
                
            }
            for(counter = 1 ; counter < n[i] ; counter++)
            {
                snappers[counter]->isPower = true;
                if(!snappers[counter]->left->isOn)
                {
                    int c;
                    for(c = counter ; c < n[i] ; c++)
                    {
                        snappers[c]->isPower = false;
                    }
                    break;
                }
                
                
            }
        }
        
        fout << "Case #" << i+1 << ": ";
        bool light = true;
        for(j = 0 ; j < n[i] ; j++)
        {
            if(!snappers[j]->isOn)
            {
                light = false;
            }
        }
        if(light)
            fout << "ON" << endl;
        else
            fout << "OFF" << endl;
            
        for(j = 0 ; j < n[i] ; j++)
        {
            delete snappers[j];
        }
    }
    
    delete power;
    fin.close();
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
