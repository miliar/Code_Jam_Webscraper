#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    long T, ts=0;
    cin>>T;
    while(T--){
        ts++;
        printf("Case #%d: [",ts);

        string C, D, N, ans="";
        long c, d, n;
        cin>>c;if(c==1) cin>>C;
        cin>>d;if(d==1) cin>>D;
        cin>>n>>N;

        if(c==0&&d==0) ans=N;
        else
        for(long i=0;i<N.length();i++){
            ans+=N[i];

            long temp=ans.length();

            string var="";
            if(c==1) var=var+C[1]+C[0];
            if(c==1&&temp-2>=0)
                if(ans.substr(temp-2,2)==C.substr(0,2)||ans.substr(temp-2,2)==var) ans=ans.substr(0,temp-2)+C[2];

            int len=ans.length();

            if(d==1){
                char a='a', first=0, last=0;
                int p=0;
                for(int i=len-1;i>0&&p==0;i--){
                    if(ans[i]==D[0]) {a=D[0];last=i;}
                        else
                        if(ans[i]==D[1]) {a=D[1];last=i;}
                            else
                            continue;
                    for(int j=i-1;j>=0&&p==0;j--){
                        if(a==D[0]&&ans[j]==D[1]) {p=1;first=j;}
                        if(a==D[1]&&ans[j]==D[0]) {p=1;first=j;}
                    }
                }

                if(p==1) {ans="";}//ans.substr(0,first);if(last+1<len) ans+=ans.substr(last+1, len-last-1);}

            }
        }

        int lon=ans.length();
        for(int i=0;i<lon-1;i++){
            cout<<ans[i]<<", ";
        }
        if(lon>=1) cout<<ans[lon-1];
        cout<<"]\n";

    }

    return 0;
}
