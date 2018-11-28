#include <cstdlib>
#include <iostream>
#include <fstream.h>
#include <string>

using namespace std;
char dic[20];


static int resultado;

int get_matches(char cadena[20], char caso[500], int largo, int lastn);

int main(int argc, char *argv[])
{
    char str[2000];
    int results[100];
    
dic[0]='w';
dic[1]='e';
dic[2]='l';
dic[3]='c';
dic[4]='o';
dic[5]='m';
dic[6]='e';
dic[7]=' ';
dic[8]='t';
dic[9]='o';
dic[10]=' ';
dic[11]='c';
dic[12]='o';
dic[13]='d';
dic[14]='e';
dic[15]=' ';
dic[16]='j';
dic[17]='a';
dic[18]='m';
dic[19]='\0';

    fstream file_op("C-small-attempt0.in",ios::in);
    
    int cantidad_letras;
    int casos_testeo;

    file_op.getline(str,2000);
    cout <<str<< endl;
    casos_testeo = atoi(str); 

    int i;
    
    char caso[1000];
    strcpy(caso,"");

    cout<<dic[2]<<endl;
    for(i=0;i!=casos_testeo;i++)
    {
        file_op.getline(str,2000); 
        
        char cadena[20];
        cadena[0]='\0';
        resultado=0;
        cout<<str<<"-"<< strlen(str)<<endl;
        get_matches(cadena,str,0,0);
        cout<<resultado<<endl;
        results[i] = resultado;
    }    
    
    file_op.close();
    
   ofstream out("C-small.out");
    for(i=0;i!=casos_testeo;i++)
    {
        if((results[i])<10)
            out<<"Case #"<<i+1<<": 000"<<results[i]<<endl;                            
        else if (results[i]<100)
            out<<"Case #"<<i+1<<": 00"<<results[i]<<endl;                            
        else if (results[i]<1000)
            out<<"Case #"<<i+1<<": 0"<<results[i]<<endl;                            
        else if (results[i]<10000)
            out<<"Case #"<<i+1<<": "<<results[i]<<endl;    
        else                        
        {
            int aaa;
            aaa = results[i]/10000;
            aaa = aaa*10000;
            results[i] = results[i]-aaa;
            out<<"Case #"<<i<<": "<<results[i]<<endl;                
        }

    }
    out.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}

int get_matches(char cadena[20], char caso[500], int largo, int lastn)
{
    int i;

    if(largo!=19)
    {
        for(i=lastn;i!=strlen(caso);i++)
        {
            if(caso[i]==dic[largo])
            {
                cadena[largo]=caso[i];
                cadena[largo+1]='\0';                              

                get_matches(cadena, caso, largo+1, i);
            }
        }
    }                
    else
    {      
        resultado++;
    }
}


