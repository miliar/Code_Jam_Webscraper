using namespace std;
#include <iostream>
#include <fstream>
#include <math.h>

char* f_state(long int K,long int N,long int i){
         char result[3];
         long int temp;
         temp=(int) floor(K/pow(2,N));
         temp=K-(int) (temp*pow(2,N));
//         cout<<"[["<<i<<": "<<N<<" "<<K<<" "<<temp+1<<" "<<pow(2,N)<<"]]\n";
         if(temp+1==(int)pow(2,N)) return "ON";
         else return "OFF";

}

int main(){
    long int T,N,K,i;

    ofstream outfile;
    ifstream infile;
    
    infile.open ("A-large.in");
    outfile.open ("A-large.out");

    infile >> T;
    
    for(i=1;i<=T;i++){
        infile >> N;
        infile >> K;
//       outfile << "Case #"<<i<<": "<<f_state(K,N,i)<<N<<" "<<K<<" "<<pow(2,N)<<"\n";
       outfile << "Case #"<<i<<": "<<f_state(K,N,i)<<"\n";
    }
//    cin>>T;
    outfile.close();
    infile.close();    
    return (0);
}
