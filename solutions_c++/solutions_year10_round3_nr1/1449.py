#include <iostream>
#include <vector>
using namespace std;
int main(){
    int ncasos,n,a,b,a1,b1;
    scanf("%d",&ncasos);
    for(int i=1;i<=ncasos;i++){
        scanf("%d",&n);
        int cont=0;
        for(int j=1;j<=n;j++){
            if(j==1)
            cin>>a>>b;
            else{
            cin>>a1>>b1;
            if(b<b1&&a>a1)
            cont++;
                else{
                    if(a<a1&&b>b1)
                    cont++;
                    else{
                        if(a>a1&&b<b1)
                        cont++;
                    }
                }
            }
        }
        cout<<"Case #"<<i<<": "<<cont<<endl;

    }
}
/*
2
3
1 10
5 5
7 7
2
1 1
2 2
*/
