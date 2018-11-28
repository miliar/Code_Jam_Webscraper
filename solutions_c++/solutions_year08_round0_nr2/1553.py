#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)

typedef pair<int,int> PII;
int convert(char *str){
	int res = ((str[0]-'0')*10+str[1]-'0')*60+((str[3]-'0')*10+str[4]-'0');
	return res;
}
int solve(vector<PII> &tab){
	int res = 0;
	int ile_poc = 0;
	REP(i,tab.size()){
		if( tab[i].second == 0 )ile_poc++;
		else{
			if( ile_poc > 0 )ile_poc--;
			else res++;
		}
	}
	return res;
}
char str1[20],str2[20];
vector<PII> A,B;
int main(){
	int d;
	scanf("%d",&d);
	REP(test,d){
		A.clear();B.clear();
		int na,nb,t;
		scanf("%d %d %d",&t,&na,&nb);		
		REP(i,na){
			scanf("%s %s",str1,str2);
			A.push_back(make_pair(convert(str1),1));
			B.push_back(make_pair(convert(str2)+t,0));
		}
		REP(i,nb){
			scanf("%s %s",str1,str2);
			B.push_back(make_pair(convert(str1),1));
			A.push_back(make_pair(convert(str2)+t,0));
		}
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		//REP(i,A.size())printf("%d %d\n",A[i].first,A[i].second);

		int res_a = solve(A);
		int res_b = solve(B);		

		printf("Case #%d: %d %d\n",test+1,res_a,res_b);
	}

	return 0;
}
