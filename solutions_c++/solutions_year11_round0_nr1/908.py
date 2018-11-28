#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Alarge.txt","w",stdout);
    int t;
    cin>>t;
    int kases=0;
    while(t--){
        int n;
        cin>>n;
        int odes[100],bdes[100];
        int o=0,b=0;
        int ar[1000][2];
        for(int i=0;i<n;++i){
            char a;int b;
            cin>>a>>b;
            ar[i][0]=a;
            ar[i][1]=b;
            /*if(a=='O')
                odes[o++]=b;
            else if(a=='B')
                bdes[b++]=b;
            *///printf("%c %d\n",a,b);
        }
        int oat=1,bat=1,opush=0,bpush=0;
        int time=0;
        int olast=0,blast=0;
        int timeoflastpush=0;
        for(int i=0;i<n;++i){
            if(ar[i][0]=='O'){
                int dis=abs(ar[i][1]-oat);
                if (timeoflastpush-opush>=dis)
                    timeoflastpush++;
                else
                    timeoflastpush+=(dis-timeoflastpush+opush)+1;
                oat=ar[i][1];
                opush=timeoflastpush;

            }
            else{
                int dis=abs(ar[i][1]-bat);
                if (timeoflastpush-bpush>=dis)
                    timeoflastpush++;
                else
                    timeoflastpush+=(dis-timeoflastpush+bpush)+1;
                bat=ar[i][1];
                bpush=timeoflastpush;
            }
        }
        ++kases;
        printf("Case #%d: ",kases);
        printf("%d\n",timeoflastpush);
        //cin>>kases;

    }
    return 0;
}
