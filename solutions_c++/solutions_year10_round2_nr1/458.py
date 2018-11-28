#include <iostream>
#include <map>
#include <string>

#define TASK "A"
#define SMALL "small-attempt" 
#define NUM "0"
#define LARGE "large"

using namespace std;

int test;
int numtest;
int n,m;
map<string,int> H;
int all;
int ans;
string s;

#define N 1001



void readinput(){
    all=0;
    H.clear();
    scanf("%i %i\n",&n,&m);
    for (int i=0;i<n;i++){
        cin>>s;
        s+='/';
        for (int j=0;j<s.size();j++){
            if (j && s[j]=='/'){
                string dir = s.substr(0,j);
                //cout<<dir<<endl;
                if (H.find(dir)==H.end()){
                    all++;
                    H[dir]=all;
                }    
            }    
        }    
    }
	ans=0;   
    for (int i=0;i<m;i++){
        cin>>s;
        s+='/';
        for (int j=0;j<s.size();j++){
            if (j && s[j]=='/'){
                string dir = s.substr(0,j);
                //cout<<dir<<endl;
                if (H.find(dir)==H.end()){
                    all++;
                    ans++;
                    H[dir]=all;
                }    
            }    
        }    
    }
}

void writeoutput(){
	printf("Case #%i: ",numtest);
    printf("%i\n",ans);
	
}

void solve(){

}

int main(void){
	//freopen(TASK"-"SMALL""NUM".in","r",stdin);
	//freopen(TASK"-"SMALL""NUM".out","w",stdout);
	freopen(TASK"-"LARGE".in","r",stdin);
	freopen(TASK"-"LARGE".out","w",stdout);
	scanf("%i\n",&test);
	for (int q=0;q<test;q++){
        numtest=q+1;
		readinput();
		solve();
		writeoutput();
	}

	return 0;
}
