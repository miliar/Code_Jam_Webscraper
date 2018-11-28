#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;
int abs(int x){
    if(x>0) return x;
    else return -x;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    while(cin >> n ){
       for(int k=1; k<=n; ++k){
            int m;
            scanf("%d",&m);
            char ch[103];
            int num[103];
            for(int i=0; i<m; ++i ){
                getchar();
                scanf("%c %d",&ch[i],&num[i]);

            }
//            for(int i=0; i<m; ++i ) cout << ch[i]<< " " <<num[i] << " ";
//            cout << endl;
            int count=0,B=1,A=1, t=0,flag=0;
            for(int i=0; i<m;++i){
                if(ch[i]=='B'){
                    if(abs(B-num[i])<=t && flag){
                        B=num[i];
                        t=0;
                    }else if(abs(B-num[i])>t && flag){
                        if(B>num[i]) B-=t;
                        else B+=t;
                        t=0;
                    }
              
                    if(B==num[i]){
                        count++;
                      
                        if(flag) t=1;
                        else t+=1;
                    }
                    else{
                        count+=abs(B-num[i]);
                        count++;
                       if(flag) t=abs(B-num[i])+1;
                       else t+=(abs(B-num[i])+1);
                        B=num[i];
                    }
                    flag=0;
                }else if(ch[i]=='O'){
                    if(abs(A-num[i])<=t && !flag){
                        A=num[i];
                        t=0;
                    }else if(abs(A-num[i])>t && !flag){
                        if(A>num[i]) A-=t;
                        else A+=t;
                        t=0;
                    }
                    if(A==num[i]){
                        count++;
                        if(!flag) t=1;
                        else t+=1;
                    }
                    else{
                        count+=abs(A-num[i]);
                        count++;
                        if(!flag) t=abs(A-num[i])+1;
                        else t+=(abs(A-num[i])+1);
                        A=num[i];
                    }
                    flag=1;
                }
            }
            cout << "Case #" << k << ": ";
            cout << count << endl;
        }
    }
    return 0;
}