#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
#include<string>
#include<vector>
#include<sstream>
#include<string.h>
#include<unistd.h>
#include<map>

using namespace std;

int main(int argc, char *argv[]){



    freopen("C-small-attempt0.in","r",stdin);
    freopen("outputc.txt","w",stdout);

    //freopen("input.txt","r",stdin);

    vector<string>v;

    int tol;
    while(cin>>tol){
        int i,k,m,u,n;
        int start,end;
        for(i=0;i<tol;i++){
            int ans=0;
            printf("Case #%d: ",i+1);
            cin>>start>>end;
            for(k=start;k<=end;k++){
                string s1;
                char tmp[10];
                sprintf(tmp,"%d",k);
                s1=tmp;
                v.clear();
                for(u=1;u<s1.length();u++){
                    string cal=s1;
                    cal.insert(0,cal.substr(cal.length()-u,u));
                    cal.erase(cal.length()-u,u);
                    int index=0;
                    while(cal[index]=='0'){
                        cal.erase(cal.begin());
                    }
                    v.push_back(cal);
                }

                for(m=k+1;m<=end;m++){
                    string s2;
                    char tmp[100];
                    memset(tmp,0,sizeof(tmp));
                    sprintf(tmp,"%d",m);
                    s2=tmp;
                    for(n=0;n<v.size();n++){
                        if(s2==v[n]){
                            ans++;
                            break;
                        }
                    }
                }
            }
            cout<<ans<<endl;
        }

    }
    return 0;
}

