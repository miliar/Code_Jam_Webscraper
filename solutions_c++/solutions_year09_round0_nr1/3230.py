#include <cstdlib>
#include <iostream>
#include <fstream.h>
#include <string>

using namespace std;
char dic[2000][2000];
static int resultado;

int get_matches(char cadena[], char caso[], int largo, int cant_letras, int cant_palabras, int iterador);

int main(int argc, char *argv[])
{
    char str[2000];
    int results[25];
    
    fstream file_op("A-small-attempt1.in",ios::in);
    
    int cantidad_letras;
    int cantidad_palabras;
    int casos_testeo;

    file_op.getline(str,2000);
    cout <<str<< endl;
    char *pch;
    pch = strtok (str," ");
    cout << pch << endl;
    cantidad_letras = atoi(pch);
    pch = strtok (NULL," ");
    cout << pch<< endl;
    cantidad_palabras = atoi(pch);
    pch = strtok (NULL," "); 
    cout << pch<< endl;
    casos_testeo = atoi(pch); 

    int i;
    int j;

    for(i=0;i!=cantidad_palabras;i++)
    {
        file_op.getline(str,2000); 
        strcpy(dic[i],str);        

    }
    
    bool esmulti;
    esmulti=false;
    char caso[1000];
    int letra_actual;
    strcpy(caso,"");
    
    for(i=0;i!=casos_testeo;i++)
    {
        file_op.getline(str,2000); 
        
        letra_actual=0;
  //      while(letra_actual!=cantidad_letras)
    //    {
      //      if(str[j]=='(')
      //      {
        //        esmulti=true;
      //      }
       //     else
       //     {
      //          caso[letra_actual]=str[j]
       //     }
      //  }
      char cadena[200];
      cadena[0]='\0';
      resultado=0;
      cout<<str<<endl;
      get_matches(cadena,str,0,cantidad_letras,cantidad_palabras,0);
               
      cout<< endl<<endl<< dic[i] << endl << resultado << endl<<endl;
      results[i] = resultado;
    }    
    
    file_op.close();
    
   ofstream out("A-small.out");
    for(i=0;i!=casos_testeo;i++)
    {
        out<<"Case #"<<i+1<<": "<<results[i]<<endl;                            
    }
    out.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}

int get_matches(char cadena[20], char caso[200], int largo, int cant_letras, int cant_palabras, int iterador)
{

    int i,j;
    int letra_actual;
    int cont;
    bool seguir;

    letra_actual=0;
    iterador=0;
    if(largo!=cant_letras)
    {
        while(letra_actual!=largo)
        {
            if(caso[iterador]=='(')
            {
                while(caso[iterador]!=')')
                {
                    iterador++;
                }
                iterador++;
                letra_actual++;
           }
           else
           {
               iterador++;
               letra_actual++;
           }
       }

        if(caso[iterador]=='(')
        {
             iterador++;
             while(caso[iterador]!=')')
             {         
                 cadena[largo]=caso[iterador];
                 cadena[largo+1]='\0';
                
                 seguir=false;

                 for(i=0;i!=cant_palabras;i++)
                 {
                     cont =0;                         

                     for(j=0;j!=largo;j++)
                     {
                         if(dic[i][j]==cadena[j])
                         {
                             cont++;
                         }

                      }
                      if(cont==largo)
                      {
                          seguir=true;
                         break;
                      }
                  }
                  if(seguir==true)
                  {                  
                      get_matches(cadena, caso,largo+1,cant_letras, cant_palabras, iterador);
                  }
                  iterador++;
             }
        }
        else
        {
              cadena[largo]=caso[iterador];
              cadena[largo+1]='\0';
              
              seguir=false;
              cont =0;
              for(i=0;i!=cant_palabras;i++)
              {
                  cont =0;                   
                  for(j=0;j!=largo;j++)
                  {
                      if(dic[i][j]==cadena[j])
                      {
                          cont++;
                      }
 
                  }
                  if(cont==largo)
                  {
                      seguir=true;
                   break;
                  }
              }
              if(seguir==true)
              {
                  get_matches(cadena, caso,largo+1,cant_letras,cant_palabras, iterador);
              }
        }        
    }                          
    else
    {      
        for(i=0;i!=cant_palabras;i++)
        {
            if(strcmp(cadena,dic[i])==0)
            {

                resultado++;
            }                            
        }
    }


}


