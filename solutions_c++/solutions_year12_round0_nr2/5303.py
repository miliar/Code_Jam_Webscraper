#include <fstream>

main()

{
      using namespace std;
long a,b,c,d,x,o=0,t,u=1,g=2;
ifstream I("input.txt");
ofstream O("output1.txt");
I>>t;
for(int j=o;j<100;j++){
        o=0;
I>>a>>b>>c;
if (c==1) {d=1,g=0;}
else {d=c*3-4;g=2;}
 for (int i=0;i<a;i++){
  I>>x;
  if(x>=d+g) o++;
  else if ((x>=d)& (b!=0)) {o++;b--;}
}
if (u==100){O<<"Case #"<<u<<':'<<' '<<o;}
else
O<<"Case #"<<u<<':'<<' '<<o<<endl; u++;}
return 0;
}
