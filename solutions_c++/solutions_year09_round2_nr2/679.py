#include <iostream>
#include <map>

using namespace std;

string nextN( string s, int level ) {
    if( s.size()==1 ) {
        if(level==0) return s+"0";
        else return s;
    }
    //fix the first char in substring
    //recurse over remainder
    string rem=nextN( s.substr(1), level+1 );
    if( rem==s.substr(1) ) { //already descending so go back up a level
        if( s[0]>=rem[0] ) {  //current letter doesn't help either so go up
            if(level==0) { //we're at the start, entire string is descreasing
                int nonz=-1;
                sort(s.begin(),s.end());
                for( int i=0; i<s.size(); i++ )
                    if(s[i]!='0') { nonz=i; break; }
                swap(s[nonz],s[0]);
                s.insert(1,"0"); //insert extra 0
                return s;
            }
            return s;
        }
        else { //reorder and place next highest
            int cur=-1;
            for( int i=1; i<s.size(); i++ )
                if( s[i]>s[0] && (cur==-1||s[cur]>s[i]) ) cur=i;
            if(cur==-1) cout << "WTF" << endl;
            swap(s[0],s[cur]);
            //sort second portion
            sort(s.begin()+1,s.end());
            return s;
        }
    }

    return string(1,s[0])+rem;
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int N;
    cin >> N;

    for( int test=1; test<=N; test++ ) {
        string num;
        cin >> num;
        cout << "Case #" << test << ": " << nextN(num,0) << endl;
    }
    return 0;
}
