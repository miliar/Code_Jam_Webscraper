#include<iostream>
#include<fstream>
using namespace std;
class BOT {
      public:
      int b;
      int s;
};
int main(){
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int i=1;
    int T,N;
    in>>T;
    int outt=1;
    while(T--){
           in>>N;
           char C;
           int M;
           bool SC[150]={0};
           BOT o[150],b[150];
           int oi=0,bi=0;
           SC[0]=1;
           int NN;
           NN=N;
           i=1;
           for(int iter=0;iter<150;iter++){
                   o[iter].b=b[iter].b=-1;
                   o[iter].s=b[iter].s=-1;
           }
           while(N--){
                //sc[N+1] = 0;
                in>>C>>M;
                if(C=='O'){
                         o[oi].b=M;
                         o[oi].s=i;
                         oi++;i++;
                }
                else{
                         b[bi].b=M;
                         b[bi].s=i;
                         bi++;i++;
                }
           }
           int time=0;
           int bp=1,op=1;
           oi=bi=0;
           bool flag = true;
           while(!SC[NN]){
                   flag = true;
                   if(o[oi].b!=-1){
                                 if(o[oi].b<op) op--;
                                 else if(o[oi].b>op) op++;
                                 else {
                                    if(SC[o[oi].s-1]){
                                                      SC[o[oi].s]=1;
                                                      oi++;
                                                      flag = false;
                                    }
                                 }
                   }
                   if(b[bi].b!=-1){
                                   if(b[bi].b<bp) bp--;
                                   else if(b[bi].b>bp) bp++;
                                   else if(flag){
                                    if(SC[b[bi].s-1]){
                                                      SC[b[bi].s]=1;
                                                      bi++;
                                    }
                                   }
                   }
                   time++;
           }
           
           cout<<"Case #"<<outt<<": "<<time<<"\n";
           out<<"Case #"<<outt<<": "<<time<<"\n";
           outt++;
    }
     out.close();
     in.close();    
     system("pause");
     return 0;
}                  
