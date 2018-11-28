#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

    bool used[2000002];
    int TESTN = 1;
    
void solve () {
    
    memset ( used, 0, sizeof(used) );
    
    int a, b, bam;
    
    scanf("%d%d", &a, &b);

    long long ans = 0;
    
    for ( int i = a; i <= b; ++i )  {

        if ( used[i] ) continue;
        
        char num[30] = {0};
        
        int tempAns = 0;
        
        sprintf( num, "%d", i );
        
        string s = string(num);
        
        //cout<<"got "<<s<<"\n";
        
        for ( int j = 0; j < (int)s.size(); ++j ) {
        
            string temp = s.substr(j);
            temp += s.substr(0,j);
            
            if ( temp[0] == '0' ) continue;
            
            sscanf(temp.c_str(), "%d", &bam);
            
            
            if ( bam >= a && bam <= b && !used[bam] ) {
            
                //cout<<" pass temp "<<temp<<"\n";
               // cout<<" got num "<<bam<<endl;
                
                used[bam]=1;
                tempAns++;
            }
        }
        
        ans += (tempAns * tempAns - tempAns) / 2;
    }
    
    printf("Case #%d: %lld\n",TESTN, ans);
    TESTN++;
}

int main () {

    int t;
    scanf("%d", &t);

    for ( int i = 0; i < t; ++i ) solve();

    return 0;
}
