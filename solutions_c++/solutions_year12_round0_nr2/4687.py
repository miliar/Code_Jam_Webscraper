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
		int n,s,p;	//�l���A�����ׂ��A��l
		int cnt=0,sum=0;	//cnt�������ׂ��Asum���p�����Ă鐔
		priority_queue<int,vector<int>,greater<int> >que;

		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			int in;
			scanf("%d",&in);
			que.push(in);
		}

		while(que.size()){
			int k=que.top();que.pop();//�a
			int l=k/3;//3�Ŋ������ŏ��l
			int o=l+(k-l*3);//3�Ŋ������ő�l

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

