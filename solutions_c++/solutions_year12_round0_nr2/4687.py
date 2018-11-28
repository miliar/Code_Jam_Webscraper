#include<cstdio>
#include<iostream>
#include<queue>

using namespace std;

int main()
{
	//freopen("C:\\Users\\tkms\\Desktop\\inp.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for(int q=0;q<t;q++){
		int n,s,p;	//人数、驚くべき、基準値
		int cnt=0,sum=0;	//cntが驚くべき、sumが基準p超えてる数
		priority_queue<int,vector<int>,greater<int> >que;

		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			int in;
			scanf("%d",&in);
			que.push(in);
		}

		while(que.size()){
			int k=que.top();que.pop();//和
			int l=k/3;//3で割った最小値
			int o=l+(k-l*3);//3で割った最大値

			if(o-l==1 && o>=p){
				sum++;
				continue;
			}
			else if(o==l && l && o && o!=10){
				o+=1;l-=1;
			}
			if(o>=p+1)sum++;
			else if(o>=p && cnt<s){
				cnt++;sum++;
			}
			else if(o==l && o>=p){
				sum++;
			}
		}

		printf("Case #%d: %d\n",q+1,sum);
	}
	return 0;
}

