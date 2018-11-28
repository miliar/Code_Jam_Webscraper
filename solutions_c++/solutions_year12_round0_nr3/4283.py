#include<iostream>
#include<vector>
#include<fstream>
#include<map>
#include<sstream>
#include<string>
#include<set>
#include<algorithm>
using namespace std;
#define REP(i,n) for(int i =0;i<n;i++)
#define FOR(i,a,b) for(int i =a;i<=b;i++)
int numDigits(int n){
    int cnt = 0 ;
    while(n>0){
        ++cnt;
        n /= 10;
    }
    return cnt;
}
bool areAllDigitsSame(int num){
    bool ans = true;
    int prev = num%10;  
    num /= 10;
    while(num > 0){
        if(prev != num%10)
            return false;
        prev = num%10;
        num /= 10;
    }
    return true;
}
struct comp{
  bool operator()(const pair<int,int> p1, const pair<int, int> p2){
        return p1.first < p2.first;
  }
};
string intToStr(int n){
    stringstream ss;
    ss<<n;
    return ss.str();
}
int strToInt(string s){
    int ans;
    stringstream ss;
    ss<<s;
    ss>>ans;
    return ans;
}
int main(){
    int kase, T, ans = 0;
    string s, temp;
    cin>>T;
    for(int kase = 1;kase <= T;kase++){
        int A,B;
        int perm;
        cin>>A>>B;
        set<pair<int, int>, comp > st;
        stringstream ss;
        FOR(i,A,B){
            if(areAllDigitsSame(i))
                continue;
            int ndigits = numDigits(i);
            s = intToStr(i);
            //cout<<"s: " <<s<<endl;
            REP(j,ndigits){
                REP(k, ndigits-1){
                    temp = s.substr(k+1) + s.substr(0,k+1);
                    perm = strToInt(temp);
                    set<pair<int,int> , comp >::iterator itt, itt1, itt2;
                    if((perm <=B) && (perm >= A)  && (i != perm) ){
                        itt1 = st.find(make_pair(i,perm));
                        itt2 = st.find(make_pair(perm,i));
                        if(!((itt1->first == i) &&(itt1->second == perm) ) && !((itt2->first == perm) &&(itt2->second == i) )){
                            //cout<<"putting into map" <<i<< " "<<perm<<endl;
                            st.insert(make_pair(i,perm));
                        }
                    }
                }
            }
        }
        //cout<<endl;
        set<pair<int, int>,comp >::iterator it, it1;
        
        set<pair<int, int>,comp > copy(st); 
/* 
        for(it = copy.begin(); it != copy.end(); it++)
            cout<<it->first<<" " <<it->second<<endl;
        cout<<endl;
        */
        ans = copy.size();
        cout<< "Case #"<<kase<<": " <<ans<<endl;
    }
    return 0;
}
