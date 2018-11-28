#include <iostream>
#include <vector>
#include <string>
using namespace std;

class bignum{
      public:
      int Num[50];
      bignum(string str){
         ldfrmstr(str); 
      }
      void ldfrmstr(string str){
         for(int ii=0;ii<50;ii++) Num[ii]=0;
          int ind =0;            
          for(int ii=str.length()-1;ii>=0;ii--,ind++){
           if(str[ind]>='0' && str[ind]<='9') Num[ii]=str[ind] - '0';
          }
      }  
      string tostr(){
           string str;
           bool flag =0;
           int ind=0;   
           for(int ii=49;ii>=0;ii--){
              if(!flag && Num[ii]!=0 ) flag= true; 
              if(flag){
                 str = str+ char(Num[ii]+'0');
              }
           }
           if(!str.length()) str="0";
           return str;
       }
       bool operator <( bignum B){
            for(int ii=49;ii>=0;ii--){
              if(Num[ii]!=B.Num[ii]){
                 return (Num[ii]<B.Num[ii]);
              }
            }
            return false;  
       }
       bool operator !(void){
            for(int ii=0;ii<50;ii++)
              if(Num[ii] !=0)  return false;
            return true;  
       }     
       bool operator == (bignum B){
            return(!(*this-B));
       }
       //only gives the diff assumes lhs is bigger always
       bignum operator-( bignum B){
             bignum tmp("0");
             for(int ii=0;ii<50;ii++){
                if(Num[ii]>=B.Num[ii])
                 tmp.Num[ii] = Num[ii]-B.Num[ii];
                else{
                  tmp.Num[ii] = 10+Num[ii]-B.Num[ii];
                  B.Num[ii+1]+=1;
                }     
             }
            return tmp;
       } 
       bignum operator+(bignum B){
              bignum tmp("0");
              for(int ii=0;ii<50;ii++){
                    tmp.Num[ii]=Num[ii]+B.Num[ii];
                    if(tmp.Num[ii]/10){
                      B.Num[ii+1] +=1;
                      tmp.Num[ii] %=10;
                    }
              }
              return tmp;
       }            
};
bignum GCD(bignum A, bignum B){
    bignum big=A,small=A,tmp=A;
    if(A<B) big =B;
    else small=B;
    bignum smallx10("0"); 
    while(!!small){
      //cout<<"calculating the GCD of "<<big.tostr()<<" and "<<small.tostr()<<endl;    
       if(big==small) break;
       smallx10.ldfrmstr(small.tostr()+"0");
       tmp = smallx10;
       //if there is a magnitude difference
       while(smallx10<big){                                              
           tmp= smallx10;
           smallx10.ldfrmstr(smallx10.tostr()+"0");
       }
       if(!(tmp==smallx10)){
           tmp=big-tmp; //entered loop => exitted with value <big
           if(tmp== small) return small;
           if(tmp<small) {big =small; small=tmp;}
           else{big =tmp;}
       }
                            
         
       
       while(small<big)
         big= big-small;
                    
      //  cout<<"big now becomes" <<big.tostr()<<endl;                 
        tmp = small;
        small=big;
        big= tmp;
        
    }
     return small;
     //my algo is slightly complex then the below
    /* while(!!A){
      if(B<A){
        A= A-B; 
      }else{
        A =B-A;
        B= B-A; 
      }   
      unsigned tmp;
      cin>> tmp;   
     }
    return B;*/
}

 int main(){
    unsigned cas;
    cin >>cas;
    for(int cc=1;cc<=cas;cc++){
      int N; 
      string Str;
      cin >>N;
     /* bignum A("98000000"), B("2000000"),C("4000000");
      bignum F= A+B; 
      bignum D=B+B;
      bignum E= C-B;
      cout<< "A "<<A.tostr()<<endl;
      cout<< "B "<<B.tostr()<<endl;
       cout<< "C "<<C.tostr()<<endl;
      cout << "A+B "<<F.tostr()<<endl;
      cout <<"D==C " <<(D==C) <<endl;
      cout << "C-B " << E.tostr()<<endl;
      */
  
     vector <bignum> Ti;
      bignum min("0"); 
      int pos=1,posnxt=0;
      for(int i=0;i<N;i++){
       cin>>Str;
       bignum tmp(Str);
       Ti.push_back(tmp);
       if(i==0) min=tmp;
       else if(tmp<min) min = tmp;
       pos= posnxt++;
      } 
      vector <bignum> Di;	    
      for(int i=0; i<N-1; i++){
        if(Ti[i]==Ti[i+1]) continue;      
        if(Ti[i]<Ti[i+1]) {
         Di.push_back(Ti[i+1]-Ti[i]);
         }
        else{
         Di.push_back(Ti[i]-Ti[i+1]);
         }
         bignum Tmp = Di.back();
      }
      
      bignum gcd= Di[0];
      for(int i=0; i<Di.size()-1;i++){
         if(i==0)
           gcd = GCD(Di[i],Di[i+1]);
         else{ 
           gcd = GCD(gcd, Di[i+1]);  
         }
      }//got gcd
      bignum ngcd=gcd;
      while(ngcd<min) ngcd=ngcd+gcd;
      bignum y=ngcd-min;
      cout<< "Case #"<<cc<<": "<<y.tostr()<<endl;
 }
     cin >> cas;
}
