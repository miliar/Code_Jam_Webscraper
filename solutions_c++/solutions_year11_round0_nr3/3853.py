#include<iostream.h>
#include<math.h>
#include<fstream.h>

int selec[15];
void combine(int n)
{int i=0;
memset(&selec, 0, sizeof(int)*15);

    while(n!=0){

        selec[i]=n%2;
        n=n/2;
    i++;
    }

}

long long add(int a,int b)
{

    int n=0;
    long long ans=0;
    while(!(a==0&&b==0)){
        if((a%2==1&&b%2==0)||(a%2==0&&b%2==1)){
            ans+=pow(2,n);

        }
        a=a/2;
        b=b/2;

    n++;
    }
    return ans;
}



int main()
{

ifstream f1;
f1.open("input.in");
ofstream f2;
f2.open("output.txt");


int t=0;
f1>>t;
int k=1;
while(k<=t)
{
    int n;
    f1>>n;
    long long c[15];
    for(int i=0;i<n;i++){
        f1>>c[i];
    }
    int ans=-1;

for(int i=1;i<pow(2,n);i++){
    combine(i);

    long long sum1=0,sum2=0;long long num=0;
    for(int j=0;j<n;j++){

        if(selec[j]==1){
            sum1=add(c[j],sum1);
        }
        else {num=num+c[j];
            sum2=add(c[j],sum2);
        }
    }


if(sum1==sum2){


    if(ans==-1){
        ans=num;}
        else if(num>ans){
            ans=num;}


}
}
if(ans==-1){
    f2<<"Case #"<<k<<": NO\n";
}
else{
    f2<<"Case #"<<k<<": "<<ans<<"\n";}

    k++;
}
}
