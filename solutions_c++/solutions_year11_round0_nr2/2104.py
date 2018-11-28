
/*
author:ravi shukla
*/

# include<iostream>
# include<cstdio>
# include<cstring>
# include<cstdlib>
# include<cmath>
# include<cassert>
# include<cctype>
# include<algorithm>

# include<vector>
# include<limits>
# include<list>
# include<stack>
# include<queue>
# include<set>
# include<map>
# include<bitset>
# include<sstream>
# include<deque>
# include<fstream>


#define REP(ii,a,b) for(int ii=a;ii<(int)(b);++ii)
#define REPD(ii,a,b) for(int ii=a;ii>(int)(b);ii--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define HASB(a,b) ((a&(1<<b))>0)
#define PI 3.14159265 

using namespace std;

typedef vector<int> VI;
typedef  int unsigned UI;
typedef long long LL;
typedef  long long unsigned LLU;

int main(){
    freopen("magl_in.IN","r+",stdin);
    freopen("mag_ou.txt","w+",stdout);
    int T,i=0,C,D,N,tlen;
    bool bflag=false;
    string temp,ele,ch,srep;
    char tch;
    map<string,string> mrep;
    multimap<char,char>mopp;
    multimap<char,char>::iterator it;
    cin>>T;
    while(i<T){
        i++;
        bflag=false;
        mrep.clear();mopp.clear();ele="";
        cin>>C;
        REP(ii,0,C){
            cin>>temp;
            ele=temp.substr(0,2);
            mrep[ele]=temp.substr(2,1);
            reverse(ele.begin(),ele.end());
            mrep[ele]=temp.substr(2,1);
        }
        cin>>D;
        REP(ii,0,D){
            cin>>temp;
            mopp.insert (pair<char,char>(temp[0],temp[1]));
            mopp.insert (pair<char,char>(temp[1],temp[0]));
        }
        cin>>N>>temp;
        ele=temp.substr(0,1);
        REP(ii,1,N){
       //     cout<<"121  "<<ele<<endl;
            ch=temp.substr(ii,1);
            if(ele.length()>0){
                srep=ele.substr(ele.length()-1,1)+ch;
                if(mrep.find(srep)!=mrep.end()){
                    ele=ele.substr(0,ele.length()-1)+mrep[srep];
                }else{
                    ele=ele+ch;
                }
            }else{
                ele=ch;
            }
       //     cout<<"345  "<<ele<<endl;
            tch=ele[ele.length()-1];bflag=false;
            if(mopp.find(tch)!=mopp.end()){
                tlen=ele.length();
                REP(jj,0,tlen-1){
                    for(it=mopp.equal_range(tch).first;it!=mopp.equal_range(tch).second; ++it){
                        if(ele[jj]==(*it).second){
       //                     cout<<"420  "<<ele[jj]<<" "<<(*it).second<<endl;
                            bflag=true; ele="";
                            break;
                        }
                    }
                    //cout<<bflag<<endl;
       //             cout<<"890  "<<ele<<endl;
                    if(bflag==true){                       
                        break;
                    }
                       //cout<<"798 "<<ele<<endl;
                }
            }
            
        }
        cout<<"Case #"<<i<<": [";
        if(ele.length()>0)
            cout<<ele[0];
        REP(ii,1,ele.length()){
        cout<<", "<<ele[ii];
    }
    cout<<"]"<<endl;
    }
    return 0;
}














