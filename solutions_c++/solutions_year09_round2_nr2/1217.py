#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)

using namespace std;
char snumber[30];
int C[10], B[10];
int N;

string format(string s)
{
    while (s.size() < 30) {
	string tmp = ""; tmp += '0';
	tmp += s;
	s = tmp;
    }	
    return s;	
}

string findSuffix(int A[])
{
    string suffix = "";
    FOR(i,0,10) FOR(j,0,A[i]) suffix += char('0'+i);
    sort(suffix.begin(), suffix.end());
    return suffix;
}


int main()
{
	int T;
	scanf("%d",&T);
	FOR(t,0,T)
	{
	   scanf("%s", snumber);	   
	   string number  = snumber;
	   N = strlen(snumber);

	   memset(C,0,sizeof(C));
	   FOR(i,0,N) C[number[i]-'0']++;
	   string ans = "";   
	
	    for(int preffix = 0; preffix < N-1; ++preffix)
		 for(int digit=number[preffix]-'0'+1; digit<10; ++digit){
			memcpy(B,C,sizeof(C));
			for(int j=0; j<preffix; ++j) --B[number[j]-'0'];
			if (B[digit] <= 0) continue;
			--B[digit];
			string ins = number.substr(0, preffix);
			ins += char('0' + digit);
			ins += findSuffix(B);
			ins = format(ins);
			if (ans == "") ans = ins;
			else ans = min(ans, ins);
	   }	
	   //printf("Resp without zero %s\n",ans.c_str());	
	
	   string withZero = "";
	   FOR(i,1,10) if (C[i] > 0)
	   {		
		--C[i];
		withZero += char('0' + i);
		break;
	   }
	  
	  withZero += '0';
	  withZero += findSuffix(C);
	  withZero = format(withZero);
	  if (ans == "")  ans = withZero;	
	  else ans = min(ans, withZero);
	  while (ans[0] == '0') ans = ans.substr(1);
          printf("Case #%d: %s\n",1+t,ans.c_str());

	}

	return 0;
}
