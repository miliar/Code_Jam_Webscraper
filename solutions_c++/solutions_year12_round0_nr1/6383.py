#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<list>
#include<set>
#include<map>
#include<climits>
#define ff(i,a,b) for (int i=a;i<b;i++)
#define ffd(i,a,b) for (int i=a;i>=b;i--)
#define f(i,n) ff(i,0,n)
#define In(i,a,b) (i>=a && i<=b)
#define offset 200
#define ll long long int
#define e 2.71828
using namespace std;

int main(){
char alfa[30]="yhesocvxduiglbkrztnwjpfmaq";
char linea[150];
int n;
cin>>n;
gets(linea);
f(i,n){
    gets(linea);
    int tam=strlen(linea);
    printf("Case #%d: ",i+1);
    f(j,tam){
        if (isalpha(linea[j]))putchar(alfa[linea[j]-'a']);
        else putchar(' ');
    
    }
    puts("");
}

return 0;}
