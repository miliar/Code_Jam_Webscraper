#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
using namespace std;
int convert(string time){
        return atoi(time.substr(0,2).c_str())*100+atoi(time.substr(3,2).c_str());
}
struct myclass {
  bool operator() (int i,int j) { return (i>j);}
} myobject;
int main(){
        ifstream fin("inp");
        int nt;
        string temp;
        fin>>nt;
        cout<<"sdfasdfa"<<nt;
        for(int u=0;u<nt;u++){
        int na,nb,t;
        fin>>t>>na>>nb;
        cout<<t<<" "<<na<<" "<<nb<<endl;
        vector<int> sa;
        vector<int> sb;
        vector<int> ea;
        vector<int> eb;
        for(int i=0;i<na;i++){
                fin>>temp;

                sa.push_back(convert(temp));
                fin>>temp;
                ea.push_back(convert(temp)+t);
        }
        for(int i=0;i<nb;i++){
                fin>>temp;
                sb.push_back(convert(temp));
                fin>>temp;
                eb.push_back(convert(temp)+t);
 }

        //create sa
        sort(sa.begin(),sa.end(),myobject);
        sort(eb.begin(),eb.end(),myobject);
        sort(sb.begin(),sb.end(),myobject);
        sort(ea.begin(),ea.end(),myobject);
        stack<int,vector<int> > sta(sa);
        stack<int,vector<int> > sta1(eb);
        stack<int,vector<int> > stb(sb);
        stack<int,vector<int> > stb1(ea);
        int counta=0,countb=0;

        while(!sta.empty()){
                if(sta1.empty()){
                        sta.pop();
                        counta++;
                }
                else{
                if(sta.top()>=sta1.top()){
                        sta.pop();
                        sta1.pop();
                }
                else{

                        counta++;
                        sta.pop();
                }}
        }

        while(!stb.empty()){
                if(stb1.empty()){
                        stb.pop();
                        countb++;
                }
                else{
                if(stb.top()>=stb1.top()){
                        stb.pop();
                        stb1.pop();
                }
                else{
                        countb++;
                        stb.pop();
                }
                }
        }

        cout<<"Case #"<<u+1<<":"<<" "<<counta<<" "<<countb<<endl;
        }
}
