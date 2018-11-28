#include<iostream>
#include<stdio.h>
using namespace std;
//vector<int> arr;
//vector<int>::iterator it;
int main()
{
	int i,k;
	int sum,cnt;
	int T;
	int N,S,P;
	scanf("%d",&T);
	for(k=1;k<=T;k++){
			cnt=0;
			scanf("%d %d %d",&N,&S,&P);
			//cout<<N<<S<<P<<endl;
			for(i=0;i<N;i++){
				scanf("%d",&sum);
				//cout<<N<<"kjgkj"<<endl;
					if (sum==0){
						if (P==0)
						cnt++;
					}
					else if (sum/3 >=P)
						cnt++;
					else if (sum%3==0){
						if (sum/3 == P-1){
							if (S){cnt++;S--;}
						}
					}
					else if (sum%3==1){
						if (sum/3 == P-1)
							cnt++;
					}
					else if (sum/3 == P-2){
						if (S){cnt++;S--;}
					}
					else if (sum/3 == P-1)
						cnt++;
			}
			printf("Case #%d: %d\n",k,cnt); 		
	}

}
