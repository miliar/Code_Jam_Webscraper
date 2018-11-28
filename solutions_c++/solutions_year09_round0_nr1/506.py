#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;

string dict[5000];

main(){

    int l,d,n;
    scanf("%d %d %d",&l,&d,&n);

    for(int i=0;i<d;i++){
	cin>>dict[i];
    }

    for(int test=1;test<=n;test++){

	bool ok[l][26];
	for(int i=0;i<l;i++)
	    for(int j=0;j<26;j++)
		ok[i][j]=0;

	string s;
	cin>>s;

	int sindex=0;
	int lindex=0;

	while(sindex<s.length()){

	    if(s[sindex]=='('){

		sindex++;
		while(s[sindex]!=')'){
		    ok[lindex][s[sindex]-'a']=1;
		    sindex++;
		}
		sindex++;
	    }
	    else{
		ok[lindex][s[sindex]-'a']=1;
		sindex++;
	    }

	    lindex++;
	}

	int ct=0;
	for(int i=0;i<d;i++){ // check if dict[i] matches with s

	    bool f=1;

	    for(int j=0;j<l;j++)
		if(!ok[j][dict[i][j]-'a']){
		    f=0;
		    break;
		}

	    if(f) ct++;
	}

	printf("Case #%d: %d\n", test, ct);

    }
}
