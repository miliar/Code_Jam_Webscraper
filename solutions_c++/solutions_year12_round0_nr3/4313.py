#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>

using namespace std;

int tam(int x) {
    int c=0;
    while(x>0) {
        c++;
        x/=10;
    }
    return c;
}
void Shift(int &x, int q) {
    for(int i=0;i<q;i++) {
        x*=10;
    }
}

void Cycle(int &x, int tamM) {
    int a;
    a= (x%10);
    Shift(a,tamM-1);
    //cout << "\ncycle1\na vale: " << a << " e x vale " << x;
    x =((x/10)+a);
    //cout << "\ncycle3: x termina com" << x << endl;
}
int isRecycled(int n, int m) {
    int tamM= tam(m);
//    cout << "tamM de " << m << "=="<<tamM<<endl;
    for(int i=0;i<tamM;i++) {
        if(n==m) {
            //cout << "testou n: " << n << " e m: " << m << endl;
            return 1;
        } else {
            //cout << "testou n: " << n << " e m: " << m << endl;
            Cycle(n,tamM);
        }
    }
    return 0;
}
int recycledBetween(int a, int b) {
    int m,n, cont=0;
    for(n=a;n<b;n++) {
        for(m=n+1;m<=b;m++) {
            cont+=isRecycled(n,m);
        }
    }
    return cont;
}
/*
int main(void) {
    cout<<recycledBetween(1111,2222);
    return 0;
}
*/

int main()
{
    int i,j, quant;
    int m, n;
    int pos;
    char nomearq[100];
    char input[200];
    string s;
    cout << "enter the filename: ";
    gets(nomearq);
    ifstream entrada(nomearq);
    ofstream saida("saida.out",ios::trunc);
    entrada.getline(input,200);
    quant = atoi(input);
    for(i=0;i<quant;i++) {
        pos = 0;
        entrada.getline(input,200);
        s = input;
        pos = s.find(' ');
        input[pos]='\0';
        n = atoi(input);
        m = atoi(&input[pos+1]);
        saida << "Case #" << i+1 << ": " << recycledBetween(n,m) << endl;
    }
    entrada.close();
    saida.close();
    return 0;
}

