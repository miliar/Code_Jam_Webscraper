#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream in("C:\\Documents and Settings\\Ankit Gupta\\Desktop\\A-large.in");  //A-small-attempt3.in");
    ofstream out("C:\\Documents and Settings\\Ankit Gupta\\Desktop\\A-large.out");
    int notimes;
    in>>notimes;
    int N,K;
    int num=0;
    int arr[1000];
    for(int coun=1;coun<=notimes;coun++){
                     in>>N>>K;
                     out<<"Case #"<<coun<<": ";
                     num=0;
                     int flag=0;
                     
                     while( K ){
                            
                            if( (K%2)==0 ){
                                break;
                            }
                                
                            arr[++num]=K%2;
                            if( num==N ){
                                 flag=1;
                                 break;
                            }
                            K= K/2;
                     }
                     
                     if( flag == 1 )
                         out<<"ON\n";
                        
                     else
                         out<<"OFF\n";                
                  
    }
    out.close();
   // int pp;cin>>pp;
    return 0;
}                     
                     
