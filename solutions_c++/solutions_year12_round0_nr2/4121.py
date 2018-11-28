/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2012-04-14 10:33:49 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
	int Max[31][2];
	for(int i=0;i<31;i++){
		if(i%3==0){
			Max[i][0]=i/3;
			Max[i][1]=i/3+1;
		}
		if(i%3==1){
			Max[i][0]=i/3+1;
			Max[i][1]=i/3+1;
		}
		if(i%3==2){
			Max[i][0]=i/3+1;
			Max[i][1]=i/3+2;
		}
	}
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int n,s,p;
		int ans=0;
		vector<int> num;
		cin>>n>>s>>p;
		for(int i=0;i<n;i++){
			int temp;
			cin>>temp;
			if(temp==0){
				if(p==0){
					ans++;
				}
				n--;i--;
				continue;
			}
			if(temp==1){
				if(p<=temp){
					ans++;
				}
				n--;
				i--;
				continue;
			}
			if(temp==29 || temp==30){
				ans++;
				n--;
				i--;
				continue;
			}
			num.push_back(temp);
		}
		sort(num.begin(),num.end());
		for(int i=n-1;i>=0;i--){
	//		cout<<"free: "<<num[i]<<" "<<Max[num[i]][0]<<endl;
			if(Max[num[i]][0]>=p){
	//			cout<<"in"<<endl;
				ans++;
			}
			else
			if(Max[num[i]][1]>=p && s!=0){
				ans++;
				s--;
			}
		}/*
		for(int i=n-s;i<n;i++){
			cout<<"if: "<<num[i]<<endl;
			if(Max[num[i]][1]>=p){
				cout<<"in"<<endl;
				ans++;
			}
		}*/
		cout<<"Case #"<<t+1<<": "<<ans<<endl;

	}
}
