#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#define test(a,bit)  (a>>bit&1)!=0
#define set(a,bit) (a|=1<<bit)
//#define clear(a,bit) (a&=~(1<<bit))
#define negation(a) (ALL_BITS^a)
#define subs(a,b) (a~b)

using namespace std;

#define MAXD 5000
#define MAXL 16

int tdic;
string dic[MAXD];
vector <int> dir;
bool inicio;

bool checa (int pos, int letras){

    if (inicio) {
    	
        for (int i=0; i<tdic;i++){
        	//printf("*%d %d %d \n",letras, dic[i][pos]-'a', test(letras,dic[i][pos]-'a'));
            if (test(letras,dic[i][pos]-'a')) dir.push_back(i);
        }
        inicio=false;
    }else {
    	vector <int> dir2;
        for (int i=0; i<dir.size(); i++){
            if (test(letras, dic[ dir[i] ][pos]-'a')) dir2.push_back( dir[i] );
        }
        dir=dir2;
    }
}

int main() {
    int l,n;
    string s;

    scanf("%d %d %d\n",&l, &tdic, &n);
    for (int i=0; i<tdic; i++){
        cin>>s;
        dic[i]=s;
    }
    for (int i=0; i<n; i++){
        cin>>s;
        
        inicio=true;
		dir.clear();
		
        for (int j=0,p=0; j<s.length(); j++){
        	int letras=0;
            if (s[j]=='(') {

                int k;
                for (  k=j+1; s[k]!=')'; k++) {
                	set(letras, s[k]-'a');
                }
                
                j=k;
                checa(p++,letras);
            }else {
            	set(letras, s[j]-'a');
            	
            	checa(p++, letras);
            	//cout<<s[j]<<" "<<letras<<"<-"<<s[j]-'a'<<" "<<dir.size()<<endl;
            }
        }
      //  cout<<s<<endl;
        printf("Case #%d: %d\n",i+1, dir.size());
    }
    return 0;
}
