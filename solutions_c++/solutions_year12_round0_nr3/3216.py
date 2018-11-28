#include<stdio.h>
#include<memory.h>
#include<set>
using std::set;
int main(){
    freopen("input3.in","r",stdin);
    freopen("output3_lib.txt","w",stdout);

    int t=0;
    scanf("%d" ,&t);

    int i=0;
    for(i=0;i<t;i++){
        int result=0;
        int digit=0;
        int A,B;
        //int a[8];
        //int b[8];
        //memset(a,0,sizeof(int)*8);
        //memset(b,0,sizeof(int)*8);
        //initial down
        scanf("%d",&A);
        scanf("%d",&B);

        int _t1=A;
        int pow=1;
        while(_t1!=0){
            //a[digit]=A%10;
            //b[digit]=B%10;
            _t1/=10;
            //B/=10;
            digit++;
            pow*=10;
        }
        pow/=10;
        //pre process over
        int n,m;
        for(n=A;n<B;n++){
            int num=n;
            int pos=1;//移动后pos位数。
            set<int> seti;
            for(pos=1;pos<digit;pos++){
                int temp=num;
                int _cur=0;
                for(_cur=0;_cur<pos;_cur++){
                    temp=(temp%10)*pow+temp/10;
                }
                //temp=num%10*pow+num/10;
                if(temp>A&&temp<=B&&temp>n){
                    //if(i==4){
                    //    printf("%d : %d\n",n,temp);
                    //}
                    seti.insert(temp);
                }
            }
            result+=seti.size();

        }


        printf("Case #%d: %d\n",i+1,result);
    }
    return 0;
}

