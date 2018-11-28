#include <iostream>
#include <cstring>

using namespace std;

string s[5000],temp;
int l,d,n,c=0;
bool v[100][255];


void process(string temp){
    memset(v,false, sizeof(v));
    cout << "Case #" << ++c << ": ";
    int i=0,num =0;
    while(num<l){
        while(temp[i] != '(' && num < l ) v[num++][temp[i++]] = true;
        if(temp[i] == '('){
            i++;            
            while(temp[i] !=')') v[num][temp[i++]]=true;
            i++;
            num++;                          
        }           
    }
    int res=0;
    int j;    
    for( i =0 ; i<d ; i++){
        for(j=0; j<l; j++)
            if( !v[j][s[i][j]] ) break;
        if(j==l) res ++; 
    }            
    cout << res <<endl;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d%d%d\n",&l,&d,&n);
    for(int i=0; i<d; i++) getline(cin,s[i]);
    for(int i=0; i<n; i++){
        getline(cin,temp);              
        process(temp);
    }
    return 0;
}
