#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int caso;
    cin>>caso;
    int c[26];
    c[1]= 0;
c[2]= 1;
c[3]= 2;
c[4]= 3;
c[5]= 5;
c[6]= 8;
c[7]= 14;
c[8]= 24;
c[9]= 43;
c[10]= 77;
c[11]= 140;
c[12]= 256;
c[13]= 472;
c[14]= 874;
c[15]= 1628;
c[16]= 3045;
c[17]= 5719;
c[18]= 10780;
c[19]= 20388;
c[20]= 38674;
c[21]= 73562;
c[22]= 140268;
c[23]= 268066;
c[24]= 513350;
c[25]= 984911;
    for(int casos=0;casos<caso;casos++){
        int dev=0;
        int t;
        cin>>t;
        cout<<"Case #"<<casos+1<<": "<<c[t]%100003<<endl;
    }
    
    //system("pause");
    return 0;
}


