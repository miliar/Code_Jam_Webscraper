#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#include <stdio.h>
#include <string.h>

void inc(char* num){
	int t=1;
	while(t){
		t = 0;
		(*num)++;
		if(*num > '9'){
			*num = '0';
			t = 1;
		}
		num++;
	}
}

int getMin(int x, int len){
	int t=x;
	int min = x;
	int len10=1;
	while(--len)
		len10*=10;
	do{
		if(t%10){
			t = len10 * (t%10) + t/10;
			if(t < min)
				min = t;
		}
		else
			t = len10 * (t%10) + t/10;
	}while(t!=x);
	
	return min;
}


int getNum(int x, int len, int to, int from){
	int t=x;
	int len10 = 1;
	int ct = 0;
	//printf("%d: ",x);
	while(--len)
		len10*=10;
	do{
		if(t%10){
			t = len10 * (t%10) + t/10;
			if(t >= from && t<=to){
				//printf("%d ",t);
				ct++;
			}
		}
		else
			t = len10 * (t%10) + t/10;
	}while(t!=x);
	//puts("");
	return ct*(ct-1)/2;
}
int main(){
	std::set<int>* old;

	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	int tn;
	int t;
	scanf("%d",&tn);
	
	int tmp;
	int i;
	
	for(t=1;t<=tn;t++){
		int from, to;
		scanf("%d %d",&from,&to);
		//printf("%d - %d\n",from,to);
		tmp = from;
		int len = 0;
		int len10 = 1;
		while(tmp){
			len++;
			tmp/=10;
			len10*=10;
		}
		
		old = new std::set<int>();
		
		int ct=0;
		for(i=from;i<=to;i++){
			if(i == len10){
				len++;
				len10*=10;
				old = new std::set<int>();
			}
			
			tmp = getMin(i, len);
			if(old->find(tmp) == old->end()){
				ct += getNum(tmp,len,to,from);
				old->insert(tmp);
			}
		}
		
		printf("Case #%d: %d\n",t,ct);
	}	
	return 0;
}
