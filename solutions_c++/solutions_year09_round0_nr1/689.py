#include <iostream>
#include <string>

using namespace std; 

int main() {
    string dic[5100] ; 
    int l,d,n,i; 
    string instr;
    int table[20][26] ; 


    cin >> l >> d >> n  ;
    getline(cin,instr);
    for(i=0;i<d; i++) {
        getline(cin,dic[i]);
    }

    for(i=0;i<n;i++) {
        int sum =0 ; 
        getline(cin,instr);
        int j,k; 
        for(j=0;j<l;j++) {
            for(k=0;k<26;k++) {
                table[j][k] = 0 ;
            }
        }

        int idx = 0 ;
        bool opena = false ; 

        for(j=0;j<instr.length();j++) {
            if ( instr[j]==')' ) { idx++; opena = false ; continue; }
            else if ( instr[j]>='a' && instr[j]<='z') {
                table[idx][instr[j]-'a'] = 1 ;
                if (!opena) idx++;
            } else if ( instr[j]=='(') {
                opena = true; 
            }
        }

        for(j=0;j<d;j++) {
            sum++;
            for(k=0;k<l;k++) {
                if(table[k][dic[j][k]-'a']==0 ){
                    sum--;
                    break; 
                }
            }
        }

        cout << "Case #" << i+1 << ": " ; 
        cout << sum << endl ; 
    }
    cout.flush();

    return 0 ;
}
