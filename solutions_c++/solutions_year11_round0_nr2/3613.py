#include<map>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;



bool verifycombine(string &list,vector<string>combs){
    int l = list.size()-1;
    for(int i = 0;i<combs.size();i++){
        if((list[l]==combs[i][0] && list[l-1]==combs[i][1]) || (list[l]==combs[i][1] && list[l-1]==combs[i][0])){
            //replace
            list.replace( list.size()-2 , 2, 1 , combs[i][2]  );
            return true;

        }
    }
    return false;
}

void verifyopposed(string &list,vector<string>oppo){
    map<char,int>mp;
    char l = list[ list.size()-1 ];

    for(int i = 0; i<list.size();i++){
        mp[list[i]]++;
    }
    //cout<<list<<endl;
    for(int i = 0;i<oppo.size();i++){
        if(oppo[i][0]==l || oppo[i][1]==l){
            if(mp[ oppo[i][0]  ] && mp[ oppo[i][1]  ]){
                //clear
                list.clear();
                return;
            }
        }
    }
}

int main(){
    int T;
    cin>>T;
    int k = 1;
    while(T--){
        /****************************/
        int C;
        cin>>C;
        vector<string>combine;
        string aux;
        while(C--){
            cin>>aux;
            combine.push_back(aux);
        }
        int D;
        cin>>D;
        vector<string>opposed;
        while(D--){
            cin>>aux;
            opposed.push_back(aux);
        }
        int N;
        cin>>N; //no sirve :P
        string str;
        cin>>str;
        /******************************/
        string elemlist;
        elemlist+=str[0]; //condicion : 1<=N

        for(int i = 1;i<N;i++){
            int j = 0;
            elemlist+=str[i];
        
        //   cout<<elemlist<<"*"<<endl;

            if(verifycombine(elemlist,combine)){}
            //cout<<"?"<<endl;
            else{ verifyopposed(elemlist,opposed);}
        }
        //cout<<elemlist<<endl;i
        printf("Case #%d: [",k++);
        for(int i = 0; i< elemlist.size(); i++){
            if(i>0&& i< elemlist.size())printf(", ");
            printf("%c",elemlist[i]);
        }
        printf("]\n");
    }

return 0;
}
