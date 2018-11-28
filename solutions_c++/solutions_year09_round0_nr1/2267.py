#include<iostream>
//#include<conio.h>
#include<fstream>
using namespace std;


void check_validity(int level,int input_no);

int L,D,N;// L->length of each word, D->no. of words given, N->no. of test cases
char input_string[5000][16];
char test_string[500];
int p[15][2],n,flag;
//int index[26][5000][15],index_count[26][15];
    

int main(){
    
    
    fstream input;
    input.open("A-large(2).in", ios::in);
    input>>L>>D>>N;
    for(int i=0;i<D;i++)
        input>>input_string[i];
        
    fstream output;
    output.open("A-large.out", ios::out);
    
    int letter_count;
    for(int i=0;i<N;i++){
            n=0;letter_count=0,
            input>>test_string;
            for(int ii=0;letter_count<L;ii++){
                   if (test_string[ii]!='('){ 
                       p[letter_count][0]= ii;
                       p[letter_count++][1]= ii;
                       continue;
                   }
                   else 
                        {
                            p[letter_count][0]=ii+1;
                            while(test_string[ii]!=')'){
                                    ii++;
                            } 
                            p[letter_count++][1]= ii-1;
                        }  
            }
           // int m;
            for (int j=0;j<D;j++){
            flag=0;
            check_validity(0,j);
            }       
            //cout<<endl;
            output<<"Case #"<<(i+1)<<": "<<n<<endl;
           // cout<<"Case #"<<(i+1)<<": "<<n<<endl;
    }
    input.close();
    output.close();//getch();
    return 0;
}
void check_validity(int level,int input_no){

    for (int i=0;i<=(p[level][1]-p[level][0]);i++){
        if (flag==1) break;
        if (test_string[p[level][0]+i]==input_string[input_no][level]){
           if (level==(L-1)){ 
                  n++;//cout<<"#"<<n<<"#";
                  flag=1;
                  return;
                  }
           if (level<L) check_validity(level+1,input_no);
        }
    }{flag=1;return; }       
              
}
