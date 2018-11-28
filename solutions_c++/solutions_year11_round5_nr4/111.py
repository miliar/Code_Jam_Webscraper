#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

long long N;

bool isSquare(long long val){
	long long ini = 1, fim = val, med;
	
	if(!val)return true;
	
	while(ini != fim){
		med = (ini+fim)/2;
		
		if(med < (val+med-1)/med)
			ini = med+1;
		else
			fim = med;
	}
	return ini*ini == val;
}

bool go(char *str, long long val){
	
	if(*str == 0){
		if(isSquare(val)){
			N = val;
			return true;
		}else{
			return false;
		}
	}else{
		if(*str == '0' || *str == '?')
			if(go(str+1, val*2)){
				*str = '0';
				return true;
			}
		if(*str == '1' || *str == '?')
			if(go(str+1, val*2 + 1)){
				*str = '1';
				return true;
			}
			return false;
	}
}

char str[100];
int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	
	for(int i = 1; i <= casos; i++){
		scanf("%s", str);
		
		go(str,0);
		
		cout << "Case #" << i << ": " << string(str) << endl;
	}
	
	return 0;
}