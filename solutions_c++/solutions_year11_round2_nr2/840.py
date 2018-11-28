#include<iostream>
#include<cmath>
using namespace std;
int vendor[201][2];//pos, num
int c,d;
void Proc(){
     double r=double(1000000)*double(1000000)*double(10);
     double l=double(0);
     double lastpos = -pow(double(10),20);
     double startpos,testValue;
     int i,j,k;
     bool ok;
     while(abs(r-l)>0.0000001){
          testValue = (r+l)/2;
		  if (testValue<1){
			  k=1;
		  }
          ok = true;
		  lastpos=-pow(double(10),20);
          for(i=1;i<=c;++i){
            // if ((vendor[i][0]-lastpos)>=d){
            ///    startpos=vendor[i][0]-testValue;
            // }else{
            //    startpos=
            // }
             if ((vendor[i][0]-testValue)>=lastpos){
                startpos =vendor[i][0]-testValue;
             }else
             if (lastpos-vendor[i][0]>testValue){
                ok=false;   
				break;
             }else{
                   startpos =  lastpos;
             }
             lastpos= startpos+ (vendor[i][1])*d;
			 if ((lastpos-d-vendor[i][0])>testValue){
				ok=false;
				break;
			 }
          }
          if (ok){
              r= testValue;
          }else{
              l= testValue;
          }
     }
     printf("%.10lf\n",(r+l)/2);
}
int main(){
    int t,tc,i;
  //  freopen("B-small-attempt0.in", "r", stdin);
  //   freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;++t){
       scanf("%d %d",&c,&d);
       for(i=1;i<=c;++i){
             scanf("%d %d",&vendor[i][0],&vendor[i][1]);
       }
       printf("Case #%d: ",t);
       Proc();
    }
  //  system("pause");
    return 0;
}
