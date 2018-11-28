#include <cstdio>
#include <cstring>
using namespace std;

int l,d,n,ans,len,now;
char s[100000][20],ss[100000],bl[10];

int main() {
    int C=0;
    scanf("%d%d%d",&l,&d,&n);
    gets(bl);
    for (int i=1;i<=d;i++) gets(s[i]);
    for (int i=1;i<=n;i++) {
        gets(ss);
        len=strlen(ss);
        ans=0;
        for (int kk=1;kk<=d;kk++) {
        	now=0;
        	bool ok=true;
        	for (int j=0;j<l;j++) {
            	if (ss[now]=='(') {
	            	bool check=false;
                	now++;
                	while (ss[now]!=')') {
                    	if (ss[now]==s[kk][j]) check=true;
                    	now++;
                	}    
                	if (!check) {
                    	ok=false;
                    	break;
                	}    
            	} else {
            	    if (ss[now]!=s[kk][j]) {
            	        ok=false;
            	        break;
            	    }    
            	}    
            	now++;
            }        
            if (now!=len) ok=false;
            if (ok) ans++;
        }     
        printf("Case #%d: %d\n",++C,ans);
    }    
}        
