#include <iostream>
#include <fstream>

using namespace std;
int main(){
ifstream in("A-large.in");
ofstream out("A-large.out");
long long int N, n, a, b, c, d, x, y, m, k, i, h, j, cont;
long long int ar[9], ar2[9][2];
in>>N;
k=N;
while (N>0){
for (i=0; i<9; i++){ar[i]=0;ar2[i][0]=i/3; ar2[i][1]=i%3;}
cont=0;
in>>n>>a>>b>>c>>d>>x>>y>>m;
//ar[0][0]=x;
//ar[0][1]=y;
//out<<ar[0][<<' '<<y<<endl;
ar[(x%3)*3+(y%3)]++;
for (i=1; i<n; i++){
x=((a%m)*(x%m)+b)%m;
y=((c%m)*(y%m)+d)%m;
//ar[i][0]=x;
//ar[i][1]=y;
//out<<x<<' '<<y<<endl;
ar[(x%3)*3+(y%3)]++;
//ar2[(x%3)*3+(y%3)][0]=x;
//ar2[(x%3)*3+(y%3)][1]=y;
}
//for (i=0; i<9; i++)out<<ar[i]<<endl;
//for (i=0; i<9; i++)out<<ar2[i][0]<<' '<<ar2[i][1]<<endl;
/*for (i=0; i<n; i++){
        for (j=i+1; j<n; j++){
                for (h=j+1; h<n; h++){
                        int p=ar[i][0]+ar[j][0]+ar[h][0];
                        int q=ar[i][1]+ar[j][1]+ar[h][1];
                        //out<<p<<' '<<q<<endl;
                        if (p%3==0 && q%3==0)cont++;
                        
                }
        }
}*/
for (i=0; i<9; i++)
for (j=i+1; j<9; j++)
for (h=j+1; h<9; h++){
int p=(ar2[i][0]+ar2[j][0]+ar2[h][0])%3;
int q=(ar2[i][1]+ar2[j][1]+ar2[h][1])%3;
if (p==0 && q==0){
//out<<i<<' '<<j<<' '<<h
cont+=ar[i]*ar[j]*ar[h];
}
}
for (i=0; i<9; i++){
cont+=(ar[i]*(ar[i]-1)*(ar[i]-2))/6;
}
out<<"Case #"<<k-N+1<<": "<<cont<<endl;
N--;
}
return 0;
}
