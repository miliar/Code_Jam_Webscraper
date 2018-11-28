#include<fstream>
#include<iostream>
#include <cstdlib>

using namespace std;
main()
{
int tc,j,total,temp2,k,mul;
int a,b,c,flag[1000],i,nd;
ifstream f;ofstream f2;
f.open("C:/Turboc3/input.txt");
f2.open("C:/Turboc3/o.txt");
f >> tc;
for(int i=0;i<tc;i++) {
    total=0;
    f >> a >> b;
    for(k=a;k<=b;k++) {
        flag[k]=0;
    }
    for(k=a;k<=b;k++) {
        if(flag[k]!=0) continue;
        flag[k]=1;
        c=k;
        nd=1;mul=1;
        if(c/10) {nd=2;mul=10;}
        if(c/100) {nd=3;mul=100;}
        if(c/1000) {nd=4;mul=1000;}
        for(j=0;j<nd-1;j++) {
            temp2=c%10;
            c=c/10;
            c+=temp2*mul;
            if((c!=k)&&(c<=b)&&(c>=a)&&(flag[c]==0)) {
                total++;
            }
        }
    }
    f2 << "Case #"<<i+1<<": "<<total<<"\n";
}
f.close();
f2.close();
return 0;
}