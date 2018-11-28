#include <iostream>
#include <vector>
using  namespace std;
vector <int> a,b,total; 

int main(){
    int n,ntc,num;
    cin >> ntc;
    for(int tc=1;tc<=ntc;tc++){
         cin >> n;
         char s;
         a.clear();
         b.clear();
         total.clear();
         for(int i=1;i<=n;i++){
             cin >> s >> num;
             if(s=='O'){
               a.push_back(num);
               total.push_back(num);
             }
             else{
               b.push_back(num+1000);
               total.push_back(num+1000);
             }
         }
         a.push_back(10001);
         b.push_back(10001);
         total.push_back(10001);
         int nowa=1,nowb=1001,tara=a[0],tarb=b[0],tmpa=0,tmpb=0,tmptotal=0,tartotal=total[0],time=0,ck=0,ck2=0;
         while(1){
                  ck=ck2=1;
             if(nowa==tartotal || nowb==tartotal ){
                   if(tara==tartotal && tara==nowa)
                       tmptotal++,tmpa++,ck=0; 
                   if(tarb==tartotal && tarb==nowb)
                       tmptotal++,tmpb++,ck2=0;
                   tartotal=total[tmptotal];
                   tara = a[tmpa];
                   tarb = b[tmpb];                              
             }
              if(nowa!=tara && ck)
                if(nowa > tara) nowa--;
                else nowa ++;
             if(nowb!=tarb  && ck2)
                if(nowb > tarb) nowb--;
                else nowb ++;
             time++;
          //   cout<< "now:" <<time << " " << nowa << " " << nowb<<endl;
             if(tmptotal==n)break;
         }
         cout << "Case #"<<tc<<": " << time << endl;
    }
}
