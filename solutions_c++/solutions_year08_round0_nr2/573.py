#include<iostream>
#include<deque>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;
struct DATA{
	int hour ;
	int minute;
	int st_sum,ed_sum;
};
DATA data[300];
struct TRAIN{
	int st_time;
	bool operator <(const TRAIN &a)const{
		return a.st_time < st_time;
	}
};
TRAIN now;
priority_queue<TRAIN>A,B,empty;
string str1  , str2;

bool cmp(DATA a ,DATA b){
	return a.st_sum < b.st_sum;
}
int main(){
	int test;
	int Case = 0;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("ans1.out","w",stdout);
	scanf("%d",&test);
	while(test--){
		Case++;
		int time;
		scanf("%d",&time);
		int num_A , num_B;
		scanf("%d%d",&num_A,&num_B);
		int i ,j;
		A = empty;
		B = empty;
		for(i = 0 ; i < num_A ; i++){
			cin>>str1>>str2;
			data[i].hour = 0;
			data[i].minute = 0;
			for(j = 0 ; j < str1.length(); j++){
				if(str1[j]==':'){
					break;
				}
				data[i].hour *=10;
				data[i].hour+=str1[j]-'0';
			}
			data[i].hour*=60;
			for(j = j+1 ; j < str1.length(); j++){
				data[i].minute *=10;
				data[i].minute+=str1[j]-'0';
			}
			data[i].st_sum = data[i].hour+data[i].minute;
			///////////////////////////////////////
			data[i].hour = 0;
			data[i].minute = 0;
			for(j = 0 ; j < str2.length(); j++){
				if(str1[j]==':'){
					break;
				}
				data[i].hour *=10;
				data[i].hour+=str2[j]-'0';
			}
			data[i].hour*=60;
			for(j = j+1 ; j < str2.length(); j++){
				data[i].minute *=10;
				data[i].minute+=str2[j]-'0';
			}
			data[i].ed_sum = data[i].hour+data[i].minute;
			now.st_time = data[i].ed_sum + time;
			B.push(now);

		}
		for( ; i < num_B + num_A; i++){
			cin>>str1>>str2;
			data[i].hour = 0;
			data[i].minute = 0;
			for(j = 0 ; j < str1.length(); j++){
				if(str1[j]==':'){
					break;
				}
				data[i].hour *=10;
				data[i].hour+=str1[j]-'0';
			}
			data[i].hour*=60;
			for(j = j+1 ; j < str1.length(); j++){
				data[i].minute *=10;
				data[i].minute+=str1[j]-'0';
			}
			data[i].st_sum = data[i].hour+data[i].minute;
			///////////////////////////////////////
			data[i].hour = 0;
			data[i].minute = 0;
			for(j = 0 ; j < str2.length(); j++){
				if(str1[j]==':'){
					break;
				}
				data[i].hour *=10;
				data[i].hour+=str2[j]-'0';
			}
			data[i].hour*=60;
			for(j = j+1 ; j < str2.length(); j++){
				data[i].minute *=10;
				data[i].minute+=str2[j]-'0';
			}
			data[i].ed_sum = data[i].hour+data[i].minute;
			now.st_time = data[i].ed_sum + time;
			A.push(now);
		}
		sort(data , data+num_A , cmp);
		sort(&data[num_A],&data[num_A+num_B],cmp);
		int count1 = 0 , count2 = 0;
		for(i = 0 ; i < num_A;i++){
			if(!A.empty()&&A.top().st_time <= data[i].st_sum){
				A.pop();
			}
			else{
				count1++;
			}
		}	
		for( ; i < num_B + num_A ; i++){
			if(!B.empty()&&B.top().st_time <= data[i].st_sum){
				B.pop();
			}
			else{
				count2++;
			}
		}

		printf("Case #%d: %d %d\n" , Case , count1 , count2);
	}
	return 0;
}
