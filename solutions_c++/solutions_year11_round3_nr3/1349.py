#include<iostream.h>
#include<fstream.h>

int main()
{

ifstream f1;
ofstream f2;
f1.open("input.txt");
f2.open("output.txt");

int t;
f1>>t;
int k=1;
while(t--)
{

    int n,l,h;
    int num[100];
    f1>>n>>l>>h;
    for (int i=0;i<n;i++)
{
f1>>num[i];
}
   int flag=0;
int ans=0;
for(int i=l;i<=h;i++){
 flag=0;
    for(int j=0;j<n;j++){
        if(!(num[j]%i==0||i%num[j]==0)){
            flag=1;
            break;
        }
    }
    if(flag==0){
        ans=i;
        break;
    }
}


            if(flag==1){
                f2<<"Case #"<<k<<": NO\n";
                k++;
            }
            else {
                f2<<"Case #"<<k<<": "<<ans<<"\n";
                k++;
            }
}
}



