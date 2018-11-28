#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<utility>
#include <map>
#include<string>
using namespace std;
char next_value[8];
vector<pair<string,string> > myvectorpair;
int count = 0;

void printing(){
	//vector< pair<char *,char *> > ::iterator search_it;
	//cout<<"Inside printing()\n";
	for(int i = 0; i<count; i++){
		cout<<"In List "<<myvectorpair[i].first<<" "<<myvectorpair[i].second<<endl<<flush;
	}
	//cout<<"End of printing()\n";
}
int all_same(char *s){
	int len = strlen(s);
	char c = s[0];
	int i = 0;
	for(i = 1; i<len && c== s[i]; i++);
	if(i == len) return(1);
	else return(0);
}

int with_in_range(char c[8], char it[8], char ra[8]){
	char current[8],initial[8],range[8];
	int len;
	int flag1 = 0,flag2 = 0;
	//vector< pair<char *,char *> > ::iterator  it;
	strcpy(current,c);
	strcpy(initial,it);
	strcpy(range,ra);
	len = strlen(current);
	if(current[0]== '0') return 0;
	if(strcmp(current,initial)==0) return 0;
	for(int i = 0; i<len && (flag1+flag2 !=2) ; i++){
		if(flag1 == 0){
			if(current[i]>range[i])
				return(0);
			else if(current[i]<range[i])
				flag1= 1;
		}
		if(flag2 == 0){
			if(current[i]>initial[i])
				flag2 = 1;
			else if(current[i]<initial[i])
				return(0);
		}
	}
	//cout<<"before inserting "<<initial<<" "<<current<<endl<<flush;
	for(int i = 0; i<count; i++){
		if((myvectorpair[i].first == initial && myvectorpair[i].second == current)||
			(myvectorpair[i].first == current && myvectorpair[i].second == initial)){
				return(0);
		}
	}
	pair <string, string > mypair;
	mypair = make_pair(initial,current);
	myvectorpair.push_back(mypair);
	count++;
	//cout<<"after inserting "<<initial<<" "<<current<<endl<<flush;
	//cout<<"calling printing in with_in_range\n";
	//printing();
	return(1);
}
	
void next_number(char s[8]){
	char output[8];
	int len = 0, flag = 0;
	strcpy(output,s);
	len = strlen(s);
	for(int i = len-1; i>=0 && flag == 0; i--){
			switch(output[i]){
			case '9': output[i] = '0'; break; 
			case '0': output[i] = '1'; flag = 1; break;
			case '1': output[i] = '2'; flag = 1; break;
			case '2': output[i] = '3'; flag = 1; break;
			case '3': output[i] = '4'; flag = 1; break;
			case '4': output[i] = '5'; flag = 1; break;
			case '5': output[i] = '6'; flag = 1; break;
			case '6': output[i] = '7'; flag = 1; break;
			case '7': output[i] = '8'; flag = 1; break;
			case '8': output[i] = '9'; flag = 1; break;

		}
		
	}
	strcpy(next_value,output);
}
	


	
int main(){
	int test = 0;
	char A[8], B[8], num[8], num2[8], temp[8];
	int len = 0, equal_count = 0;
	multimap<char *,char *>::iterator search_it;
	scanf("%d\n",&test);
	for(int x = 1; x <= test; x++){
		count = 0,equal_count = 0;
		scanf("%s %s\n",A,B);
		len = strlen(A);
		if(len==1){
			printf("Case #%d: 0\n",x);
		}
		else{
			strcpy(num, A);
			count = 0,equal_count = 0;
			while(strcmp(num,B)!=0){
				if(all_same(num) == 1){
					equal_count++;
				}
				else{

					strcpy(num2,num);
					strcpy(temp,num2);
					for(int i = 1; i<len; i++){
						strcpy(temp,num2);
						for(int j = len-1; j>=1; j--){
							num2[j] = num2[j-1];
						}
						num2[0] = temp[len-1];
						if(with_in_range(num2, num, B)==1){
							//cout<<"Count increased "<<num<<" "<<temp<<" "<<num2<<endl<<flush;
							//count++;
						}
					}
					
				}
				next_number(num);
				strcpy(num, next_value);
				//printf("Calling printing in main function\n");
				//printing();
			}
			printf("Case #%d: %d\n",x,count);
			myvectorpair.clear();
		}
		

	}
	
	return(0);
}

