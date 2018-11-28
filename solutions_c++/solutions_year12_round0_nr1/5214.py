#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
using namespace std;
//#define DEBUGMODE

void Eng2Googlerese(char *vet, char *o) {
    int i=0, j=0;
#ifdef DEBUGMODE
cout<<"Entrou no Eng2Googlerese\n";
#endif
    while(vet[i]==' ') i++; //remove espaços
    while(vet[i]!='\0') {
        switch(vet[i]) {
            case 'a':
                o[j]='y';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'b':
                o[j]='h';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'c':
                o[j]='e';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'd':
                o[j]='s';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'e':
                o[j]='o';//e->o
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'f':
                o[j]='c';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'g':
                o[j]='v';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'h':
                o[j]='x';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
                break;
            case 'i':
                o[j]='d';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'j':
                o[j]='u';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'k':
                o[j]='i';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'l':
                o[j]='g';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'm':
                o[j]='l';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'n':
                o[j]='b';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'o':
                o[j]='k';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'p':
                o[j]='r'; //p->r
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'q':
                o[j]='z';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'r':
                o[j]='t';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 's':
                o[j]='n';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 't':
                o[j]='w';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'u':
                o[j]='j';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'v':
                o[j]='p';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'w':
                o[j]='f';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'x':
                o[j]='m';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'y':
                o[j]='a';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case 'z':
                o[j]='q';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                i++;
                j++;
            break;
            case ' ':
                o[j]=' ';
#ifdef DEBUGMODE
cout<< o[j];
#endif
                while(vet[++i]==' '); //remove espaços
                j++;
            break;
            default:
                cout<<"\nErro encontrado, letra: "<<vet[i];
                return;
        }
    }
    if(o[j-1]==' ')
        o[j-1]='\0';
    else
        o[j]='\0';

}

int main()
{
    char w[101], res[101];
    char tam[101];
    int i,j, quant;
    char nomearq[100];
    gets(nomearq);
    ifstream entrada(nomearq);
    ofstream saida("saida.out",ios::trunc);
    entrada.getline(tam,100);
    quant = atoi(tam);
    cout << quant << endl;
    for(i=0;i<quant;i++) {
        entrada.getline(w,101);
        Eng2Googlerese(w,res);
        cout << "\nEntrada 1: ";
        puts(w);
        cout << "Case #"<<i+1<<": ";
        saida << "Case #"<<i+1<<": ";
        cout << res << endl;
        saida << res << endl;
        puts(res);

    }

    saida.close();
    entrada.close();
    return 0;
}
