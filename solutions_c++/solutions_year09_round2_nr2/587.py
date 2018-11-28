#include <fstream>
#include <string>
#include <iostream>
using namespace std;

ifstream fin("p1in2.txt");
ofstream fou("p1out2.txt");

int d[10];


bool ifmax( string s )
{
	int tmp[10];
    for (int i=0; i<=9; i++) tmp[i]=d[i];

    for (int i=0; i<s.length(); i++){
        for (int k=9; k>=0; k--){
            if (tmp[k]>0){
                if (s[i]!='0'+k) return false;
                tmp[k]--;
            	break;
            }
        }
    }
    return true;
}


void changelow( string& N, int idx )
{
	for (int i=idx; i<N.length(); i++){
        for( int k=0; k<=9; k++){
        	if (d[k]>0){
                N[i]='0'+k;
                d[k]--;
            	break;
            }
        }
    }
}


string work( string N )
{
    memset( d , 0 , sizeof(d) );
    for (int i=0; i<N.length(); i++){
    	d[N[i]-'0']++;
    }

	for (int i=0; i<N.length() ; i++){
        d[N[i]-'0']--;
    	if (ifmax( N.substr(i+1) )){
        	d[N[i]-'0']++;
            for (int k=N[i]-'0'+1; k<=9; k++){
                if (d[k]>0){
                    N[i]='0'+k;
                    d[k]--;
                    changelow( N , i+1 );
                    return N;
                }
            }
        }
    }

}


int main()
{
    int T;
    fin >> T;
    for (int i=1; i<=T; i++){
    	string N;
        fin >> N;
        N='0'+N;
        cout << N;
        
        string ans = work(N);
        if (ans[0]=='0') ans = ans.substr(1);
		fou << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
