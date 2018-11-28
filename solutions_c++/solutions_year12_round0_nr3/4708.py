#include<cstdio>
#include<cstdlib>
#include<string>
#include<iostream>
#include<set>

using namespace std;

string roll(int a,int i){
    char str[]="123456789";
    sprintf(str,"%d",a);
    string aa(str);
    string * tmp = new string(aa.substr(i,aa.length()-i));
    (*tmp)+=(aa.substr(0,i));
    return *tmp;
}

int recykled_numbers(int a,int b){
    int ans = 0;
    if(a>b)
        swap(a,b);
    for(int i = a ; i <= b ; ++i){
        set<int> Set;
        string aa = roll(i,0);
        for(int j = 1; j < aa.length() ; ++j){
            aa = roll(i,j);
            if(aa[0]!='0'){
                int x;
                sscanf((char *)aa.c_str(),"%d",&x);
                if(x <= b && x > i){
                    Set.insert(x);
                   // cout<<"x= "<<x<<endl;
                }
            }
        }
        ans+=Set.size();
    }
    return ans;
}

int main(){
  //  for(int i = 0 ; i < 5 ; ++i){
  //      cout<<roll(12345,i)<<endl;
  //  }
    int t;
    cin>>t;
    for(int i = 0 ; i < t ; ++i){
        int a,b;
        cin>>a>>b;
        cout<<"Case #"<<i+1<<": "<<recykled_numbers(a,b)<<endl;
    }
}
