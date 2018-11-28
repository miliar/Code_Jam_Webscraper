#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int com[30][30];
map<char, char> op;
int c,d,n;
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		scanf("%d",&c);
		for(int i=0;i<30;i++){
			for(int j=0;j<30;j++){
				com[i][j] = -1;
			}
		}
		op.clear();
		for(int i=0;i<c;i++){
			char buff[10];
			scanf("%s",buff);
			com[buff[0]-'A'][buff[1]-'A']=buff[2];
			com[buff[1]-'A'][buff[0]-'A']=buff[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++){
			char buff[10];
			scanf("%s",buff);
			op[buff[0]] = buff[1];
			op[buff[1]] = buff[0];
		}
		scanf("%d",&n);
		char buf[1024];
		scanf("%s",buf);
		bool remove=false;
		int rem;

		string print;
		print="";
		for(int i=0;i<n;i++){
			char temp=buf[i];
			bool flag = false;
			if(i>0){
				char pre;
				if( print.length()>0)
					pre= print[print.length()-1];
				if(print.length() > 0 && com[pre-'A'][temp-'A']!= -1){
					if(remove && rem == print.length()-1)
						remove = false;
					print = print.substr(0,print.length()-1);
					print += (char)com[pre-'A'][temp-'A'];
					flag = true;
				}
				else if(print.length() > 0 && com[temp-'A'][pre-'A'] != -1){
					if(remove && rem == print.length()-1 )
						remove = false;
					print = print.substr(0,print.length()-1);
					print += (char)com[temp-'A'][pre-'A'];
				
					flag = true;
				}
				else
					print+=temp;
			}
			else
				print+=temp;
			if(!flag){
				if(!remove){
					if(op.find(temp) != op.end()){
						rem = print.length()-1;
						remove = true;
					}
				}
				else{
					if( op[print[rem]] == temp){
						print = "";
						remove = false;
					}
				}
			}
		}
		
		printf("Case #%d: [",te+1);
		for(int i=0;i<print.length();i++){
			if( i > 0 )
				printf(", ");
			printf("%c",print[i]);
		}
		printf("]\n");
	}
	return 0;
}