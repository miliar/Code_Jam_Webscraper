#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

char line[1000];
int dup_count[10];

int get_next_number(int* pos){
    while(line[*pos] == ' '){
        *pos = (*pos) + 1;              
    }
    
    int result = 0;
    while(1){
        char next = line[*pos];
        if(next == ' ' || next == '\0'){
            break;
        }
        int val = next-'0';
        result = result*10 + val;
        *pos = (*pos) + 1;          
    } 
    return result;
}

void get_input(int* N,int* M){
    int position=0;
    
    *N = get_next_number(&position);
    *M = get_next_number(&position); 
}

int shift(int num,int pos,int pow){   
        int result = num;
        for(int i=0;i<pos;i++){
                result = pow*(result%10) + (result/10);
        }
        return result;
}

int process(int N,int M)
{
    for(int r=0;r<10;r++)
       dup_count[r]=0;
    int out=0;
    int size=0;
    int pow=1;
    int temp =N;
    while(temp > 0){
      size++;
      pow = pow* 10;
      temp /= 10;
    }
    pow = pow /10;
    for(int i=N;i<=M;i++){
     for(int j=1;j<size;j++){
         int result = shift(i,j,pow);
         if(result>=N and result <=M and result !=i){
            out++;
         }
     }
    }
     return out/2;
}

int main(int argc, char *argv[])
{
    ifstream read;
    read.open("C-small-attempt0.in");
    ofstream write;
    write.open("output.txt");
    
    read.getline(line,1000);
    int T = atoi(line);
    
    int j=1;
    while(T--){
        write << "Case #"<<j++<<": ";
        read.getline(line,1000);
        int N,M;
        get_input(&N,&M);
        int out = process(N,M);       
        write << out <<"\n";    
     }
   system("PAUSE");
    return EXIT_SUCCESS;
}
