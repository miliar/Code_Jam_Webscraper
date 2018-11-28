#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int T,A,B;
    int x,r,o,rp;
    ifstream myfile("input.txt");
    ofstream myOfile("output.in");
    if(myfile.is_open()&&myOfile.is_open()){
         myfile>>T;
         for(int i=0; i<T; i++){
                 myfile>>A>>B;
                 r=0;
                 o=1;
                 for(int j=A; j>9; j/=10, o*=10);
                 for(int j=A; j<B; j++){
                      if(j%10==0){
                                x = j;
                                int z=100;
                                while(x/z!=0 && x%z==0) z*=10;
                                if(x/z!=0) {
                                           int a = x/z;
                                           int b = x%z;
                                           x=b*o/z*10+a;
                                           }
                                           else{continue;}
                                  }else x=(j%10)*o+(j/10);
                      rp = 0;
                      while(x!=j){
                           if(x>j&&x<=B) rp++;
                           if(x%10==0){
                                int z=100;
                                while(x/z!=0 && x%z==0) z*=10;
                                if(x/z!=0) {
                                           int a = x/z;
                                           int b = x%z;
                                           x=b*o/z*10+a;
                                           }
                                           else{rp=0; break;}
                           }else x=x%10*o+x/10;
                      }
                 
                      r+=rp;
                 }
                 myOfile<<"Case #"<<i+1<<": "<<r<<endl;
         }
         myfile.close();
         myOfile.close();
    }else{
          cout<<"Error opening the files.";
    }
    return 0;
}
