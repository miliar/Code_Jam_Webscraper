#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>

using namespace std;

int abs(int n){
	return n<0?-n:n;
}
int sgn(int n){
	return n<0?-1:(n>0?1:0);
}
int main(){
	int T;
	scanf("%d\n",&T);
	for(int Case=0;Case<T;Case++){
		int N;
		scanf("%d ",&N);
		vector< pair<char,int> >pushes;
		vector<int>O,B;
		for(int push=0;push<N;push++){
			char ch;
			int bnum;
			scanf("%c %d ",&ch,&bnum);
			pushes.push_back(pair<char,int>(ch,bnum));
			if(ch=='B')B.push_back(bnum);
			else O.push_back(bnum);
		}
		long long time=0;
		int Opos=1,Bpos=1;
		while(!pushes.empty()){
			pair<char,int>curr=pushes[0];
			int*cpos,*opos;
			vector<int>*cstk,*ostk;
			if(curr.first=='B'){
				cpos=&Bpos;
				opos=&Opos;
				cstk=&B;
				ostk=&O;
			}
			else{
				cpos=&Opos;
				opos=&Bpos;
				cstk=&O;
				ostk=&B;
			}
			
			int tdif=abs(curr.second-*cpos)+1;
			if(!(*ostk).empty()){
				if(tdif>=abs((*ostk)[0]-*opos))
					*opos=(*ostk)[0];
				else
					*opos+=sgn((*ostk)[0]-*opos)*tdif;
			}
			*cpos=curr.second;
			time+=tdif;
			
			pushes.erase(pushes.begin());
			(*cstk).erase((*cstk).begin());
		}
		printf("Case #%d: %lld\n",Case+1,time);
	}
	return 0;
}