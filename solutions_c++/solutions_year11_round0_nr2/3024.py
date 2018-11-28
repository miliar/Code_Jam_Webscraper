#include<sstream>
#include<iostream>
#include<vector>
#include<cmath>
#include<string>
using namespace std;

vector<string> combine;
vector<string> combineTo;
vector<string> opposed;

int main(){
        freopen("B-large.in","rt",stdin);
        freopen("b.out","wt",stdout);
    int t;
    cin>>t;
    stringstream ss;
    string tmp,tmp1;
    for (int i=0; i<t ; i++){
        combine.clear();
        combineTo.clear();
        opposed.clear();
        int c,d,n;
        string st;
        cin>>c;
        for (int j=0 ;j<c ; j++){
            cin>>st;
            ss.clear();
            ss<<st[0]<<st[1];
            ss>>tmp;
            combine.push_back(tmp);
            ss.clear();
            ss<<st[2];
            ss>>tmp;
            combineTo.push_back(tmp);
        }
        cin>>d;
        for (int j=0 ;j<d ; j++){
            cin>>st;
            opposed.push_back(st);
        }
        cin>>n;
        cin>>st;
        bool cont = false;
        //string newStr=st[0]+"";
        for (int j=1 ; j<st.size() ; j++){
            cont = false;
            for (int k=0 ; k<c ; k++){
                ss.clear();
                ss<<st[j]<<st[j-1];
                ss>>tmp;
                ss.clear();
                ss<<st[j-1]<<st[j];
                ss>>tmp1;
                if (tmp == combine[k] || tmp1 == combine[k]){
                   st = st.substr(0,j-1)+ combineTo[k]+st.substr(j+1,st.size()-j-1);
                   j--;
                   cont = true;
                   break;
                   
                }
            }
            if (!cont){
                       cont = true;
               for (int k=0 ; k<d && cont ; k++){
                   for (int m=0 ; m<j ; m++){
                       ss.clear();
                        ss<<st[j]<<st[m];
                        ss>>tmp;
                        ss.clear();
                        ss<<st[m]<<st[j];
                        ss>>tmp1;
                       if (tmp == opposed[k] || tmp1 == opposed[k]){
                          st = st.substr(j+1,st.size()-j-1);
                          j=-1;
                          cont = false;
                          break;
                       }
                   }
               }
            }
        }
        cout<<"Case #"<<(i+1)<<": [";
        for (int j=0 ; j<st.size() ; j++){
            if (j)cout<<", ";
            cout<<st[j];
        }
        cout<<"]\n";
    }
    //system("pause");
    return 0;
}
