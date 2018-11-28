# include <stdio.h>
# include <stdlib.h>
# include <string>
# include <iostream>
# include <map>
# include <string.h>
using namespace std;
int main(){
    freopen("out.txt","w",stdout);
    string temp,help,ayu,res,Opu[50];
    int c,i,j,k,com,opu,n,h;
    scanf("%d",&c);
    map <string,string> Com;
    for(k=1;k<=c;k++){
        Com.clear();
        scanf("%d",&com);
        for(i=0;i<com;i++){
            cin>>temp;
            help=temp.substr(0,2);
            ayu=temp.substr(2,1);
            Com[help]=ayu;
            help[0]=temp[1],help[1]=temp[0];
            Com[help]=ayu;
        }
        scanf("%d",&opu);
        for(i=0;i<opu;i++){
            cin>>Opu[i];
        }
        scanf("%d",&n);
        cin>>temp;
        res="";
        for(i=0;i<temp.size();i++){
            if(res.size()==0){
                res+=temp.substr(i,1);
            }else{
                help="  ";
                help[0]=res[res.size()-1],help[1]=temp[i];
                if(Com[help].size()>0){
                    res[res.size()-1]=Com[help][0];
                }else{
                    res+=temp.substr(i,1);
                }
            }
            for(j=0;j<opu;j++){
                if(res[res.size()-1]==Opu[j][0]){
                    for(h=0;h<res.size();h++){
                        if(res[h]==Opu[j][1]){
                            res="",j=opu;
                        }
                    }
                }
                if(res[res.size()-1]==Opu[j][1]){
                    for(h=0;h<res.size();h++){
                        if(res[h]==Opu[j][0]){
                            res="",j=opu;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<k<<": [";
        for(i=0;i<res.size();i++){
            cout<<res[i];
            if(i<res.size()-1){
                cout<<", ";
            }
        }
        cout<<"]"<<endl;
    }
    return 0;
}
