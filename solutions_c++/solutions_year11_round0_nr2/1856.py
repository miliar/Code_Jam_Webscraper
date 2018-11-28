#include<iostream>
#include<iterator>
#include<string>
#include<vector>
#include<map>
#include<set>

using namespace std;

int main(){
    int cases;
    cin>>cases;
    for(int cas=1;cas<=cases;cas++){
        map<string,char> combine;
        set<string> opposed;

        int c,o;
        cin>>c;
        for(int i=0;i<c;i++){
            string co;
            cin>>co;
            char str[3]={};
            str[0]=co[0];
            str[1]=co[1];
            combine[str]=co[2];
            std::swap(str[0],str[1]);
            combine[str]=co[2];
        }
        cin>>o;
        for(int i=0;i<o;i++){
            string op;
            cin>>op;
            opposed.insert(op);
            swap(op[0],op[1]);
            opposed.insert(op);
        }
        int len;
        cin>>len;
        string str;
        cin>>str;

        vector<char> stack;

        for(int i=0;i<len;i++){
            stack.push_back(str[i]);
            while(stack.size()>=2){
                int s = stack.size();
                string b;
                b.push_back(stack[s-2]);
                b.push_back(stack[s-1]);
                if(combine.count(b)){
                    stack.pop_back();
                    stack.pop_back();
                    stack.push_back(combine[b]);
                    //cout<<"combine "<<b<<" -> "<<combine[b]<<"\n";
                }else{
                    break;
                }
            }
            string opp="##";
            if(stack.size()>=2){
                string b;
                int s = stack.size();
                opp[1] = stack[s-1];
                bool clear = false;
                for(int j=0;j<stack.size()-1;j++){
                    opp[0]=stack[j];
                    if(opposed.count(opp)){
                        clear=true;
                        break;
                    }
                }
                if(clear){
                    //cout<<"clear\n";
                    stack.clear();
                }
            }
        }
        cout<<"Case #"<<cas<<": [";
        if(stack.size()){
            copy(stack.begin(),stack.end()-1,ostream_iterator<char>(cout,", "));
            cout<<stack.back();
        }
        cout<<"]\n";
    }
}
