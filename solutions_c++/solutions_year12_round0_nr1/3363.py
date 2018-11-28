#include<fstream>
using namespace std;

bool pares(int k, int j);

int main(){
    
    fstream leer, escribir;
    
    leer.open("A-small-attempt0.in", ios::in);
    escribir.open("A-small-attempt0.out", ios::out);
    
    char arr[26];
    
    arr[0] = 'y';
    arr[1] = 'h';
    arr[2] = 'e';
    arr[3] = 's';
    arr[4] = 'o';
    arr[5] = 'c';
    arr[6] = 'v';
    arr[7] = 'x';
    arr[8] = 'd';
    arr[9] = 'u';
    arr[10] = 'i';
    arr[11] = 'g';
    arr[12] = 'l';
    arr[13] = 'b';
    arr[14] = 'k';
    arr[15] = 'r';
    arr[16] = 'z';
    arr[17] = 't';
    arr[18] = 'n';
    arr[19] = 'w';
    arr[20] = 'j';
    arr[21] = 'p';
    arr[22] = 'f';
    arr[23] = 'm';
    arr[24] = 'a';
    arr[25] = 'q';
    
    char linea[105];
    
    int T, i, j;
    
    leer>>T;
    leer.getline(linea, 102);
    for(i=1;i<=T;i++){
        leer.getline(linea, 102);
        j=0;
        escribir<<"Case #"<<i<<": ";
        while(linea[j]!=0){
            if(linea[j]==' ')
                escribir<<' ';
            else
                escribir<<arr[(int)(linea[j]-'a')];
            j++;
        }
        escribir<<endl;
    }
    
    leer.close();
    escribir.close();
    return 0;
}
