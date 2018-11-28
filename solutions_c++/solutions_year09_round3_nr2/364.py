#include <fstream>
#include <vector>
#include <math.h>
using namespace std;



int main(){
    ifstream in("b.in");
    ofstream out("b.out");
    
    int t, k=0, n, i, j, a, b, c;
    in>>t;
    
    while (k<t){
          k++;
          in>>n;
          vector < vector <int> >vv;
          vv.clear(); 
          for (i=0; i<n; i++){
              vector <int>v;
              v.clear();
              for (j=0; j<6; j++){
                  in>>a;
                  v.push_back(a);
                  }
              vv.push_back(v);
              }
          
          double cmi[3]; a=0; b=0; c=0;
          double cmt[3];
          double res=0;
          for (i=0; i<n; i++){
              a+=vv[i][0];
              b+=vv[i][1];
              c+=vv[i][2];
              }
          cmi[0]=a/double(n);
          cmi[1]=b/double(n);
          cmi[2]=c/double(n);
          for (i=0; i<n; i++){
              a+=vv[i][3];
              b+=vv[i][4];
              c+=vv[i][5];
              }
          cmt[0]=a/double(n);
          cmt[1]=b/double(n);
          cmt[2]=c/double(n);

          if (cmi[0]==cmt[0] && cmi[1]==cmt[1] && cmi[2]==cmt[2]){
             
             res=sqrt( pow((cmi[0]), 2.0) +  pow((cmi[1]), 2.0) + pow((cmi[2]), 2.0) );
             out<<"Case #"<<k<<": "<<res<<' '<<0<<endl;
             }
             
          else {
               if (cmi[0]==0 && cmi[1]==0 && cmi[2]==0){
                            out<<"Case #"<<k<<": "<<0<<' '<<0<<endl;
                  }
               else {
                    
                    /*
                    double vec[3];
                    double hyp;
                    vec[0]=cmt[0]-cmi[0];
                    vec[1]=cmt[1]-cmi[1];
                    vec[2]=cmt[2]-cmi[2];
                    double parc=(vec[0]*-1*cmi[0])+(vec[2]*-1*cmi[2])+(vec[1]*-1*cmi[1]);
                    double parc2=(sqrt(pow(vec[0], 2.0)+pow(vec[1], 2.0)+pow(vec[2], 2.0))  )*(sqrt(pow(cmi[0], 2.0)+pow(cmi[1], 2.0)+pow(cmi[2], 2.0))  );
                    parc/=parc2;
                    hyp=sqrt(pow(cmi[0], 2.0)+pow(cmi[1], 2.0)+pow(cmi[2], 2.0))  ;
                    
                    double tita=acos(parc);
                    double sentita=sin(tita);
                    double costita=cos(tita);
                    
                    double op=sentita*hyp;
                    double ady=costita*hyp;
                    */
                    double t=-1*(cmi[0]*(cmt[0]-cmi[0]) + cmi[1]*(cmt[1]-cmi[1]) + cmi[2]*(cmt[2]-cmi[2])) / (pow((cmt[2]-cmi[2]), 2.0) + pow((cmt[1]-cmi[1]), 2.0) + pow((cmt[0]-cmi[0]), 2.0));
                    double res;
                    if (t>=0){
                       double v1=cmi[1]*cmt[2]-cmi[2]*cmt[1];
                       double v2=cmi[2]*cmt[0]-cmi[0]*cmt[2];
                       double v3=cmi[0]*cmt[1]-cmi[1]*cmt[0];
                       double v4=cmt[0]-cmi[0];
                       double v5=cmt[1]-cmi[1];
                       double v6=cmt[2]-cmi[2];
                       
                       res= (sqrt (pow(v1, 2.0)+pow(v2, 2.0)+pow(v3, 2.0)) ) / (sqrt (pow(v4, 2.0)+pow(v5, 2.0)+pow(v6, 2.0)));
                       out<<"Case #"<<k<<": "<<res<<' '<<t<<endl;
                       }
                    else {
                         res=sqrt (pow(cmi[0], 2.0)+pow(cmi[1], 2.0)+pow(cmi[2], 2.0) );
                       out<<"Case #"<<k<<": "<<res<<' '<<0<<endl;
                         
                         }
                    }
               
               
               }
          }
    
    }
