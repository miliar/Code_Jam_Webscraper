#include<cstdio>
#include<iostream>
#include<cstring>
#include<map>

using namespace std;

int main()
{
    int T,N,S,p,i,j,num,max1,max2,count;

    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);

    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%d %d %d",&N,&S,&p);
        count=0;
        for(j=0;j<N;j++){
            scanf("%d",&num);
            if (num%3==0) {
                max1=num/3;
                if(num!=0)max2=(num/3)+1;
                else max2=0;
            }
            else if(num%3==1) {
                max1=(num/3)+1;
                if(num!=1)max2=(num/3)+1;
                else max2=1;
            }
            else if(num%3==2) {
                max1=(num/3)+1;
                max2=(num/3)+2;
            }

            if(max1 >= p) count++;
            else if(max1<p && max2>=p && S>0) {
                count++;
                S--;
            }
            else if(max1<p && max2>=p && S<=0) continue;
            else if (max2 < p) continue;
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
