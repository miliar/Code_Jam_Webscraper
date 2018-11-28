#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<set>
#include<list>
#include<algorithm>
#define tr(container, it) for(typeof(container.begin()) it =container.begin();it!=container.end();it++)
using namespace std;
typedef pair<char, char> pcc;

int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-output1.out","w",stdout);
    int T,N,C,D;
    scanf("%d",&T);
    char str[4],inp[1000];
    for(int I=1;I<=T;I++){
        map<pcc, char> com;
        map<char, list<char> > opp;
        set<char> st;
        scanf("%d",&C);
        for(int i=0;i<C;i++){
            scanf("%s",str);
            com[pcc(str[0],str[1])]=str[2];
            com[pcc(str[1],str[0])]=str[2];
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf("%s",str);
            opp[str[0]].push_back(str[1]);
            opp[str[1]].push_back(str[0]);
        }
        scanf("%d",&N);
        //char ans[N+1];
        vector<char> ans;
//        int counter=0;
        scanf("%s",inp);
        int i=1;
        for(i=1;i<N-1;i++){
            bool con=true;
            if(opp.find(inp[i-1])!=opp.end()){
                tr(opp[inp[i-1]],it){
                    if(st.find(*it)!=st.end()){
                        st.clear();
                        //counter=0;
                        ans.clear();
                        i++;
                        break;
                    }
                }
            }
            if(com.find(pcc(inp[i-1],inp[i]))!=com.end()){
                st.insert(com[pcc(inp[i-1],inp[i])]);
                //ans[counter++]=com[pcc(inp[i-1],inp[i])];
                ans.push_back(com[pcc(inp[i-1],inp[i])]);
                i++;
                con=false;
            }
            else if(opp.find(inp[i])!=opp.end()){
               // cout<<"reached"<<i<<endl;
                tr(opp[inp[i]],it){
                    if(st.find(*it)!=st.end() || *it==inp[i-1]){
                        st.clear();
                        //counter=0;
                        ans.clear();
                        con=false;
                        i++;
                        break;
                    }
                }
            }
            if(con){
               // cout<<"here"<<i<<endl;
               //cout<<inp[i-1]<<endl;
                st.insert(inp[i-1]);
//                ans[counter++]=inp[i-1];
                ans.push_back(inp[i-1]);
            }
//            cout<<i<<" "<<ans.size()<<endl;
        }
                bool cond=false;        
         if(opp.find(inp[i-1])!=opp.end()){

                tr(opp[inp[i-1]],it){
                    if(st.find(*it)!=st.end()){
                        st.clear();
                        //counter=0;
                        ans.clear();
                        cond=true;
                        break;
                    }
                }
                if(cond && i==N-1){
                    st.insert(inp[i-1]);
                    ans.push_back(inp[i-1]);
                }
            }
        
        if(!cond && i==N){
            st.insert(inp[N-1]);
//            ans[counter++]=inp[N-1];
            ans.push_back(inp[N-1]);
        }
        else if(!cond){
            bool con=true;
            if(com.find(pcc(inp[i-1],inp[i]))!=com.end()){
                ans.push_back(com[pcc(inp[i-1],inp[i])]);
                st.insert(inp[i]);
                con=false;
            }
            else if(opp.find(inp[i])!=opp.end()){
                tr(opp[inp[i]],it){
                    if(st.find(*it)!=st.end() || *it==inp[i-1]){
                        st.clear();
                        //counter=0;
                        ans.clear();
                        con=false;
                    }
                }
            }
            if(con){
                ans.push_back(inp[N-2]);
                ans.push_back(inp[N-1]);
            }
        }
//        cout<<ans.size()<<endl;
        printf("Case #%d: [",I);
        vector<char>::iterator It=ans.begin();
        if(It!=ans.end()){printf("%c",*It);
            It++;
        }
        for(;It!=ans.end();It++)
            printf(", %c",*It);
        printf("]\n");
    }
    return 0;
}
