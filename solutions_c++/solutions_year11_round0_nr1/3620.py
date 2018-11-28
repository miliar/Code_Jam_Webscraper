#include <iostream>
using namespace std;

int curTime,orangeCurPos,orangeLastActiveTime,blueCurPos,blueLastActiveTime;

void handle(char c,int pos)
{
	int costTime ;
	int iTmp;

	if(c=='O'){
		costTime = (pos>orangeCurPos) ? (pos-orangeCurPos) : (orangeCurPos-pos);
		costTime++;
		iTmp = (costTime+orangeLastActiveTime);

		if( curTime < iTmp ){
			curTime = iTmp ;
		}else
			curTime = curTime + 1;


		orangeLastActiveTime = curTime;
		orangeCurPos = pos;

	}else{
		costTime = (pos>blueCurPos) ? (pos-blueCurPos) : (blueCurPos-pos);
		costTime++;

		iTmp = (costTime+blueLastActiveTime);

		if( curTime < iTmp ){
			curTime = iTmp ;
		}else
			curTime = curTime + 1;

		blueLastActiveTime = curTime;
		blueCurPos = pos;
	}

	//cout << c << " " << pos  << " curTime:" << curTime << endl;
}

int main()
{

	freopen("A-large.in","r",stdin);	freopen("A-large.out","w",stdout);

	int n,m,t;

	char  c;

	while(cin>>n){
		for(int i=1;i<=n;i++){
			curTime = 0;
			orangeCurPos = 1;
			blueCurPos = 1;

			orangeLastActiveTime = 0;
			blueLastActiveTime = 0;
			cin>> m;
			scanf("%d",&m);
			for(int j=0;j<m;j++){
				cin>> c >> t;
				

				handle(c,t);
			}
			printf("Case #%d: %d\n",i,curTime);
		}
	}

	return 0;
}