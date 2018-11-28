//B. Magicka
//GCJ 2011 Qual.

#include <cstdio>
#include <list>
#include <algorithm>
#include <cstdlib>

using namespace std;

char str[5];

int m(char x){
	if(x=='Q') return 0;
	if(x=='W') return 1;
	if(x=='E') return 2;
	if(x=='R') return 3;
	if(x=='A') return 4;
	if(x=='S') return 5;
	if(x=='D') return 6;
	if(x=='F') return 7;
	return 8;
}

int main(){
	int tt,t,cc,i,j,d;
	int k1,k2,n;
	char dat[10][10];
	char dat2[10][10];
	char s;

	list<char> l;
	list<char>::reverse_iterator rit;
	list<char>::iterator it;

	freopen("B-large.in","r",stdin);
	//freopen("b.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&tt);
	for(t=1;t<=tt;t++){

		scanf("%d",&cc);

		//reset
		for(i=0;i<10;i++)for(j=0;j<10;j++)dat[i][j]=0;
		for(i=0;i<10;i++)for(j=0;j<10;j++)dat2[i][j]=0;
		l.clear();

		for(i=0;i<cc;i++){//combine
			scanf("%s",str);
			dat[m(str[0])][m(str[1])] = dat[m(str[1])][m(str[0])] = str[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++){//oppose
			scanf("%s",str);
			dat2[m(str[0])][m(str[1])] = dat2[m(str[1])][m(str[0])] = -1;
		}
		scanf("%d",&n);
		scanf("%s",str);
		for(i=0;i<n;i++){//invoke
			//printf("\ni=%d\n",i);
			s=str[i];
			l.push_back(s);

			//isCombine();
			//printf("size=%d: ",l.size());
			if(l.size()<2) continue;//nothing to do
			rit=l.rbegin();
			k1=m(*rit);
			++rit;
			k2=m(*rit);
			//printf("%d %d\n",k1,k2);

			if(dat[k1][k2]>0){
				l.pop_back();
				l.pop_back();
				l.push_back(dat[k1][k2]);
				//printf("combinedsize=%d: ",l.size());
			}

			//isOpposed();
			for(rit=l.rbegin(),s=*rit,++rit;rit!=l.rend();rit++){
				if(dat2[m(*rit)][m(s)]==-1){//opposed
					//printf("OPPOSED\n");
					l.clear();
					break;
				}
			}

			/*for(it=l.begin();it!=l.end();it++){
				printf("%c, ",*it);
			}printf("\n");*/
		}

//printf("\n");
		printf("Case #%d: [", t);
		if(l.size()==0){
			printf("]\n");
			continue;
		}
		if(l.size()==1){
			printf("%c]\n",l.front());
			continue;
		}
		it=l.begin(); printf("%c",*it); it++;
		while(it!=l.end()){
			printf(", %c",*it);
			it++;
		}
		printf("]\n");
	}
	return 0;
}
