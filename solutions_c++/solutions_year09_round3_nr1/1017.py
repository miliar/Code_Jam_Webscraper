#include <iostream>
#include <set>
using namespace std;

int main(){
    int N;
    cin>>N;
    for(int i=1;i<=N;++i){
        char str[100];
        int change[100];

        set<char> s;
        cin>>str;
        for(int j=0;j<strlen(str);++j){
            s.insert(str[j]);
        }
        int x=s.size();
        if(x==1)x=2;

        int map[100];
        memset(map,-1,100*sizeof(int));
        int result[100];
        memset(result,0,100*sizeof(int));
        int map2[40];
        memset(map2,0,40*sizeof(int));

        int start=0,len=strlen(str);


        for(int j=0;j<len;++j){
            if(map[str[j]-'0']==-1){
                if(start==0){
                    map[str[j]-'0']=1;
                    start++;
                }else if(start==1){
                    map[str[j]-'0']=0;
                    start++;
                }else
                map[str[j]-'0']=start++;
            }
//            cout<<str[j]<<"###"<<map[str[j]-'0']<<endl;
            change[j]=map[str[j]-'0'];
//            cout<<change[j]<<"%";
        }
        for(int j=0;j<len;++j){
            if(j==0)map2[j]=1;
            else map2[j]=x*map2[j-1];
        }
        for(int j=1;j<=len;++j){
//            cout<<change[len-j]<<"#"<<map2[j-1]<<endl;
            int temp=change[len-j]*map2[j-1];
            int count=0;
            while(temp>0){
                result[count++]+=temp%10;
                if(result[count-1]>100000){
                    result[count]+=result[count-1]/10;
                    result[count-1]%=10;
                }
                temp/=10;
            }
        }
        cout<<"Case #"<<i<<": ";
        for(int j=0;j<90;++j){
            if(result[j]>9){
                result[j+1]+=result[j]/10;
                result[j]%=10;
            }
        }
        start=0;
        for(int j=89;j>=0;--j){
            if(start!=0){
                cout<<result[j];
            }
            if(start==0){
                if(result[j]!=0){
                    cout<<result[j];
                    start=1;
                }
            }
        }
        cout<<endl;
    }
    return 0;
}
