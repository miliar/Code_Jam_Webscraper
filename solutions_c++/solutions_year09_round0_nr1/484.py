/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;
int automata[20][26];
char input[1000];
int d,n,q;
char dic[5010][20];

int main()
{
	int i;

	cin >> d >> n >> q;

	for(i=0;i<n;i++){
		cin >> dic[i];
	}
	
	int kase;
	int j;
	bool graph[20][26];
	for(kase=1;kase<=q;kase++){
		cin >> input;
		int len = strlen(input);

		bool flag=false;
		int j =0;
		memset(graph,false,sizeof graph);
		for(i=0;i<len;i++){
			if(input[i] =='(')
				flag=true;
			else if(input[i] ==')')
				flag=false,j++;
			else if(flag)
				graph[j][input[i]-'a'] = true;
			else{
				graph[j][ input[i]-'a'] = true;	
				j++;
			}
		}

		int cnt = 0;
		for(i=0;i<n;i++){
			flag=true;
			for(j=0; j<d && flag;j++){
				if(!graph[j][dic[i][j]-'a']){
					flag=false;
				}
			}

			if(flag)
				cnt++;
				
		}

		cout << "Case #"<<kase <<": " << cnt <<endl;
	}
	return 0;
}